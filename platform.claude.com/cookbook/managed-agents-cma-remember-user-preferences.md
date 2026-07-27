<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-remember-user-preferences -->

# Build agents that remember your users

Most agents start every conversation from scratch. A customer tells your shopping assistant their size, their budget, and which materials they avoid, and the next time they return, the agent has forgotten everything. They have to repeat themselves, and the experience feels generic rather than personal.

We just introduced Memory in Claude Managed Agents to solve this. Think of it as a shared notebook your agent gets for each customer: Claude jots relevant things down during a session, and those notes are still there the next time the same customer comes back. Setup is a simple API call away.

In this guide you will build an example shopping assistant for a retail brand. The agent will learn a customer's preferences during their first visit, save them to a user-specific memory store, and recall them automatically on the next visit without being told again.

## What you will build

* A **memory store** that holds one customer's shopping preferences
* A **shopping agent** configured to check and update that store
* **Two separate sessions** that demonstrate memory carrying across visits
* A pattern for **inspecting and seeding** memories from your own application

## How memory works

When you attach a memory store to a session, it appears as a directory inside the agent's environment at `/mnt/memory/{store-name}`, and Claude reads and writes files there using its standard file tools. Your application has full read and write access to the same files through the REST API, so you can seed a store with known facts, audit what the agent has written, or export everything to your own systems.

> **Beta feature.** Memory stores are part of the Claude Managed Agents public beta. The API may change before general availability. The Python SDK adds the required `anthropic-beta` header automatically for every method under `client.beta`.

## Prerequisites

* An Anthropic API key with access to the Claude Managed Agents beta. Set it as the `ANTHROPIC_API_KEY` environment variable.
* Python 3.11 or later.
* The Anthropic Python SDK. Memory store methods require a recent release:

```
uv add anthropic
# or: pip install -U anthropic
```

## Set up the client

python

```
%%capture
%pip install -q "anthropic>=0.91.0"
```

python

```
import os

from anthropic import Anthropic
from utilities import wait_for_idle_status

MODEL = os.environ.get("COOKBOOK_MODEL", "claude-sonnet-4-6")

client = Anthropic()
```

### A helper for conversational turns

Managed agent sessions are event-driven: you send a user message, then stream events until the session goes idle. To keep the rest of this guide readable, wrap that loop in a helper that prints the agent's replies and the files it touches under `/mnt/memory/`.

python

```
def run_turn(session_id: str, user_text: str) -> str:
    """Send one user message and stream the agent's response until it goes idle.

    Returns the agent's full text reply for callers who want it programmatically.
    """
    print(f"\n[user]  {user_text}")
    reply_parts: list[str] = []

    with client.beta.sessions.events.stream(session_id) as stream:
        client.beta.sessions.events.send(
            session_id,
            events=[
                {
                    "type": "user.message",
                    "content": [{"type": "text", "text": user_text}],
                }
            ],
        )
        for event in stream:
            if event.type == "agent.message":
                for block in event.content:
                    if block.type == "text":
                        reply_parts.append(block.text)
                        print(f"[agent] {block.text}")

            elif event.type == "agent.tool_use":
                # Surface reads and writes to the memory mount so you can see
                # the agent checking and updating its memory.
                inp = event.input or {}
                target = inp.get("file_path") or inp.get("command", "")
                if "/mnt/memory/" in str(target):
                    print(f"  [memory] {event.name}: {target}")

            elif event.type == "session.status_idle":
                # Break on any idle reason so an unexpected stop_reason
                # (such as requires_action) cannot hang the loop.
                break

            elif event.type == "session.status_terminated":
                break

    wait_for_idle_status(client, session_id)
    return "".join(reply_parts)
```

## Step 1: Create a memory store

A memory store is a named container for text files, scoped to your workspace. In a production deployment you would typically create one store per end user and keep a mapping from your user IDs to store IDs in your own database.

The `description` you set here is rendered into the agent's system prompt whenever the store is attached, so use it to tell Claude what the store is for.

python

```
store = client.beta.memory_stores.create(
    name="Shopper Preferences",
    description=(
        "Personal shopping preferences for a single customer: "
        "sizes, style, budget, favorite brands, and materials to avoid."
    ),
)

print(store.id)  # memstore_01...
```

```
memstore_01NKkumXZXY8mEhoRA3xhBvN
```

## Step 2: Define the shopping agent

Every managed agent session needs an **agent** (the model, system prompt, and tools) and an **environment** (the container the agent runs in). You can create these once and reuse them across many customers and sessions.

Give the agent the built-in `agent_toolset`, which includes the file tools it uses to read and write memory. The `agent_toolset_20260401` type string is the toolset's API identifier, not a model alias, so you do not need to update it when newer models ship.

python

```
environment = client.beta.environments.create(
    name="shopping-demo",
    config={"type": "cloud", "networking": {"type": "limited"}},
)

agent = client.beta.agents.create(
    name="Personal Shopper",
    model=MODEL,
    system=(
        "You are a personal shopping assistant for a retail brand. "
        "Help the customer find products that match their taste and budget, "
        "and remember what you learn about them for future visits."
    ),
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {
                "enabled": True,
                "permission_policy": {"type": "always_allow"},
            },
        }
    ],
)

print(agent.id)  # agent_01...
```

```
agent_011CaMbJoHMUyR5TjeFDtMG9
```

## Step 3: First visit, where the agent learns preferences

Now start a session and attach the memory store through the `resources` array. The `instructions` field is per-attachment guidance that tells Claude how to use this particular store in this particular session.

Because this is the customer's first visit, the store is empty. Watch the `[memory]` lines in the output: the agent checks the store, finds nothing yet, and then writes a new file capturing what it learned.

python

```
memory_resource = {
    "type": "memory_store",
    "memory_store_id": store.id,
    "access": "read_write",
    "instructions": (
        "This customer's personal preferences: sizes, style, budget, and "
        "materials to avoid. Check it at the start of every conversation "
        "and update it whenever you learn something new."
    ),
}

session_one = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
    resources=[memory_resource],
)

# The response tells you where the store is mounted inside the agent's environment.
for resource in session_one.resources:
    if resource.type == "memory_store":
        print(f"Mounted at {resource.mount_path}")
```

```
Mounted at /mnt/memory/shopper-preferences
```

python

```
run_turn(
    session_one.id,
    "Hi! I'm looking for a new jacket. A few things about me: I wear a size "
    "medium, I only buy vegan leather (no animal leather please), my budget "
    "is usually under $200, and I love earth tones. What would you suggest?",
)
```

```
[user]  Hi! I'm looking for a new jacket. A few things about me: I wear a size medium, I only buy vegan leather (no animal leather please), my budget is usually under $200, and I love earth tones. What would you suggest?
[agent] Let me check if I have any info about you on file, and save your preferences right away!
  [memory] bash: cat /mnt/memory/shopper-preferences 2>/dev/null || echo "No file found"
  [memory] write: /mnt/memory/shopper-preferences
  [memory] write: /mnt/memory/shopper-preferences/preferences.md
[agent] I've saved your preferences for future visits! Now, here are some great **vegan leather jacket picks in earth tones under $200** that I'd suggest:

---

### 🌿 Top Picks for You

#### 1. **Olive Moto Jacket** — ~$110–$150
A classic biker silhouette in a deep **olive green** faux leather. Look for styles with zip-detail sleeves and a fitted waist. Great for casual or edgy looks.
- *Why you'll love it:* Earthy tone, very on-trend, versatile for layering.

#### 2. **Camel/Tan Oversized Blazer-Jacket** — ~$80–$160
A structured vegan leather blazer in **camel or tan** gives a polished, sophisticated vibe. Works dressed up or down.
- *Why you'll love it:* Classic earth tone, medium sizing runs well in this style, timeless investment.

#### 3. **Rust/Cognac Bomber Jacket** — ~$90–$170
A **rust or cognac-toned** vegan leather bomber is a bold earth-tone statement piece with a relaxed, comfortable fit.
- *Why you'll love it:* Rich warm color, bomber silhouettes are flattering in medium, cozy feel.

#### 4. **Terracotta Cropped Jacket** — ~$75–$140
A cropped vegan leather jacket in **terracotta** pairs beautifully with high-waisted jeans or wide-leg trousers.
- *Why you'll love it:* Trendy silhouette, stunning earthy hue, well within budget.

---

### 🛍️ Brands to Check Out
Here are some brands known for quality vegan leather within your budget:
- **ASOS** – Wide range of faux leather styles in various earth tones
- **Free People** – Boho-leaning earth tone options
- **H&M** – Affordable vegan leather jackets in seasonal colors
- **Lulus** – Great selection of trendy vegan styles under $100
- **Noize** – A dedicated vegan outerwear brand, often has earthy tones under $200

---

Do any of these styles appeal to you? I can help narrow it down further — for example, do you prefer a **fitted or relaxed fit**, or a particular style like moto, bomber, or blazer? 😊
```

## Step 4: Inspect what the agent saved

Everything the agent writes to the mount is a regular memory document that your application can read, edit, or delete through the API. List the store's contents with `view="full"` to include file content in the response.

This is how you build a "What we know about you" page in your product, sync memories into your own database, or let a human reviewer correct something the agent got wrong.

python

```
page = client.beta.memory_stores.memories.list(
    store.id,
    view="full",
)

for memory in page.data:
    if memory.type == "memory":
        print(f"=== {memory.path} ===")
        print(memory.content)
        print()
```

```
=== /preferences.md ===
# Shopper Preferences

## Sizes
- Tops/Jackets: Medium

## Style
- Loves earth tones (browns, tans, olive, terracotta, camel, rust, etc.)
- Interested in jackets

## Budget
- Usually under $200

## Materials
- VEGAN LEATHER ONLY — absolutely no animal leather
- (No other material restrictions noted yet)

## Favorite Brands
- None noted yet

## Other Notes
- First visit; preferences collected 2026-04-23
```

You should see a file (typically something like `/preferences.md`) containing the size, budget, material, and color preferences the customer mentioned, organized by topic. Claude chose the filename and structure on its own.

## Step 5: Return visit, where the agent recalls on its own

This is the moment that matters. Create a **brand new session** and attach the **same memory store**. The customer does not repeat any of their preferences, but the agent reads them from memory and tailors its recommendations accordingly.

python

```
session_two = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
    resources=[memory_resource],  # same store, new session
)

run_turn(
    session_two.id,
    "Hey, I'm back! I need a bag for work. Any recommendations?",
)
```

```
[user]  Hey, I'm back! I need a bag for work. Any recommendations?
[agent] Welcome back! Let me check your preferences before making any recommendations!
  [memory] read: /mnt/memory/shopper-preferences
  [memory] bash: ls /mnt/memory/shopper-preferences/
  [memory] read: /mnt/memory/shopper-preferences/preferences.md
[agent] Great news — I already have your preferences on file! Here's what I kept in mind for you:

- 🎨 **Style:** Earth tones (browns, tans, olive, camel, etc.)
- 💰 **Budget:** Under $200
- 🌱 **Materials:** Vegan leather only — no animal leather

With that in mind, here are some work bag recommendations that would suit you perfectly:

---

### 🛍️ Top Picks for a Work Bag

1. **Structured Tote in Camel Vegan Leather** — A polished, professional look in a warm earth tone. Fits a laptop + daily essentials. Great desk-to-commute bag.

2. **Olive Canvas & Vegan Leather Trim Laptop Bag** — A sleek crossbody/shoulder bag with a relaxed but put-together vibe. The canvas keeps it lightweight.

3. **Tan Vegan Leather Satchel** — A classic work satchel with a top handle and shoulder strap. Timeless silhouette, stays under budget.

4. **Terracotta Faux-Leather Tote** — A bold but grounded earth tone that adds personality to a work outfit without being over the top.

---

Do any of these styles appeal to you? I can also ask a few quick questions to narrow it down further:

- **Do you prefer a tote, backpack, crossbody, or briefcase-style?**
- **Do you need to carry a laptop, and if so, what size?**
- **Do you lean more structured/professional or relaxed/casual for work?**
```

In the output, notice that the agent reads `/mnt/memory/shopper-preferences/` before answering, then recommends bags that are vegan leather, in earth tones, and under $200, even though this message mentioned none of those things. The preferences carried across from the first session.

## Going further: patterns for production

### Seed a store from your existing data

If you already know things about a customer from their account profile or purchase history, you can write them into the store before the first session so the agent starts informed. In a real application you would run this seeding step before any sessions are created; it appears here, after the demo, only so the main learn-then-recall flow above stays focused.

> **Note:** Run this cell before the cleanup cell at the end of the notebook, since `store` is deleted there.

python

```
# Optional: run before the cleanup cell.
seeded = client.beta.memory_stores.memories.create(
    store.id,
    path="/purchase-history.md",
    content=(
        "## Recent purchases\n"
        "- Canvas tote, olive, $89 (Jan 2026)\n"
        "- Wool beanie, rust, $34 (Dec 2025)\n"
    ),
)
print(f"Seeded {seeded.path}")
```

```
Seeded /purchase-history.md
```

### Combine per-customer and shared stores

A session can attach up to eight memory stores, each with its own access level. A common pattern is one read-write store per customer plus a read-only store of brand-wide knowledge that every session shares.

```
catalog = client.beta.memory_stores.create(
    name="Product Catalog Notes",
    description="Current promotions, sizing guidance, and stock notes.",
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
    resources=[
        {
            "type": "memory_store",
            "memory_store_id": store.id,
            "access": "read_write",
            "instructions": "This customer's personal preferences.",
        },
        {
            "type": "memory_store",
            "memory_store_id": catalog.id,
            "access": "read_only",
            "instructions": "Brand-wide product guidance. Consult before recommending items.",
        },
    ],
)

# Remember to clean up the catalog store when you are done:
# client.beta.memory_stores.delete(catalog.id)
```

### Audit and correct

Every write to a memory store is recorded as an immutable version with the session that made it. Use `client.beta.memory_stores.memory_versions.list(...)` to review history, and `client.beta.memory_stores.memories.update(...)` to correct a file that the agent got wrong. See the [Memory API reference](https://docs.anthropic.com/en/docs/managed-agents/memory) for the full surface.

## Clean up

Delete the resources you created while following this guide.

python

```
wait_for_idle_status(client, session_one.id)
wait_for_idle_status(client, session_two.id)

client.beta.sessions.archive(session_one.id)
client.beta.sessions.archive(session_two.id)
client.beta.memory_stores.delete(store.id)
client.beta.agents.archive(agent.id)
client.beta.environments.archive(environment.id)
```

## Summary

You built a shopping agent that remembers its customers across visits by:

1. Creating a memory store for the customer
2. Attaching it to each session through `resources`
3. Letting Claude read and write files under `/mnt/memory/` as it learned new preferences
4. Inspecting those files from your own application through the Memory API

From here you can map your own user IDs to memory store IDs, seed stores from your existing customer data, and layer shared read-only stores on top for brand-wide knowledge.

### Other notebooks in this series

* [`CMA_iterate_fix_failing_tests.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_iterate_fix_failing_tests.ipynb) — the entry-point notebook. Introduces agents, environments, sessions, file mounts, and the streaming event loop through a do-observe-fix loop on a failing test suite.
* [`CMA_operate_in_production.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_operate_in_production.ipynb) — production setup story: vault-backed MCP credentials, the `session.status_idled` webhook for HITL without long-lived connections, and the resource lifecycle CRUD verbs.

### Learn more

* [Claude Managed Agents overview](https://docs.anthropic.com/en/docs/managed-agents/overview)
* [Memory stores API reference](https://docs.anthropic.com/en/docs/managed-agents/memory)
* [Session resources](https://docs.anthropic.com/en/docs/managed-agents/memory#attach-a-memory-store-to-a-session)
