<!-- source: https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers -->

#  Orchestrator-Workers Workflow

##  Introduction

Have you ever needed multiple perspectives on the same task, but couldn't predict in advance which perspectives would be most valuable? The orchestrator-workers pattern solves this by having a central LLM analyze each unique task and dynamically determine the best subtasks to delegate to specialized worker LLMs.

Traditional approaches either require manual prompting multiple times or use hardcoded parallelization that generates the same variations regardless of context.

With this approach, an orchestrator LLM analyzes the task, determines which variations would be most valuable for this specific case, then delegates to worker LLMs that generate each variation.

###  What You'll Build

A system that takes a product description request and:

1. Analyzes what types of marketing copy would be valuable
2. Dynamically generates specialized task descriptions for workers
3. Produces multiple content variations optimized for different audiences
4. Returns coordinated results from all workers

###  Prerequisites

* Python 3.9 or higher
* Anthropic API key set as environment variable: `export ANTHROPIC_API_KEY='your-key'`
* Basic understanding of prompt engineering
* Familiarity with Python classes and type hints

###  When to use this workflow

This workflow is well-suited for complex tasks where you can't predict the subtasks needed in advance. The key difference from simple parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Use this pattern when:**

* Tasks require multiple distinct approaches or perspectives
* The optimal subtasks depend on the specific input
* You need to compare different strategies or styles

**Don't use this pattern when:**

* You have simple, single-output tasks (unnecessary complexity)
* Latency is critical (multiple LLM calls add overhead)
* Subtasks are predictable and can be pre-defined (use simpler parallelization)

##  How It Works

The orchestrator-workers pattern operates in two phases:

1. **Analysis & Planning Phase**: The orchestrator LLM receives the task and context, analyzes what approaches would be valuable, and generates structured subtask descriptions in XML format.
2. **Execution Phase**: Each worker LLM receives:

   * The original task for context
   * Its specific subtask type and description
   * Any additional context provided

The orchestrator decides *at runtime* what subtasks to create, making this more adaptive than pre-defined parallel workflows.

##  Setup

###  Installation



pip install anthropic

###  Helper Functions

This example uses helper functions from `util.py` for making LLM calls and parsing XML responses:

* `llm_call(prompt, system_prompt="", model="claude-sonnet-4-6")`: Sends a prompt to Claude and returns the text response
* `extract_xml(text, tag)`: Extracts content from XML tags using regex

These utilities handle API authentication (reading `ANTHROPIC_API_KEY` from environment) and provide a simple interface for the orchestrator-workers pattern. You can view the complete implementation in [util.py(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/util.py).

##  Implementation

The `FlexibleOrchestrator` class coordinates the two-phase workflow:

**Key design decisions:**

* Prompts are templates that accept runtime variables (`task`, `context`) for flexibility
* XML is used for structured output parsing (reliable and language-model-friendly format)
* Workers receive both the original task AND their specific instructions for better context
* Error handling validates that workers return non-empty responses

The implementation includes:

* `parse_tasks()`: Parses the orchestrator's XML output into structured task dictionaries
* `FlexibleOrchestrator.process()`: Main coordination logic that calls orchestrator, then workers
* Response validation to catch and handle empty worker outputs



from util import extract\_xml, llm\_call

# Model configuration

MODEL = "claude-sonnet-4-6" # Fast, capable model for both orchestrator and workers

def parse\_tasks(tasks\_xml: str) -> list[dict]:

"""Parse XML tasks into a list of task dictionaries."""

tasks = []

current\_task = {}

for line in tasks\_xml.split("\n"):

line = line.strip()

if not line:

continue

if line.startswith("<task>"):

current\_task = {}

elif line.startswith("<type>"):

current\_task["type"] = line[6:-7].strip()

elif line.startswith("<description>"):

current\_task["description"] = line[12:-13].strip()

elif line.startswith("</task>"):

if "description" in current\_task:

if "type" not in current\_task:

current\_task["type"] = "default"

tasks.append(current\_task)

return tasks

class FlexibleOrchestrator:

"""Break down tasks and run them in parallel using worker LLMs."""

def \_\_init\_\_(

self,

orchestrator\_prompt: str,

worker\_prompt: str,

model: str = MODEL,

):

"""Initialize with prompt templates and model selection."""

self.orchestrator\_prompt = orchestrator\_prompt

self.worker\_prompt = worker\_prompt

self.model = model

def \_format\_prompt(self, template: str, \*\*kwargs) -> str:

"""Format a prompt template with variables."""

try:

return template.format(\*\*kwargs)

except KeyError as e:

raise ValueError(f"Missing required prompt variable: {e}") from e

def process(self, task: str, context: dict | None = None) -> dict:

"""Process task by breaking it down and running subtasks in parallel."""

context = context or {}

# Step 1: Get orchestrator response

orchestrator\_input = self.\_format\_prompt(self.orchestrator\_prompt, task=task, \*\*context)

orchestrator\_response = llm\_call(orchestrator\_input, model=self.model)

# Parse orchestrator response

analysis = extract\_xml(orchestrator\_response, "analysis")

tasks\_xml = extract\_xml(orchestrator\_response, "tasks")

tasks = parse\_tasks(tasks\_xml)

print("\n" + "=" \* 80)

print("ORCHESTRATOR ANALYSIS")

print("=" \* 80)

print(f"\n{analysis}\n")

print("\n" + "=" \* 80)

print(f"IDENTIFIED {len(tasks)} APPROACHES")

print("=" \* 80)

for i, task\_info in enumerate(tasks, 1):

print(f"\n{i}. {task\_info['type'].upper()}")

print(f" {task\_info['description']}")

print("\n" + "=" \* 80)

print("GENERATING CONTENT")

print("=" \* 80 + "\n")

# Step 2: Process each task

worker\_results = []

for i, task\_info in enumerate(tasks, 1):

print(f"[{i}/{len(tasks)}] Processing: {task\_info['type']}...")

worker\_input = self.\_format\_prompt(

self.worker\_prompt,

original\_task=task,

task\_type=task\_info["type"],

task\_description=task\_info["description"],

\*\*context,

)

worker\_response = llm\_call(worker\_input, model=self.model)

worker\_content = extract\_xml(worker\_response, "response")

# Validate worker response - handle empty outputs

if not worker\_content or not worker\_content.strip():

print(f"⚠️ Warning: Worker '{task\_info['type']}' returned no content")

worker\_content = f"[Error: Worker '{task\_info['type']}' failed to generate content]"

worker\_results.append(

{

"type": task\_info["type"],

"description": task\_info["description"],

"result": worker\_content,

}

)

# Display results

print("\n" + "=" \* 80)

print("RESULTS")

print("=" \* 80)

for i, result in enumerate(worker\_results, 1):

print(f"\n{'-' \* 80}")

print(f"Approach {i}: {result['type'].upper()}")

print(f"{'-' \* 80}")

print(f"\n{result['result']}\n")

return {

"analysis": analysis,

"worker\_results": worker\_results,

}

##  Example Use Case: Marketing Variation Generation

Now let's see the orchestrator-workers pattern in action with a practical example: generating multiple styles of marketing copy for a product.

**Why this example demonstrates the pattern well:**

* Different products benefit from different marketing angles
* The "best" variations depend on the specific product features and target audience
* The orchestrator can adapt its strategy based on the input rather than using a fixed template

**Prompt design notes:**

* The orchestrator prompt asks for 2-3 approaches and provides XML structure guidance
* The worker prompt gives workers full context (original task, their style, and guidelines)
* Both prompts use clear XML formatting to ensure reliable parsing



ORCHESTRATOR\_PROMPT = """

Analyze this task and break it down into 2-3 distinct approaches:

Task: {task}

Return your response in this format:

<analysis>

Explain your understanding of the task and which variations would be valuable.

Focus on how each approach serves different aspects of the task.

</analysis>

<tasks>

<task>

<type>formal</type>

<description>Write a precise, technical version that emphasizes specifications</description>

</task>

<task>

<type>conversational</type>

<description>Write an engaging, friendly version that connects with readers</description>

</task>

</tasks>

"""

WORKER\_PROMPT = """

Generate content based on:

Task: {original\_task}

Style: {task\_type}

Guidelines: {task\_description}

Return your response in this format:

<response>

Your content here, maintaining the specified style and fully addressing requirements.

</response>

"""

orchestrator = FlexibleOrchestrator(

orchestrator\_prompt=ORCHESTRATOR\_PROMPT,

worker\_prompt=WORKER\_PROMPT,

)

results = orchestrator.process(

task="Write a product description for a new eco-friendly water bottle",

context={

"target\_audience": "environmentally conscious millennials",

"key\_features": ["plastic-free", "insulated", "lifetime warranty"],

},

)



```
================================================================================
ORCHESTRATOR ANALYSIS
================================================================================

This task requires creating marketing copy for an eco-friendly water bottle. The core challenge is balancing product information with persuasive messaging while highlighting the environmental benefits. Different approaches would serve distinct marketing channels and audience segments:

1. A **feature-focused technical approach** would appeal to detail-oriented consumers who make purchasing decisions based on specifications, materials, and measurable environmental impact. This serves e-commerce listings and comparison shopping.

2. A **lifestyle-oriented emotional approach** would connect with values-driven consumers through storytelling and aspirational messaging, emphasizing how the product fits into an eco-conscious lifestyle. This serves social media and brand-building content.

3. A **benefit-driven practical approach** would focus on solving everyday problems while weaving in sustainability advantages, appealing to mainstream consumers who want both functionality and environmental responsibility. This serves broad retail contexts.

Each approach addresses the "eco-friendly" aspect differently—through data, values, or practical advantages—making them valuable for different marketing contexts.

================================================================================
IDENTIFIED 3 APPROACHES
================================================================================

1. TECHNICAL-SPECIFICATIONS
   >Write a detailed, feature-focused description emphasizing materials, construction, environmental certifications, and measurable sustainability metrics (recyclability percentages, carbon footprint reduction, etc.)<

2. LIFESTYLE-EMOTIONAL
   >Write an inspirational, story-driven description that connects the product to environmental values, personal identity, and the broader movement toward sustainable living<

3. BENEFIT-PRACTICAL
   >Write a problem-solution focused description highlighting everyday usability benefits (temperature retention, durability, convenience) while naturally integrating eco-friendly advantages<

================================================================================
GENERATING CONTENT
================================================================================

[1/3] Processing: technical-specifications...
[2/3] Processing: lifestyle-emotional...
[3/3] Processing: benefit-practical...

================================================================================
RESULTS
================================================================================

--------------------------------------------------------------------------------
Approach 1: TECHNICAL-SPECIFICATIONS
--------------------------------------------------------------------------------

# EcoFlow Pro™ Insulated Water Bottle - Technical Specifications

## Product Overview
Model: EF-750-INS | Capacity: 750ml (25.4 fl oz) | Weight: 285g ±5g

## Material Composition & Construction

### Primary Body
- **Material**: 18/8 (304) food-grade stainless steel
- **Wall Thickness**: 0.6mm inner wall, 0.5mm outer wall
- **Surface Treatment**: Powder-coated finish using water-based, VOC-free coating
- **BPA/BPS/Phthalate Status**: Certified free of all endocrine-disrupting compounds

### Insulation System
- **Technology**: Double-wall vacuum insulation with copper lining
- **Vacuum Pressure**: <0.001 Pa
- **Thermal Performance**:
  - Cold retention: 24 hours (maintains <10°C)
  - Hot retention: 12 hours (maintains >65°C)
- **Condensation**: Zero external condensation at all temperatures

### Cap & Seal Assembly
- **Cap Material**: 100% post-consumer recycled polypropylene (rPP)
- **Seal Gasket**: Medical-grade silicone (FDA 21 CFR 177.2600 compliant)
- **Thread Design**: 3.5-turn precision threading for leak-proof seal (tested to 50 PSI)

## Environmental Certifications & Standards

- **ISO 14001**: Environmental Management System certified manufacturing facility
- **Cradle to Cradle Certified®**: Silver level
- **Carbon Neutral Certified**: Through verified offset programs (Climate Neutral Certified)
- **NSF/ANSI 61**: Drinking water system components certification
- **REACH Compliant**: European chemical safety regulation adherent

## Sustainability Metrics

### Carbon Footprint
- **Manufacturing Emissions**: 2.8 kg CO₂e per unit (68% reduction vs. industry average of 8.7 kg CO₂e)
- **Transportation Impact**: Optimized packaging reduces shipping emissions by 42%
- **Lifecycle Offset**: Replaces approximately 217 single-use plastic bottles annually (based on average daily consumption)
- **Net Carbon Savings**: 156 kg CO₂e per year of use vs. disposable bottle equivalent

### Recyclability & Circularity
- **End-of-Life Recyclability**: 95% by weight
- **Stainless Steel**: 100% infinitely recyclable without quality degradation
- **Plastic Components**: 89% recyclable (rPP cap and silicone gasket)
- **Disassembly Time**: <45 seconds for complete material separation
- **Take-Back Program**: Available for responsible recycling through manufacturer

### Resource Efficiency
- **Recycled Content**: 73% post-consumer recycled materials by weight
- **Water Usage in Production**: 4.2L per unit (industry average: 12.8L)
- **Energy Consumption**: 18.5 MJ per unit manufactured using 100% renewable energy
- **Packaging**: 100% recycled cardboard, soy-based inks, zero plastic components

## Durability & Longevity Specifications

- **Impact Resistance**: Survives 2-meter drop test onto concrete (maintains vacuum seal)
- **Corrosion Resistance**: 1,000+ hour salt spray test (ASTM B117)
- **Cycle Testing**: 10,000+ open/close cycles without seal degradation
- **Warranty Period**: Lifetime warranty against manufacturing defects
- **Expected Lifespan**: 15+ years under normal use conditions

## Physical Specifications

- **Dimensions**: Height: 265mm | Diameter: 73mm (body), 48mm (cap)
- **Mouth Opening**: 42mm wide-mouth design (ice cube compatible)
- **Base Diameter**: 68mm (fits standard cup holders)
- **Volume Markings**: Laser-etched ml/oz graduations (50ml increments)
- **Color Options**: 8 powder-coated finishes (all VOC-free)

## Compliance & Safety Testing

- **FDA Approved**: All food-contact materials
- **LFGB Certified**: German food safety standards
- **Proposition 65**: Compliant (no listed chemicals)
- **Lead Content**: <0.01 ppm (non-detectable)
- **Microplastic Shedding**: Zero detected in 90-day leaching study

## Performance Advantages

- **Single-Use Bottle Replacement Rate**: 1:217 annually
- **Cost Recovery Period**: 2.3 months (vs. purchasing disposable bottles)
- **Plastic Waste Prevention**: 1.89 kg per year per user
- **Water Quality Preservation**: No taste transfer, maintains pH neutrality (±0.1)

## Manufacturing & Supply Chain

- **Production Facility**: Solar-powered, zero-waste-to-landfill certified plant
- **Supply Chain Transparency**: Full material traceability via blockchain verification
- **Fair Trade Certified**: Ethical labor practices throughout supply chain
- **Local Sourcing**: 67% of materials sourced within 500km of manufacturing facility

--------------------------------------------------------------------------------
Approach 2: LIFESTYLE-EMOTIONAL
--------------------------------------------------------------------------------

**More Than Hydration. A Daily Ritual of Change.**

Every morning, you make a choice. Not just about what you drink, but about who you are and the world you're creating.

This isn't just a water bottle—it's your companion in a quiet revolution. Crafted from 100% recycled ocean-bound plastic, each bottle tells a story of transformation: waste that once threatened our seas, now reimagined as something beautiful, functional, and enduring in your hands.

Feel the smooth, cool surface against your palm. Notice its weight—substantial enough to remind you it's built to last decades, not days. This is the bottle that replaces hundreds of single-use plastics, the one that travels with you through morning commutes, mountain trails, and late-night creative sessions. It becomes part of your story, collecting scratches and memories like badges of honor.

But here's what really matters: You're not alone in this. You're joining millions who understand that sustainability isn't about perfection—it's about progress. Every refill is a small act of defiance against throwaway culture. Every sip connects you to a global community choosing differently, living intentionally, proving that our daily choices ripple outward in ways we can't always see but can always feel.

Your hydration. Your values. Your legacy.

Because the future isn't something that happens to us—it's something we carry with us, one conscious choice at a time.

**Welcome to the movement. Welcome home.**

--------------------------------------------------------------------------------
Approach 3: BENEFIT-PRACTICAL
--------------------------------------------------------------------------------

**Stay Hydrated All Day with the EcoFlow Bottle – Built for Your Active Life**

Tired of lukewarm coffee by mid-morning or water that tastes like plastic after a few months? The EcoFlow Bottle solves the everyday frustrations that come with typical water bottles while helping you make a positive environmental impact.

**Keeps Drinks at the Perfect Temperature**
Double-wall vacuum insulation maintains cold drinks icy for 24 hours and hot beverages steaming for 12 hours. Your morning coffee stays hot through your commute, and your water remains refreshingly cold during afternoon meetings or workouts.

**Built to Last Through Daily Wear and Tear**
Constructed from premium 18/8 stainless steel with a powder-coated finish, this bottle withstands drops, bumps, and the chaos of daily life. The leak-proof lid means you can toss it in your bag without worry—no more soggy papers or ruined electronics.

**Designed for Real Convenience**
The wide mouth opening fits ice cubes easily and makes cleaning simple (no hard-to-reach corners). It fits standard cup holders in your car, and the ergonomic design is comfortable to carry whether you're commuting, hiking, or running errands.

**Better for Your Wallet and the Planet**
By switching to a reusable bottle, you'll save hundreds of dollars annually on disposable bottles while eliminating plastic waste. The durable construction means you're buying one bottle that lasts for years, not replacing cheap alternatives every few months. Plus, you'll avoid the chemicals found in many plastic bottles, ensuring cleaner-tasting water every time.

**Your Reliable Hydration Companion**
The EcoFlow Bottle adapts to your lifestyle—whether you need hot tea for early mornings, cold water for the gym, or room-temperature drinks throughout the workday. It's the practical solution that makes staying hydrated effortless while naturally reducing your environmental footprint.
```

##  Summary

You've now implemented an orchestrator-workers pattern that dynamically adapts its task breakdown based on the specific input. This pattern generated multiple marketing copy variations—each tailored to different audiences and contexts—without requiring you to pre-define what those variations should be.

###  Key Takeaways

**Pattern benefits:**

* **Adaptability**: The orchestrator determines the best approach for each unique input
* **Flexibility**: Easy to apply to different domains by changing the prompts
* **Structured coordination**: XML-based communication ensures reliable parsing
* **Error resilience**: Validation catches and handles worker failures

**When this pattern excels:**

* Content generation requiring multiple perspectives (marketing, documentation, creative writing)
* Analysis tasks benefiting from different analytical lenses
* Problem-solving where the decomposition strategy depends on the problem

###  Limitations & Considerations

**Cost & Latency:**

* Requires N+1 LLM calls (1 orchestrator + N workers)
* Sequential processing in this implementation (workers run one at a time)
* For better performance, consider parallelizing worker calls with `asyncio` or thread pools

**When NOT to use this pattern:**

* Simple tasks with single, clear outputs (the added complexity isn't justified)
* Latency-critical applications (multiple API calls add overhead)
* Tasks where subtasks are always the same (use pre-defined parallelization instead)

**Failure modes to consider:**

* Orchestrator might not break down tasks optimally (prompt engineering is critical)
* Workers may return empty or malformed responses (we handle this with validation)
* XML parsing can fail if models don't follow format exactly (consider using JSON as an alternative)

###  Next Steps

**Enhance this implementation:**

1. Add parallel worker execution using `asyncio` for better performance
2. Implement retry logic for failed workers
3. Add a synthesis phase where an LLM combines worker outputs
4. Experiment with different orchestrator strategies (e.g., asking for more/fewer subtasks)

**Adapt to your use case:**

* Modify the orchestrator prompt to guide task decomposition for your domain
* Adjust worker prompts to provide domain-specific instructions
* Add context parameters relevant to your application
* Consider using Claude Opus for the orchestrator and Claude Haiku for workers to optimize cost vs. quality
