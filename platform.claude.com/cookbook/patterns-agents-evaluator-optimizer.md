<!-- source: https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer -->

##  Evaluator-Optimizer Workflow

In this workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

###  When to use this workflow

This workflow is particularly effective when we have:

* Clear evaluation criteria
* Value from iterative refinement

The two signs of good fit are:

* LLM responses can be demonstrably improved when feedback is provided
* The LLM can provide meaningful feedback itself

from util import extract\_xml, llm\_call

def generate(prompt: str, task: str, context: str = "") -> tuple[str, str]:

"""Generate and improve a solution based on feedback."""

full\_prompt = f"{prompt}\n{context}\nTask: {task}" if context else f"{prompt}\nTask: {task}"

response = llm\_call(full\_prompt)

thoughts = extract\_xml(response, "thoughts")

result = extract\_xml(response, "response")

print("\n=== GENERATION START ===")

print(f"Thoughts:\n{thoughts}\n")

print(f"Generated:\n{result}")

print("=== GENERATION END ===\n")

return thoughts, result

def evaluate(prompt: str, content: str, task: str) -> tuple[str, str]:

"""Evaluate if a solution meets requirements."""

full\_prompt = f"{prompt}\nOriginal task: {task}\nContent to evaluate: {content}"

response = llm\_call(full\_prompt)

evaluation = extract\_xml(response, "evaluation")

feedback = extract\_xml(response, "feedback")

print("=== EVALUATION START ===")

print(f"Status: {evaluation}")

print(f"Feedback: {feedback}")

print("=== EVALUATION END ===\n")

return evaluation, feedback

def loop(task: str, evaluator\_prompt: str, generator\_prompt: str) -> tuple[str, list[dict]]:

"""Keep generating and evaluating until requirements are met."""

memory = []

chain\_of\_thought = []

thoughts, result = generate(generator\_prompt, task)

memory.append(result)

chain\_of\_thought.append({"thoughts": thoughts, "result": result})

while True:

evaluation, feedback = evaluate(evaluator\_prompt, result, task)

if evaluation == "PASS":

return result, chain\_of\_thought

context = "\n".join(

["Previous attempts:", \*[f"- {m}" for m in memory], f"\nFeedback: {feedback}"]

)

thoughts, result = generate(generator\_prompt, task, context)

memory.append(result)

chain\_of\_thought.append({"thoughts": thoughts, "result": result})

###  Example Use Case: Iterative coding loop

evaluator\_prompt = """

Evaluate this following code implementation for:

1. code correctness

2. time complexity

3. style and best practices

You should be evaluating only and not attemping to solve the task.

Only output "PASS" if all criteria are met and you have no further suggestions for improvements.

Output your evaluation concisely in the following format.

<evaluation>PASS, NEEDS\_IMPROVEMENT, or FAIL</evaluation>

<feedback>

What needs improvement and why.

</feedback>

"""

generator\_prompt = """

Your goal is to complete the task based on <user input>. If there are feedback

from your previous generations, you should reflect on them to improve your solution

Output your answer concisely in the following format:

<thoughts>

[Your understanding of the task and feedback and how you plan to improve]

</thoughts>

<response>

[Your code implementation here]

</response>

"""

task = """

<user input>

Implement a Stack with:

1. push(x)

2. pop()

3. getMin()

All operations should be O(1).

</user input>

"""

loop(task, evaluator\_prompt, generator\_prompt)

```
=== GENERATION START ===
Thoughts:

The task requires implementing a Stack with constant time operations including finding minimum.
To achieve O(1) for getMin(), we need to maintain a second stack that keeps track of minimums.
Each time we push, if the value is smaller than current min, we add it to minStack.
When we pop, if the popped value equals current min, we also pop from minStack.

Generated:

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def getMin(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1]
```

=== GENERATION END ===

=== EVALUATION START ===
Status: NEEDS_IMPROVEMENT
Feedback:
While the implementation is generally correct and achieves O(1) time complexity for all operations, there are several areas for improvement:

1. Error Handling:
- pop() should raise an exception when stack is empty rather than silently returning
- getMin() should raise an exception when stack is empty rather than returning None
- These behaviors should be consistent with standard stack implementations

2. Type Hints:
- Return type hint for pop() should be None or void
- Missing type hints for class variables stack and minStack

3. Documentation:
- Missing docstrings for class and methods
- Missing parameter descriptions

4. Edge Cases:
- No explicit handling of invalid input types for push()

The core algorithm is correct and efficient, but the implementation could be more robust and better documented for production use.

=== EVALUATION END ===

=== GENERATION START ===
Thoughts:

Based on the feedback, I'll improve the implementation by:
1. Adding proper error handling with exceptions
2. Including type hints and docstrings
3. Adding input validation
4. Maintaining O(1) time complexity for all operations

Generated:

```python
from typing import List

class MinStack:
    """A stack that supports push, pop, and getting minimum element in O(1) time."""

    def __init__(self):
        """Initialize empty stack with two internal lists."""
        self.stack: List[int] = []
        self.minStack: List[int] = []

    def push(self, x: int) -> None:
        """
        Push element onto stack and update minimum stack.

        Args:
            x: Integer to push onto stack

        Raises:
            TypeError: If x is not an integer
        """
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")

        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        """
        Remove and return top element from stack.

        Raises:
            IndexError: If stack is empty
        """
        if not self.stack:
            raise IndexError("Cannot pop from empty stack")

        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def getMin(self) -> int:
        """
        Get minimum element in stack.

        Returns:
            int: Minimum element in stack

        Raises:
            IndexError: If stack is empty
        """
        if not self.minStack:
            raise IndexError("Cannot get minimum from empty stack")
        return self.minStack[-1]
```

=== GENERATION END ===
```
