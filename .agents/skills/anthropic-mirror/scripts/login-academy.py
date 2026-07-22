"""skilljar(Anthropic Academy) 로그인 세션 생성 + 쿠키 저장.

`crwl profiles`는 CDP(localhost -> IPv6 ::1) 버그로 macOS에서 실패하므로,
playwright persistent context로 헤드풀 로그인한다. 로그인 후 claude-101을 재확인해
성공/실패를 즉시 판정하고, 정상 종료(ctx.close)로 쿠키를 디스크에 flush한다.
academy-extract.py가 STATE(storage_state)의 쿠키를 읽어 추출한다.

다른 skilljar 인스턴스(예: 파트너 포털 anthropic-partners.skilljar.com, partner-sso OAuth 로그인)는
SKILLJAR_BASE 환경변수로 지정한다. 프로필·STATE는 도메인별로 분리돼 세션이 섞이지 않는다.

실행: python3 login-academy.py   (헤드풀 브라우저가 떠야 하므로 사용자 터미널에서 직접)
  SKILLJAR_BASE=https://anthropic-partners.skilljar.com python3 login-academy.py  (파트너 포털)
"""
import asyncio, os
from playwright.async_api import async_playwright

BASE = os.environ.get("SKILLJAR_BASE", "https://anthropic.skilljar.com").rstrip("/")
_HOST = BASE.split("://")[-1]
# 기본 도메인은 기존 경로 유지(하위호환), 그 외는 도메인별 파일로 분리
_TAG = "anthropic-academy" if _HOST == "anthropic.skilljar.com" else _HOST
PROFILE = os.path.expanduser(f"~/.crawl4ai/profiles/{_TAG}")
STATE = os.path.expanduser("~/.crawl4ai/academy_state.json" if _HOST == "anthropic.skilljar.com"
                           else f"~/.crawl4ai/skilljar-{_HOST}.json")
LOGIN = f"{BASE}/auth/login"
CHECK = f"{BASE}/"  # 도메인마다 코스 슬러그가 달라 루트로 확인(로그인 판정은 sj_ 쿠키로)


async def main():
    os.makedirs(PROFILE, exist_ok=True)
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            PROFILE, headless=False,
            args=["--password-store=basic", "--disable-blink-features=AutomationControlled",
                  "--no-first-run", "--no-default-browser-check"])
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
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
        try:
            await page.goto(CHECK, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)
        except Exception:
            pass
        cookies = await ctx.cookies()
        auth = [c["name"] for c in cookies if "skilljar" in c["domain"] and c["name"].startswith("sj_")]
        await ctx.storage_state(path=STATE)
        if auth:
            print(f" [OK] 로그인 성공. 인증 쿠키 {auth}. 쿠키 저장 -> {STATE}")
        else:
            print(" [!] sj_ 인증 쿠키 없음 - 로그인이 완료되지 않았습니다. 다시 실행하세요.")
        await ctx.close()


asyncio.run(main())
