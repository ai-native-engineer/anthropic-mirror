<!-- source: https://platform.claude.com/cookbook/tool-use-memory-cookbook -->

#  Context Editing & Memory for Long-Running Agents

AI agents that run across multiple sessions or handle long-running tasks face two key challenges: they lose learned patterns between conversations, and context windows fill up during extended interactions.

This cookbook demonstrates how to address these challenges using Claude's memory tool and context editing capabilities.

##  Table of Contents

1. [Introduction: Why Memory Matters](#introduction)
2. [Use Cases](#use-cases)
3. [Quick Start Examples](#quick-start)
4. [How It Works](#how-it-works)
5. [Code Review Assistant Demo](#demo)
6. [Real-World Applications](#real-world)
7. [Best Practices](#best-practices)

##  Prerequisites

**Required Knowledge:**

* Python fundamentals (functions, classes, async/await basics)
* Basic understanding of REST APIs and JSON

**Required Tools:**

* Python 3.10 or higher
* Anthropic API key ([get one here(opens in new tab)](https://console.anthropic.com/))

**Recommended:**

* Familiarity with concurrent programming concepts (threads, async)
* Basic understanding of context windows in LLMs

##  Setup

###  For VSCode Users

# 1. Create virtual environment

python -m venv .venv

# 2. Activate it

source .venv/bin/activate # macOS/Linux

# or: .venv\Scripts\activate # Windows

# 3. Install dependencies

pip install -r requirements.txt

# 4. In VSCode: Select .venv as kernel (top right)

###  API Key

cp .env.example .env

# Edit .env and add your ANTHROPIC\_API\_KEY

Get your API key from: [https://console.anthropic.com/(opens in new tab)](https://console.anthropic.com/)

##  1. Introduction: Why Memory Matters

This cookbook demonstrates practical implementations of the context engineering patterns described in [Effective context engineering for AI agents(opens in new tab)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). That post covers why context is a finite resource, how attention budgets work, and strategies for building effective agents—the techniques you'll see in action here.

###  The Problem

Large language models have finite context windows (200k tokens for the Claude 4 family of models). While this seems large, several challenges emerge:

* **Context limits**: Long conversations or complex tasks can exceed available context
* **Computational cost**: Processing large contexts is expensive - attention mechanisms scale quadratically
* **Repeated patterns**: Similar tasks across conversations require re-explaining context every time
* **Information loss**: When context fills up, earlier important information gets lost

###  The Solution

Claude 4 models introduce powerful context management capabilities:

1. **Memory Tool** (`memory_20250818`): Enables cross-conversation learning

   * Claude can write down what it learns for future reference
   * File-based system under `/memories` directory
   * Client-side implementation gives you full control
2. **Context Editing**: Automatically manages context with two strategies:

   * **Tool use clearing** (`clear_tool_uses_20250919`): Clears old tool results when context grows large
   * **Thinking management** (`clear_thinking_20251015`): Manages extended thinking blocks (requires thinking enabled)
   * Configurable triggers and retention policies

###  The Benefit

Build AI agents that **get better at your specific tasks over time**:

* **Session 1**: Claude solves a problem, writes down the pattern
* **Session 2**: Claude applies the learned pattern immediately (faster!)
* **Long sessions**: Context editing keeps conversations manageable

Think of it as giving Claude a notebook to take notes and refer back to - just like humans do.

###  What You'll Learn

By the end of this cookbook, you will be able to:

* **Implement** the memory tool for cross-conversation learning
* **Configure** context editing to manage long-running sessions
* **Apply** best practices for memory security and organization

##  1. Introduction: Why Memory Matters

This cookbook demonstrates practical implementations of the context engineering patterns described in [Effective context engineering for AI agents(opens in new tab)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). That post covers why context is a finite resource, how attention budgets work, and strategies for building effective agents—the techniques you'll see in action here.

###  The Problem

Large language models have finite context windows (200k tokens for Claude 4). While this seems large, several challenges emerge:

* **Context limits**: Long conversations or complex tasks can exceed available context
* **Computational cost**: Processing large contexts is expensive - attention mechanisms scale quadratically
* **Repeated patterns**: Similar tasks across conversations require re-explaining context every time
* **Information loss**: When context fills up, earlier important information gets lost

###  The Solution

Claude Sonnet 4.6 introduces two powerful capabilities:

1. **Memory Tool** (`memory_20250818`): Enables cross-conversation learning
   * Claude can write down what it learns for future reference
   * File-based system under `/memories` directory
   * Client-side implementation gives you full control

**Supported Models**: Claude Opus 4.1 (`claude-opus-4-1`), Claude Opus 4 (`claude-opus-4`), Claude Sonnet 4.6 (`claude-sonnet-4-6`), Claude Sonnet 4 (`claude-sonnet-4`), and Claude Haiku 4.5 (`claude-haiku-4-5`)

###  The Benefit

Build AI agents that **get better at your specific tasks over time**:

* **Session 1**: Claude solves a problem, writes down the pattern
* **Session 2**: Claude applies the learned pattern immediately (faster!)
* **Long sessions**: Context editing keeps conversations manageable

Think of it as giving Claude a notebook to take notes and refer back to - just like humans do.

##  2. Use Cases

Memory and context management enable powerful new workflows:

###  🔍 Code Review Assistant

* Learns debugging patterns from past reviews
* Recognizes similar bugs instantly in future sessions
* Builds team-specific code quality knowledge
* **Production ready**: Integrate with [claude-code-action(opens in new tab)](https://github.com/anthropics/claude-code-action) for GitHub PR reviews

###  📚 Research Assistant

* Accumulates knowledge on topics over multiple sessions
* Connects insights across different research threads
* Maintains bibliography and source tracking

###  💬 Customer Support Bot

* Learns user preferences and communication style
* Remembers common issues and solutions
* Builds product knowledge base from interactions

###  📊 Data Analysis Helper

* Remembers dataset patterns and anomalies
* Stores analysis techniques that work well
* Builds domain-specific insights over time

**Supported Models**: Claude Opus 4.1 (`claude-opus-4-1`) and Claude Sonnet 4.6 (`claude-sonnet-4-6`)

**This cookbook focuses on the Code Review Assistant** as it clearly demonstrates both memory (learning patterns) and context editing (handling long reviews).

##  3. Quick Start Examples

Let's see memory and context management in action with simple examples.

###  Setup

First, install dependencies and configure your environment:

%%capture

# Install required packages

# Option 1: From requirements.txt

# %pip install -q -r requirements.txt

# Option 2: Direct install

%pip install -q anthropic python-dotenv ipykernel

**⚠️ Important**: Create a `.env` file in this directory:

# Copy .env.example to .env and add your API key

cp .env.example .env

Then edit `.env` to add your Anthropic API key from [https://console.anthropic.com/(opens in new tab)](https://console.anthropic.com/)

import os

from typing import cast

from anthropic import Anthropic

from dotenv import load\_dotenv

# Load environment variables

load\_dotenv()

# Model configuration - use alias for automatic updates

MODEL = "claude-sonnet-4-6" # Can override via ANTHROPIC\_MODEL env var

if os.getenv("ANTHROPIC\_MODEL"):

MODEL = os.getenv("ANTHROPIC\_MODEL")

if not API\_KEY:

raise ValueError("ANTHROPIC\_API\_KEY not found. Copy .env.example to .env and add your API key.")

if not MODEL:

raise ValueError("ANTHROPIC\_MODEL not found. Copy .env.example to .env and set the model.")

MODEL = cast(str, MODEL)

client = Anthropic(api\_key=API\_KEY)

print("✓ API key loaded")

print(f"✓ Using model: {MODEL}")

```
✓ API key loaded
✓ Using model: claude-sonnet-4-6
```

###  Example 1: Basic Memory Usage

Let's see Claude use memory to store information for future reference.

**Helper Functions**

These examples use helper functions from `demo_helpers.py`:

* **`run_conversation_loop()`**: Handles the API conversation loop

  + Calls Claude's API with memory tool enabled
  + Executes tool uses (memory operations)
  + Continues until Claude stops using tools
  + Returns the final response
* **`run_conversation_turn()`**: Single turn (used in Example 3)

  + Same as above but returns after one API call
  + Useful when you need fine-grained control
* **`print_context_management_info()`**: Displays context clearing stats

  + Shows tokens saved, tool uses cleared
  + Helps visualize when context editing triggers

**⚠️ Note on Memory Clearing**

The following cell clears all memory files to provide a clean slate for this demonstration. This is useful for running the notebook multiple times to see consistent results.

**In production applications**, you should carefully consider whether to clear all memory, as it permanently removes learned patterns. Consider using selective deletion or organizing memory into project-specific directories instead.

# Import helper functions

from memory\_demo.demo\_helpers import (

run\_conversation\_loop,

run\_conversation\_turn,

print\_context\_management\_info,

)

from memory\_tool import MemoryToolHandler

# Initialize

client = Anthropic()

memory = MemoryToolHandler(base\_path="./demo\_memory")

# Clear any existing memories to start fresh

print("🧹 Clearing previous memories...")

memory.clear\_all\_memory()

print("✓ Memory cleared\n")

# Load example code with a race condition bug

with open("memory\_demo/sample\_code/web\_scraper\_v1.py", "r") as f:

code\_to\_review = f.read()

messages = [

{

"role": "user",

"content": f"I'm reviewing a multi-threaded web scraper that sometimes returns fewer results than expected. The count is inconsistent across runs. Can you find the issue?\n\n```python\n{code\_to\_review}\n```",

}

]

print("=" \* 60)

print("📝 SESSION 1: Learning from a bug")

print("=" \* 60)

# Run conversation loop

response = run\_conversation\_loop(

client=client,

model=MODEL,

messages=messages,

memory\_handler=memory,

system="You are a code reviewer.",

max\_tokens=2048,

max\_turns=5,

verbose=True,

)

print("\n" + "=" \* 60)

print("✅ Session 1 complete!")

print("=" \* 60)

```
🧹 Clearing previous memories...
✓ Memory cleared

============================================================
📝 SESSION 1: Learning from a bug
============================================================

🔄 Turn 1:
💬 Claude: I'll review this code for the race condition issue. Let me first check my memory, then analyze the problem.

  🔧 Memory tool: view /memories
  ✓ Result: Directory: /memories
(empty)

🔄 Turn 2:
  🔧 Memory tool: create /memories/review.md
  ✓ Result: File created successfully at /memories/review.md

🔄 Turn 3:
💬 Claude: ## Code Review: Multi-threaded Web Scraper Race Condition

### 🔴 **Critical Issue Found: Race Condition in Shared State**

You've correctly identified the problem! The code has **race conditions** caused by multiple threads modifying shared lists without synchronization.

---

### **The Problem**

**Lines with race conditions:**
```python
self.results.append(result)  # RACE CONDITION
```

**Problem:**
- Python's `list.append()` is **NOT thread-safe** for concurrent modifications
- Multiple threads simultaneously appending can cause:
  - **Lost updates:** One thread's append overwrites another's
  - **Inconsistent state:** Internal list structure can be corrupted
  - **Unpredictable counts:** Results randomly dropped

**Why it happens:**
`list.append()` involves multiple operations:
1. Read current list size
2. Allocate space
3. Insert item
4. Update size

# In scrape_urls():
if "error" in result:
    self.failed_urls.append(result["url"])  # ⚠️ NOT THREAD-SAFE
else:
    self.results.append(result)  # ⚠️ NOT THREAD-SAFE
```

**Why this causes lost results:**
- Python's `list.append()` is **not atomic** in all scenarios
- When multiple threads call `append()` simultaneously, the internal list operations can interleave
- This can cause lost updates where one thread's append overwrites another's

---

### **Solutions**

#### **Option 1: Use Thread Locks (Traditional approach)**
```python
import threading

class WebScraper:
    """Web scraper that fetches multiple URLs concurrently."""

    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        self.results = []
        self.failed_urls = []
        self.lock = threading.Lock()  # ✅ Add lock

    def scrape_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.fetch_url, url) for url in urls]

            for future in as_completed(futures):
                result = future.result()

                # ✅ Protect shared state with lock
                with self.lock:
                    if "error" in result:
                        self.failed_urls.append(result["url"])
                    else:
                        self.results.append(result)

        return self.results
```

#### **Option 2: Use Thread-Safe Collections**
```python
from queue import Queue

class WebScraper:
    """Web scraper that fetches multiple URLs concurrently."""

    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        self.results = Queue()  # ✅ Thread-safe
        self.failed_urls = Queue()  # ✅ Thread-safe

    def scrape_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.fetch_url, url) for url in urls]

            for future in as_completed(futures):
                result = future.result()

                if "error" in result:
                    self.failed_urls.put(result["url"])
                else:
                    self.results.put(result)

        # Convert Queue to list for return
        return list(self.results.queue)
```

#### **Option 3: Collect Results from Futures (Best approach)**
```python
def scrape_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
    """
    ✅ FIXED: Collect results in main thread, avoiding shared state.
    """
    results = []  # Local to main thread
    failed_urls = []  # Local to main thread

    with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
        futures = [executor.submit(self.fetch_url, url) for url in urls]

        for future in as_completed(futures):
            result = future.result()

            # ✅ Only main thread accesses these lists
            if "error" in result:
                failed_urls.append(result["url"])
            else:
                results.append(result)

    # Update instance variables once, in main thread
    self.results = results
    self.failed_urls = failed_urls

    return self.results
```

---

### **Recommended Fix (Complete)**

Here's the fully corrected version using **Option 3** (cleanest approach):

```python
"""
Concurrent web scraper - FIXED VERSION
Results collected in main thread to avoid race conditions.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any

import requests

class WebScraper:
    """Web scraper that fetches multiple URLs concurrently."""

    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        self.results = []
        self.failed_urls = []

    def fetch_url(self, url: str) -> Dict[str, Any]:
        """Fetch a single URL and return the result."""
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return {
                "url": url,
                "status": response.status_code,
                "content_length": len(response.content),
            }
        except requests.exceptions.RequestException as e:
            return {"url": url, "error": str(e)}

    def scrape_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Scrape multiple URLs concurrently.

        ✅ FIXED: Results collected in main thread only.
        """
        results = []  # ✅ Local variables - no race condition
        failed_urls = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.fetch_url, url) for url in urls]

            for future in as_completed(futures):
                result = future.result()

                # ✅ Only the main thread modifies these lists
                if "error" in result:
                    failed_urls.append(result["url"])
                else:
                    results.append(result)

        # Update instance variables after all threads complete
        self.results = results
        self.failed_urls = failed_urls

        return self.results

    def get_stats(self) -> Dict[str, int]:
        """Get scraping statistics."""
        return {
            "total_results": len(self.results),
            "failed_urls": len(self.failed_urls),
            "success_rate": (
                len(self.results) / (len(self.results) + len(self.failed_urls))
                if (len(self.results) + len(self.failed_urls)) > 0
                else 0
            ),
        }

if __name__ == "__main__":
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/500",
    ] * 10  # 50 URLs total

    scraper = WebScraper(max_workers=10)
    results = scraper.scrape_urls(urls)

    print(f"Expected: 50 results")
    print(f"Got: {len(results)} results")  # ✅ Now always 50
    print(f"Stats: {scraper.get_stats()}")
```

---

### **Summary**

- **Root cause**: Multiple threads appending to shared lists (`self.results` and `self.failed_urls`) without synchronization
- **Impact**: Lost updates leading to inconsistent result counts
- **Best fix**: Collect results in local variables within the main thread, then update instance variables once
- **Why this works**: Only one thread (main) accesses the result lists, eliminating the race condition entirely

The key insight: **Avoid shared mutable state in concurrent code**. Let worker threads return values and collect them in the coordinating thread.

  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully

============================================================
✅ Session 1 complete!
============================================================
```

**What happened?**

1. Claude checked its memory (empty on first run)
2. Identified the bug: **race condition** - multiple threads modifying shared state (`self.results` and `self.failed_urls`) without synchronization
3. Stored the concurrency pattern in memory for future reference

Now let's see the magic - Claude applying this learned pattern in a **new conversation**:

###  Example 2: Cross-Conversation Learning

Start a completely new conversation - memory persists!

# NEW conversation (empty messages)

# Load API client code with similar concurrency issue

with open("memory\_demo/sample\_code/api\_client\_v1.py", "r") as f:

code\_to\_review = f.read()

messages = [

{"role": "user", "content": f"Review this API client code:\n\n```python\n{code\_to\_review}\n```"}

]

print("=" \* 60)

print("🚀 SESSION 2: Applying learned pattern")

print("=" \* 60)

# Run conversation loop

response = run\_conversation\_loop(

client=client,

model=MODEL,

messages=messages,

memory\_handler=memory,

system="You are a code reviewer.",

max\_tokens=2048,

max\_turns=5,

verbose=True,

)

print("\n" + "=" \* 60)

print("✅ Session 2 complete!")

print("=" \* 60)

```
============================================================
🚀 SESSION 2: Applying learned pattern
============================================================

🔄 Turn 1:
  🔧 Memory tool: view /memories
  ✓ Result: Directory: /memories
- review.md

🔄 Turn 2:
  🔧 Memory tool: view /memories/review.md
  ✓ Result:    1: # Code Review: Multi-threaded Web Scraper
   2:
   3: ## Issue
   4: Revi...

🔄 Turn 3:
  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully

🔄 Turn 4:
💬 Claude: ## Code Review: Async API Client

### Summary
This code has **concurrency issues** related to shared mutable state being accessed from multiple coroutines without proper synchronization. While the author correctly identifies these as bugs in comments, let me provide a comprehensive review.

However, the actual race condition risk here is **somewhat overstated** because:
- List `.append()` is atomic in CPython
- The `+=` operation on integers is also atomic
- Coroutines only switch at `await` points, and there are none between the operations

**BUT** this is still problematic because:
- It relies on CPython implementation details
- It's not guaranteed by the language specification
- The code is not portable to other Python implementations
- Future refactoring could introduce `await` points that cause real races

#### 1. **Race Condition on `self.error_count` (Line 51)**
```python
self.error_count += 1  # Not atomic!
```

**Problem**: Even in async code, this operation is not atomic. While asyncio is single-threaded, the `+=` operator involves:
1. Read current value
2. Add 1
3. Write back

An `await` in another coroutine between steps 1-3 can cause lost updates.

**Impact**: Error count will be incorrect/underreported.

#### 2. **Unsafe List Append on `self.responses` (Line 53)**
```python
self.responses.append(result)  # Not thread-safe in async context!
```

**Problem**: While `list.append()` is technically atomic in CPython due to GIL, this is:
- An implementation detail, not guaranteed by the language spec
- Bad practice that makes the code fragile
- Still problematic because the list is being modified while potentially being read elsewhere

**Impact**: Potential data corruption, missing responses, or incorrect counts.

#### 3. **Logic Error: Errors Not Included in Results**
```python
if "error" in result:
    self.error_count += 1  # Counted but not stored!
else:
    self.responses.append(result)  # Only successes stored
```

**Problem**: Failed requests increment `error_count` but are **never added to `self.responses`**. This means:
- The return value of `fetch_all()` only contains successful responses
- Error details are lost
- The summary calculation is inconsistent

---

### ⚠️ **Design Issues**

#### 4. **Stateful Class Design is Anti-Pattern for Concurrent Operations**
The class maintains mutable state (`responses`, `error_count`) that's modified during concurrent operations. This is problematic because:
- Makes the client non-reusable (calling `fetch_all()` twice will mix results)
- Harder to reason about state consistency
- Requires manual reset between calls

**Better approach**: Return data directly rather than accumulating in instance variables.

#### 5. **Inconsistent Error Handling**
Errors are caught and converted to dictionaries, but then handled differently from successes. This makes the API inconsistent and loses valuable error information.

---

### 🟡 **Minor Issues**

#### 6. **Missing Type Hints**
The module imports `Optional` but never uses it. The return types could be more specific.

#### 7. **Hardcoded Test Data in Main**
The `* 20` multiplier and specific endpoints make testing less flexible.

**Fix:** Use `asyncio.gather()` which is simpler and more idiomatic for this use case.

### 5. **Missing HTTP Status Code Validation**
**Location:** `fetch_endpoint()` method

  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully

🔄 Turn 5:
💬 Claude: Here's a **corrected version**:

**Fix:**
```python
"""
Async API client with proper concurrency handling.
"""

import asyncio
from typing import List, Dict, Any
from dataclasses import dataclass

import aiohttp

@dataclass
class FetchResult:
    """Result from fetching an endpoint."""
    endpoint: str
    status: int = 0
    data: Any = None
    error: str = None

    @property
    def is_success(self) -> bool:
        return self.error is None

class AsyncAPIClient:
    """Async API client for fetching data from multiple endpoints."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def fetch_endpoint(
        self, session: aiohttp.ClientSession, endpoint: str
    ) -> FetchResult:
        """Fetch a single endpoint."""
        url = f"{self.base_url}/{endpoint}"
        try:
            async with session.get(
                url, timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                data = await response.json()
                return FetchResult(
                    endpoint=endpoint,
                    status=response.status,
                    data=data,
                )
        except Exception as e:
            return FetchResult(
                endpoint=endpoint,
                error=str(e),
            )

    async def fetch_all(self, endpoints: List[str]) -> List[FetchResult]:
        """
        Fetch multiple endpoints concurrently.

        Fixed: Returns all results directly without modifying shared state.
        Uses asyncio.gather() which is cleaner than as_completed() for this use case.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_endpoint(session, endpoint) for endpoint in endpoints]
            # gather() returns results in order and handles all concurrency
            results = await asyncio.gather(*tasks)
            return results

    @staticmethod
    def get_summary(results: List[FetchResult]) -> Dict[str, Any]:
        """Get summary statistics from results."""
        successes = sum(1 for r in results if r.is_success)
        errors = len(results) - successes

        return {
            "total_responses": len(results),
            "successful": successes,
            "errors": errors,
            "success_rate": successes / len(results) if results else 0,
        }

async def main():
    """Test the async API client."""
    client = AsyncAPIClient("https://jsonplaceholder.typicode.com")

    endpoints = [
        "posts/1",
        "posts/2",
        "posts/3",
        "users/1",
        "users/2",
        "invalid/endpoint",  # Will error
    ] * 20  # 120 requests total

    results = await client.fetch_all(endpoints)

    # Separate successes and errors for clarity
    successes = [r for r in results if r.is_success]
    errors = [r for r in results if not r.is_success]

    print(f"Expected: 120 total responses (100 successful, 20 errors)")
    print(f"Got: {len(results)} responses ({len(successes)} successful, {len(errors)} errors)")
    print(f"Summary: {AsyncAPIClient.get_summary(results)}")

    if errors:
        print(f"\nFirst error: {errors[0].endpoint} - {errors[0].error}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

### **Key Improvements in Fixed Version:**

1. ✅ **No shared mutable state** - Results returned directly
2. ✅ **All results captured** - Both successes and errors included
3. ✅ **Type-safe with dataclass** - Clear structure for results
4. ✅ **Reusable client** - Can call `fetch_all()` multiple times safely
5. ✅ **Consistent error handling** - All results have same structure
6. ✅ **Simpler concurrency** - Uses `asyncio.gather()` instead of `as_completed()`
7. ✅ **Static summary method** - Takes results as parameter, no state dependency

---

### **Alternative: If You Need Shared State**

If you absolutely need to accumulate results in the instance (e.g., for streaming/progressive updates), use an `asyncio.Lock`:

```python
import asyncio

class AsyncAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.responses = []
        self.error_count = 0
        self._lock = asyncio.Lock()  # Add lock

    async def fetch_all(self, endpoints: List[str]) -> List[Dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_endpoint(session, endpoint) for endpoint in endpoints]

            for coro in asyncio.as_completed(tasks):
                result = await coro

                # Protect shared state with lock
                async with self._lock:
                    if "error" in result:
                        self.error_count += 1
                    else:
                        self.responses.append(result)

        return self.responses
```

However, the stateless design I showed first is **strongly preferred** for async code.

import asyncio
from typing import List, Dict, Any, TypedDict

### **Testing Recommendation**

Add tests that verify all 120 requests are accounted for:

```python
async def test_all_results_captured():
    client = AsyncAPIClient("https://jsonplaceholder.typicode.com")
    endpoints = ["posts/1"] * 100
    results = await client.fetch_all(endpoints)
    assert len(results) == 100, f"Expected 100, got {len(results)}"
```

============================================================
✅ Session 2 complete!
============================================================
```

**Notice the difference:**

* Claude **immediately checked memory** and found the thread-safety/concurrency pattern
* Recognized the similar issue in async code **instantly** without re-learning
* Response was **faster** because it applied stored knowledge about shared mutable state

This is **cross-conversation learning** in action!

###  Example 3: Context Clearing While Preserving Memory

What happens during a **long review session** with many code files?

* Context fills up with tool results from previous reviews
* But memory (learned patterns) must persist!

Let's trigger **context editing** to see how Claude manages this automatically.

**Note on configuration:** We use `clear_at_least: 50` tokens because memory tool operations have small results (~50-150 tokens each). In production with larger tool results (like web search or code execution), you'd use higher values like 3000-5000 tokens.

# Configure context management with BOTH clearing strategies

# Low thresholds for demo - in production use 30-40k tokens

CONTEXT\_MANAGEMENT = {

"edits": [

# Thinking management MUST come first when combining strategies

{

"type": "clear\_thinking\_20251015",

"keep": {"type": "thinking\_turns", "value": 1} # Keep only last turn's thinking

},

{

"type": "clear\_tool\_uses\_20250919",

"trigger": {"type": "input\_tokens", "value": 5000}, # Low threshold for demo

"keep": {"type": "tool\_uses", "value": 2}, # Keep last 2 tool uses

"clear\_at\_least": {"type": "input\_tokens", "value": 2000}

}

]

}

# Extended thinking config (required for clear\_thinking strategy)

THINKING = {

"type": "enabled",

"budget\_tokens": 1024 # Budget for thinking per turn

}

# Continue from previous session - memory persists!

print("=" \* 60)

print("📚 SESSION 3: Long review session with context clearing")

print("=" \* 60)

print()

# Clean up messages - remove any empty content from previous session

# This ensures we have a valid message state to continue from

cleaned\_messages = []

for msg in messages:

if isinstance(msg.get("content"), list):

# Filter out empty content blocks

content = [c for c in msg["content"] if c]

if content:

cleaned\_messages.append({"role": msg["role"], "content": content})

elif msg.get("content"):

cleaned\_messages.append(msg)

messages = cleaned\_messages

# Review 1: Data processor (larger file)

with open("memory\_demo/sample\_code/data\_processor\_v1.py", "r") as f:

data\_processor\_code = f.read()

messages.append({

"role": "user",

"content": f"Review this data processor:\n\n```python\n{data\_processor\_code}\n```"

})

print("📝 Review 1: Data processor")

response = run\_conversation\_turn(

client=client,

model=MODEL,

messages=messages,

memory\_handler=memory,

system="You are a code reviewer.",

context\_management=CONTEXT\_MANAGEMENT,

thinking=THINKING,

max\_tokens=4096,

verbose=True

)

# Add response to messages

messages.append({"role": "assistant", "content": response[1]})

if response[2]:

messages.append({"role": "user", "content": response[2]})

print(f" 📊 Input tokens: {response[0].usage.input\_tokens:,}")

context\_cleared, saved = print\_context\_management\_info(response[0])

print()

# Review 2: SQL code

with open("memory\_demo/sample\_code/sql\_query\_builder.py", "r") as f:

sql\_code = f.read()

messages.append({

"role": "user",

"content": f"Review this SQL query builder:\n\n```python\n{sql\_code}\n```"

})

print("📝 Review 2: SQL query builder")

response = run\_conversation\_turn(

client=client,

model=MODEL,

messages=messages,

memory\_handler=memory,

system="You are a code reviewer.",

context\_management=CONTEXT\_MANAGEMENT,

thinking=THINKING,

max\_tokens=4096,

verbose=True

)

messages.append({"role": "assistant", "content": response[1]})

if response[2]:

messages.append({"role": "user", "content": response[2]})

print(f" 📊 Input tokens: {response[0].usage.input\_tokens:,}")

context\_cleared, saved = print\_context\_management\_info(response[0])

print()

# Review 3: Add one more review to ensure we trigger clearing

with open("memory\_demo/sample\_code/web\_scraper\_v1.py", "r") as f:

scraper\_code = f.read()

messages.append({

"role": "user",

"content": f"Quick check - any issues here?\n\n```python\n{scraper\_code}\n```"

})

print("📝 Review 3: Web scraper (should trigger clearing)")

response = run\_conversation\_turn(

client=client,

model=MODEL,

messages=messages,

memory\_handler=memory,

system="You are a code reviewer.",

context\_management=CONTEXT\_MANAGEMENT,

thinking=THINKING,

max\_tokens=4096,

verbose=True

)

messages.append({"role": "assistant", "content": response[1]})

if response[2]:

messages.append({"role": "user", "content": response[2]})

print(f" 📊 Input tokens: {response[0].usage.input\_tokens:,}")

context\_cleared, saved = print\_context\_management\_info(response[0])

print()

print("=" \* 60)

print("✅ Session 3 complete!")

print("=" \* 60)

```
============================================================
📚 SESSION 3: Long review session with context clearing
============================================================

📝 Review 1: Data processor
🧠 Thinking: The user wants me to review a data processor with multiple concurrency and thread-safety issues. Let...
  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully
  📊 Input tokens: 6,611
  ℹ️  Context below threshold - no clearing triggered

📝 Review 2: SQL query builder
🧠 Thinking: The user is now asking me to review a SQL query builder with SQL injection vulnerabilities. This is ...
  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully
  📊 Input tokens: 7,923
  ✂️  Context editing triggered!
      • Cleared 1 thinking turn(s), saved 166 tokens
      • After clearing: 7,923 tokens

📝 Review 3: Web scraper (should trigger clearing)
🧠 Thinking: This is a quick check request for a web scraper with threading issues. Let me quickly identify the p...
  🔧 Memory tool: str_replace /memories/review.md
  ✓ Result: File /memories/review.md has been edited successfully
  📊 Input tokens: 9,052
  ✂️  Context editing triggered!
      • Cleared 2 thinking turn(s), saved 265 tokens
      • After clearing: 9,052 tokens

============================================================
✅ Session 3 complete!
============================================================
```

**What just happened?**

As context grew during multiple reviews with extended thinking enabled, context editing was applied:

1. **Thinking blocks cleared** - Old thinking from previous turns removed first
2. **Tool results cleared** - Old memory tool results removed when threshold exceeded
3. **Memory files intact** - Claude can still query learned patterns
4. **Token usage managed** - Saved tokens from both thinking and tool results

This demonstrates the key benefit:

* **Short-term memory** (conversation context + thinking) → Cleared to save space
* **Long-term memory** (stored patterns) → Persists across sessions

Let's verify memory survived the clearing:

# Verify memory persists after context clearing

import os

print("📂 Memory files in demo\_memory/:")

print()

for root, dirs, files in os.walk("./demo\_memory"):

# Calculate relative path for display

level = root.replace("./demo\_memory", "").count(os.sep)

indent = " " \* level

folder\_name = os.path.basename(root) or "demo\_memory"

print(f"{indent}{folder\_name}/")

sub\_indent = " " \* (level + 1)

for file in files:

file\_path = os.path.join(root, file)

size = os.path.getsize(file\_path)

print(f"{sub\_indent}├── {file} ({size} bytes)")

print()

print("✅ All learned patterns preserved despite context clearing!")

```
📂 Memory files in demo_memory/:

demo_memory/
  memories/
    ├── review.md (318 bytes)

✅ All learned patterns preserved despite context clearing!
```

##  4. How It Works

###  Memory Tool Architecture

The memory tool is **client-side** - you control the storage. Claude makes tool calls, your application executes them.

####  Memory Tool Commands

| Command | Description | Example |
| --- | --- | --- |
| `view` | Show directory or file contents | `{"command": "view", "path": "/memories"}` |
| `create` | Create or overwrite a file | `{"command": "create", "path": "/memories/notes.md", "file_text": "..."}` |
| `str_replace` | Replace text in a file | `{"command": "str_replace", "path": "...", "old_str": "...", "new_str": "..."}` |
| `insert` | Insert text at line number | `{"command": "insert", "path": "...", "insert_line": 2, "insert_text": "..."}` |
| `delete` | Delete a file or directory | `{"command": "delete", "path": "/memories/old.txt"}` |
| `rename` | Rename or move a file | `{"command": "rename", "old_path": "...", "new_path": "..."}` |

See `memory_tool.py` for the complete implementation with path validation and security measures.

###  Thinking Management (`clear_thinking_20251015`)

When using extended thinking, thinking blocks accumulate and consume tokens. The `clear_thinking` strategy manages these automatically.

**Important**: This strategy requires `thinking` to be enabled in your API call.

**API Call Pattern** (with extended thinking enabled):

response = client.beta.messages.create(

betas=["context-management-2025-06-27"], # Required beta flag

model="claude-sonnet-4-6",

messages=messages,

tools=[{"type": "memory\_20250818", "name": "memory"}],

thinking={"type": "enabled", "budget\_tokens": 10000}, # Enable thinking

context\_management={ # Context editing config

"edits": [

{

"type": "clear\_thinking\_20251015",

"keep": {"type": "thinking\_turns", "value": 1} # Keep last turn only

},

{

"type": "clear\_tool\_uses\_20250919",

"trigger": {"type": "input\_tokens", "value": 35000},

"keep": {"type": "tool\_uses", "value": 5}

}

]

},

max\_tokens=2048

)

**Key points:**

* `clear_thinking` must come **first** when combining strategies
* Requires extended thinking to be enabled (`thinking={"type": "enabled", ...}`)
* Use `"keep": "all"` to preserve all thinking blocks for maximum cache hits
* Trigger is optional for thinking (clears based on `keep` value)

###  Understanding the Demo Code

Key implementation details from `code_review_demo.py`:

class CodeReviewAssistant:

def \_\_init\_\_(self, memory\_storage\_path="./memory\_storage"):

self.client = Anthropic()

self.memory\_handler = MemoryToolHandler(base\_path=memory\_storage\_path)

self.messages = []

def review\_code(self, code, filename, description=""):

# 1. Add user message

self.messages.append({...})

# 2. Conversation loop with tool execution

while True:

response = self.client.beta.messages.create(

model=MODEL,

system=self.\_create\_system\_prompt(),

messages=self.messages,

tools=[{"type": "memory\_20250818", "name": "memory"}],

betas=["context-management-2025-06-27"],

context\_management=CONTEXT\_MANAGEMENT

)

# 3. Execute tool uses

tool\_results = []

for content in response.content:

if content.type == "tool\_use":

result = self.\_execute\_tool\_use(content)

tool\_results.append({...})

# 4. Continue if there are tool uses, otherwise done

if tool\_results:

self.messages.append({"role": "user", "content": tool\_results})

else:

break

**The key pattern**: Keep calling the API while there are tool uses, executing them and feeding results back.

###  What Claude Actually Learns

This is what makes memory powerful - **semantic pattern recognition**, not just syntax:

**Session 1: Thread-Based Web Scraper**

# Bug: Race condition

class WebScraper:

def \_\_init\_\_(self):

self.results = [] # Shared state!

def scrape\_urls(self, urls):

with ThreadPoolExecutor() as executor:

for future in as\_completed(futures):

self.results.append(future.result()) # RACE!

**What Claude Stores in Memory** (example file: `/memories/concurrency_patterns/thread_safety.md`):

When Claude encounters this pattern, it stores the following insights to its memory files:

* **Symptom**: Inconsistent results in concurrent operations
* **Cause**: Shared mutable state (lists/dicts) modified from multiple threads
* **Solution**: Use locks, thread-safe data structures, or return results instead
* **Red flags**: Instance variables in thread callbacks, unused locks, counter increments

---

**Session 2: Async API Client** (New conversation!)

Claude checks memory FIRST, finds the thread-safety pattern, then:

1. **Recognizes** similar pattern in async code (coroutines can interleave too)
2. **Applies** the solution immediately (no re-learning needed)
3. **Explains** with reference to stored knowledge

# Claude spots this immediately:

async def fetch\_all(self, endpoints):

for coro in asyncio.as\_completed(tasks):

self.responses.append(await coro) # Same pattern!

---

**Why This Matters:**

* ❌ **Syntax checkers** miss race conditions entirely
* ✅ **Claude learns** architectural patterns and applies them across contexts
* ✅ **Cross-language**: Pattern applies to Go, Java, Rust concurrency too
* ✅ **Gets better**: Each review adds to the knowledge base

###  Sample Code Files

The demo uses these sample files (all have concurrency/thread-safety bugs):

* `memory_demo/sample_code/web_scraper_v1.py` - Race condition: threads modifying shared state
* `memory_demo/sample_code/api_client_v1.py` - Similar concurrency bug in async context
* `memory_demo/sample_code/data_processor_v1.py` - Multiple concurrency issues for long session demo

Let's look at one:

**`memory_demo/sample_code/web_scraper_v1.py`**

"""

Concurrent web scraper with a race condition bug.

Multiple threads modify shared state without synchronization.

"""

import time

from concurrent.futures import ThreadPoolExecutor, as\_completed

from typing import List, Dict

import requests

class WebScraper:

"""Web scraper that fetches multiple URLs concurrently."""

def \_\_init\_\_(self, max\_workers: int = 10):

self.max\_workers = max\_workers

self.results = [] # BUG: Shared mutable state accessed by multiple threads!

self.failed\_urls = [] # BUG: Another race condition!

def fetch\_url(self, url: str) -> Dict[str, any]:

"""Fetch a single URL and return the result."""

try:

response = requests.get(url, timeout=5)

response.raise\_for\_status()

return {

"url": url,

"status": response.status\_code,

"content\_length": len(response.content),

}

except requests.exceptions.RequestException as e:

return {"url": url, "error": str(e)}

def scrape\_urls(self, urls: List[str]) -> List[Dict[str, any]]:

"""

Scrape multiple URLs concurrently.

BUG: self.results is accessed from multiple threads without locking!

This causes race conditions where results can be lost or corrupted.

"""

with ThreadPoolExecutor(max\_workers=self.max\_workers) as executor:

futures = [executor.submit(self.fetch\_url, url) for url in urls]

for future in as\_completed(futures):

result = future.result()

# RACE CONDITION: Multiple threads append to self.results simultaneously

if "error" in result:

self.failed\_urls.append(result["url"]) # RACE CONDITION

else:

self.results.append(result) # RACE CONDITION

return self.results

**Bug**: Multiple threads modify `self.results` and `self.failed_urls` without locking!

Claude will:

1. Identify the race conditions
2. Store the pattern in `/memories/concurrency_patterns/thread_safety.md`
3. Apply this concurrency pattern to async code in Session 2

###  Demo Overview

We've built a complete Code Review Assistant. The implementation is in `memory_demo/code_review_demo.py`.

**To run the interactive demo:**

python memory\_demo/code\_review\_demo.py

The demo demonstrates:

1. **Session 1**: Review Python code with a bug → Claude learns the pattern
2. **Session 2**: Review similar code (new conversation) → Claude applies the pattern
3. **Session 3**: Long review session → Context editing keeps it manageable

##  7. Best Practices & Security

###  Memory Management

**Do:**

* ✅ Store task-relevant patterns, not conversation history
* ✅ Organize with clear directory structure
* ✅ Use descriptive file names
* ✅ Periodically review and clean up memory

**Don't:**

* ❌ Store sensitive information (passwords, API keys, PII)
* ❌ Let memory grow unbounded
* ❌ Store everything indiscriminately

###  Security: Path Traversal Protection

**Critical**: Always validate paths to prevent directory traversal attacks. See `memory_tool.py` for implementation.

###  Security: Memory Poisoning

**⚠️ Critical Risk**: Memory files are read back into Claude's context, making them a potential vector for prompt injection.

**Mitigation strategies:**

1. **Content Sanitization**: Filter dangerous patterns before storing
2. **Memory Scope Isolation**: Per-user/per-project isolation
3. **Memory Auditing**: Log and scan all memory operations
4. **Prompt Engineering**: Instruct Claude to ignore instructions in memory

See `memory_tool.py` for complete security implementation and tests in `tests/`.

##  Conclusion

###  What You Accomplished

In this cookbook, you learned to:

* ✅ **Implement the memory tool** for cross-conversation learning (Sessions 1 & 2 showed pattern recognition persisting)
* ✅ **Configure context editing** with token triggers and retention policies (Session 3 demonstrated automatic clearing)
* ✅ **Apply security best practices** including path validation and memory poisoning prevention

###  Applying These Patterns

**For your projects:**

1. Start with a single memory file for patterns (e.g., `/memories/patterns.md`)
2. Set context editing triggers at 30-40k tokens for production use
3. Implement per-project memory isolation to prevent cross-contamination

**Other applications:**

* **Customer support**: Store user preferences and common issue resolutions
* **Research assistants**: Accumulate domain knowledge across sessions
* **Data analysis**: Remember dataset characteristics and successful techniques

###  Next Steps

* **Production deployment**: Use [claude-code-action(opens in new tab)](https://github.com/anthropics/claude-code-action) for GitHub PR reviews
* **Security hardening**: Review the memory poisoning mitigations in `memory_tool.py`
* **Extended thinking**: Explore thinking management for compute-intensive tasks

###  Resources

* [Memory tool documentation(opens in new tab)](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
* [Claude API reference(opens in new tab)](https://docs.claude.com/en/api/messages)
* [Support(opens in new tab)](https://support.claude.com)

Memory and context management are in **beta**. Share your feedback to help us improve!
