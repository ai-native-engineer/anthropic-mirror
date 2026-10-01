"""skilljar(Anthropic Academy) 로그인 세션 생성 + 쿠키 저장.

`crwl profiles`는 CDP(localhost -> IPv6 ::1) 버그로 macOS에서 실패하므로,
playwright persistent context로 헤드풀 로그인한다. 로그인 후 claude-101을 재확인해
성공/실패를 즉시 판정하고, 정상 종료(ctx.close)로 쿠키를 디스크에 flush한다.
academy-extract.py가 STATE(storage_state)의 쿠키를 읽어 추출한다.

다른 skilljar 인스턴스(예: 파트너 포털 anthropic-partners.skilljar.com, partner-sso OAuth 로그인)는
SKILLJAR_BASE 환경변수로 지정한다. 프로필·STATE는 도메인별로 분리돼 세션이 섞이지 않는다.

실행: <crawl4ai python> login-academy.py   (헤드풀 브라우저가 떠야 하므로 사용자 터미널에서 직접)
  agents-env run --local SKILLJAR_EMAIL SKILLJAR_PASSWORD -- <crawl4ai python> login-academy.py --auto
    (이메일·비밀번호 폼 인스턴스만. 헤드리스로 폼을 채우고 Remember me를 켠다. 실패하면 exit 3)
  SKILLJAR_BASE=https://anthropic-partners.skilljar.com <crawl4ai python> login-academy.py  (파트너 포털)

playwright가 있는 인터프리터로 실행해야 한다. shebang을 두지 않으므로 `./login-academy.py`로는
실행되지 않는다 -- 실행 권한만 붙은 shebang 없는 파일은 셸이 셸 스크립트로 해석해 아무 출력 없이
끝난다. refresh.sh가 쓰는 CRAWL4AI_PYTHON과 같은 인터프리터를 쓴다.
"""

import asyncio, os, sys
from playwright.async_api import async_playwright

BASE = os.environ.get("SKILLJAR_BASE", "https://anthropic.skilljar.com").rstrip("/")
_HOST = BASE.split("://")[-1]
# 기본 도메인은 기존 경로 유지(하위호환), 그 외는 도메인별 파일로 분리
_TAG = "anthropic-academy" if _HOST == "anthropic.skilljar.com" else _HOST
PROFILE = os.path.expanduser(f"~/.crawl4ai/profiles/{_TAG}")
STATE = os.path.expanduser(
    "~/.crawl4ai/academy_state.json"
    if _HOST == "anthropic.skilljar.com"
    else f"~/.crawl4ai/skilljar-{_HOST}.json"
)
LOGIN = f"{BASE}/auth/login"
CHECK = (
    f"{BASE}/"  # 도메인마다 코스 슬러그가 달라 루트로 확인(로그인 판정은 sj_ 쿠키로)
)


AUTO = "--auto" in sys.argv[1:]


async def auto_login(page):
    """Skilljar 계정 폼(email/password)을 채운다. 폼이 다르면(파트너 SSO 등) False."""
    email, password = os.environ.get("SKILLJAR_EMAIL"), os.environ.get("SKILLJAR_PASSWORD")
    if not (email and password):
        print(" [!] SKILLJAR_EMAIL / SKILLJAR_PASSWORD 환경변수가 없습니다(agents-env run으로 주입).")
        return False
    await page.goto(LOGIN, wait_until="domcontentloaded")
    await page.wait_for_timeout(2000)
    if not await page.locator("#id_login").count() or not await page.locator("#id_password").count():
        print(f" [!] {page.url}: 이메일·비밀번호 폼이 아닙니다(SSO 인스턴스는 수동 로그인).")
        return False
    await page.fill("#id_login", email)
    await page.fill("#id_password", password)
    if await page.locator("#id_remember").count():
        await page.check("#id_remember")
    await page.click("#login_form button[type=submit]")
    await page.wait_for_load_state("domcontentloaded")
    await page.wait_for_timeout(4000)
    return True


async def main():
    os.makedirs(PROFILE, exist_ok=True)
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            PROFILE,
            headless=AUTO,
            args=[
                "--password-store=basic",
                "--disable-blink-features=AutomationControlled",
                "--no-first-run",
                "--no-default-browser-check",
            ],
        )
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        if AUTO:
            await auto_login(page)
        else:
            await interactive_login(page)
        try:
            await page.goto(CHECK, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)
        except Exception:
            pass
        signed_in = await check_signed_in(page)
        await ctx.storage_state(path=STATE)
        await ctx.close()
    if signed_in:
        print(f" [OK] 로그인 확인. 쿠키 저장 -> {STATE}")
        return
    print(" [!] 로그인되지 않았습니다(/accounts/ 가 로그인 페이지로 이동).")
    if not AUTO:
        print("     브라우저에서 로그인을 끝낸 뒤 터미널에서 Enter를 눌러야 합니다.")
        print("     이 스크립트를 백그라운드로 실행하면 Enter가 EOF로 들어가 로그인 전에 저장됩니다.")
    raise SystemExit(3)


async def interactive_login(page):
    await page.goto(LOGIN)
    print("=" * 56)
    print(" 브라우저에서 이메일+비밀번호로 로그인하세요.")
    print(" 로그인 후 이 터미널로 와서 Enter 를 누르세요.")
    print(" * Ctrl+C 누르지 마세요 - 쿠키가 저장되지 않습니다.")
    print("=" * 56)
    try:
        input(" >> 로그인 완료 후 Enter: ")
    except (EOFError, KeyboardInterrupt):
        print("\n (입력 중단 - 현재 세션 저장 시도)")


async def check_signed_in(page):
    # 로그인 판정은 /accounts/ 착지점으로 한다. sj_sessionid는 익명 세션에도 발급되고
    # 루트 HTML의 'auth/logout' 문자열도 로그아웃 상태에 남아 있어, 둘 다 쓰면
    # 로그인하지 않은 세션이 '성공'으로 저장된다(그 상태로 수집하면 레슨 본문이
    # 코스 소개글로 덮인다).
    try:
        await page.goto(f"{BASE}/accounts/", wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)
        return "/accounts/login" not in page.url
    except Exception:
        return False


asyncio.run(main())
