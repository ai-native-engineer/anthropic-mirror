<!-- source: https://platform.claude.com/cookbook/skills-notebooks-03-skills-custom-development -->

#  Building Custom Skills for Claude

Learn how to create, deploy, and manage custom skills to extend Claude's capabilities with your organization's specialized knowledge and workflows.

##  Table of Contents

1. [Introduction & Setup](#introduction)
2. [Understanding Custom Skills Architecture](#architecture)
3. [Example 1: Financial Ratio Calculator](#financial-ratio)
4. [Example 2: Company Brand Guidelines](#brand-guidelines)
5. [Example 3: Financial Modeling Suite](#financial-modeling)
6. [Skill Management & Versioning](#management)
7. [Best Practices & Production Tips](#best-practices)
8. [Troubleshooting](#troubleshooting)

##  1. Introduction & Setup

###  What are Custom Skills?

**Custom skills** are specialized expertise packages you create to teach Claude your organization's unique workflows, domain knowledge, and best practices. Unlike Anthropic's pre-built skills (Excel, PowerPoint, PDF), custom skills allow you to:

* **Codify organizational knowledge** - Capture your team's specific methodologies
* **Ensure consistency** - Apply the same standards across all interactions
* **Automate complex workflows** - Chain together multi-step processes
* **Maintain intellectual property** - Keep proprietary methods secure

###  Key Benefits

| Benefit | Description |
| --- | --- |
| **Expertise at Scale** | Deploy specialized knowledge to every Claude interaction |
| **Version Control** | Track changes and roll back if needed |
| **Composability** | Combine multiple skills for complex tasks |
| **Privacy** | Your skills remain private to your organization |

###  Prerequisites

Before starting, ensure you have:

* Completed [Notebook 1: Introduction to Skills(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/skills/notebooks/01_skills_introduction.ipynb)
* An Anthropic API key with Skills beta access
* Python environment with the local SDK installed

###  Environment Setup

Let's set up our environment and import necessary libraries:



import os

import sys

from pathlib import Path

from typing import Any

# Add parent directory for imports

sys.path.insert(0, str(Path.cwd().parent))

from anthropic import Anthropic

from anthropic.lib import files\_from\_dir

from dotenv import load\_dotenv

# Import our utilities

from file\_utils import (

download\_all\_files,

extract\_file\_ids,

print\_download\_summary,

)

# We'll create skill\_utils later in this notebook

# from skill\_utils import (

# create\_skill,

# list\_skills,

# delete\_skill,

# test\_skill

# )

# Load environment variables

load\_dotenv(Path.cwd().parent / ".env")

API\_KEY = os.getenv("ANTHROPIC\_API\_KEY")

MODEL = os.getenv("ANTHROPIC\_MODEL", "claude-sonnet-4-6")

if not API\_KEY:

raise ValueError(

"ANTHROPIC\_API\_KEY not found. Copy ../.env.example to ../.env and add your API key."

)

# Initialize client with Skills beta

client = Anthropic(api\_key=API\_KEY, default\_headers={"anthropic-beta": "skills-2025-10-02"})

# Setup directories

SKILLS\_DIR = Path.cwd().parent / "custom\_skills"

OUTPUT\_DIR = Path.cwd().parent / "outputs"

OUTPUT\_DIR.mkdir(exist\_ok=True)

print("✓ API key loaded")

print(f"✓ Using model: {MODEL}")

print(f"✓ Custom skills directory: {SKILLS\_DIR}")

print(f"✓ Output directory: {OUTPUT\_DIR}")

print("\n📝 Skills beta header configured for skill management")

##  2. Understanding Custom Skills Architecture

###  Skill Structure

Every custom skill follows this directory structure:



skill\_name/

├── SKILL.md # REQUIRED: Instructions with YAML frontmatter

├── \*.md # Optional: Any additional .md files (documentation, guides)

├── scripts/ # Optional: Executable code

│ ├── process.py

│ └── utils.js

└── resources/ # Optional: Templates, data files

└── template.xlsx

**Important:**

* **SKILL.md is the ONLY required file** - everything else is optional
* **Multiple .md files allowed** - You can have any number of markdown files in the top-level folder
* **All .md files are loaded** - Not just SKILL.md and REFERENCE.md, but any .md file you include
* **Organize as needed** - Use multiple .md files to structure complex documentation

📖 Read our engineering blog post on [Equipping agents for the real world with Skills(opens in new tab)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

###  Skills Are Not Just Markdown

![Skills Can Include Scripts and Files](https://platform.claude.com/cookbook/images/notebooks/skills-notebooks-03-skills-custom-development/not-just-markdown.png)

Skills can bundle various file types:

* **Markdown files**: Instructions and documentation (SKILL.md, REFERENCE.md, etc.)
* **Scripts**: Python, JavaScript, or other executable code for complex operations
* **Templates**: Pre-built files that can be customized (Excel templates, document templates)
* **Resources**: Supporting data files, configuration, or assets

###  SKILL.md Requirements

The `SKILL.md` file must include:

1. **YAML Frontmatter** (name: 64 chars, description: 1024 chars)

   * `name`: Lowercase alphanumeric with hyphens (required)
   * `description`: Brief description of what the skill does (required)
2. **Instructions** (markdown format)

   * Clear guidance for Claude
   * Examples of usage
   * Any constraints or rules
   * Recommended: Keep under 5,000 tokens

###  Additional Documentation Files

You can include multiple markdown files for better organization:



skill\_name/

├── SKILL.md # Main instructions (required)

├── REFERENCE.md # API reference (optional)

├── EXAMPLES.md # Usage examples (optional)

├── TROUBLESHOOTING.md # Common issues (optional)

└── CHANGELOG.md # Version history (optional)

All `.md` files in the root directory will be available to Claude when the skill is loaded.

###  Bundled Files Example

![Bundled Files in Skills](https://platform.claude.com/cookbook/images/notebooks/skills-notebooks-03-skills-custom-development/skills-bundled-files.png)

This example shows how Skills can bundle multiple files:

* **SKILL.md**: Contains the main instructions with colors, typography, and sections
* **slide-decks.md**: Additional documentation for specific use cases
* **Scripts and resources**: Can be referenced and used during skill execution

###  Progressive Disclosure

Skills load in three stages to optimize token usage:

| Stage | Content | Token Cost | When Loaded |
| --- | --- | --- | --- |
| **1. Metadata** | Name & description | name: 64 chars, description: 1024 chars | Always visible |
| **2. Instructions** | All .md files | <5,000 tokens recommended | When relevant |
| **3. Resources** | Scripts & files | As needed | During execution |

###  API Workflow



# 1. Create skill

skill = client.beta.skills.create(

display\_title="My Skill",

files=files\_from\_dir("path/to/skill")

)

# 2. Use in messages

response = client.beta.messages.create(

container={

"skills": [{

"type": "custom",

"skill\_id": skill.id,

"version": "latest"

}]

},

# ... rest of message parameters

)

###  Best Practices

For detailed guidance on skill creation and best practices, see:

* [Claude Skills Best Practices(opens in new tab)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
* [Skills Documentation(opens in new tab)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

###  Create Skill Utility Functions

Let's create helper functions for skill management:



def create\_skill(client: Anthropic, skill\_path: str, display\_title: str) -> dict[str, Any]:

"""

Create a new custom skill from a directory.

Args:

client: Anthropic client instance

skill\_path: Path to skill directory

display\_title: Human-readable skill name

Returns:

Dictionary with skill\_id, version, and metadata

"""

try:

# Create skill using files\_from\_dir

skill = client.beta.skills.create(

display\_title=display\_title, files=files\_from\_dir(skill\_path)

)

return {

"success": True,

"skill\_id": skill.id,

"display\_title": skill.display\_title,

"latest\_version": skill.latest\_version,

"created\_at": skill.created\_at,

"source": skill.source,

}

except Exception as e:

return {"success": False, "error": str(e)}

def list\_custom\_skills(client: Anthropic) -> list[dict[str, Any]]:

"""

List all custom skills in the workspace.

Returns:

List of skill dictionaries

"""

try:

skills\_response = client.beta.skills.list(source="custom")

skills = []

for skill in skills\_response.data:

skills.append(

{

"skill\_id": skill.id,

"display\_title": skill.display\_title,

"latest\_version": skill.latest\_version,

"created\_at": skill.created\_at,

"updated\_at": skill.updated\_at,

}

)

return skills

except Exception as e:

print(f"Error listing skills: {e}")

return []

def delete\_skill(client: Anthropic, skill\_id: str) -> bool:

"""

Delete a custom skill and all its versions.

Args:

client: Anthropic client

skill\_id: ID of skill to delete

Returns:

True if successful, False otherwise

"""

try:

# First delete all versions

versions = client.beta.skills.versions.list(skill\_id=skill\_id)

for version in versions.data:

client.beta.skills.versions.delete(skill\_id=skill\_id, version=version.version)

# Then delete the skill itself

client.beta.skills.delete(skill\_id)

return True

except Exception as e:

print(f"Error deleting skill: {e}")

return False

def test\_skill(

client: Anthropic,

skill\_id: str,

test\_prompt: str,

model: str = "claude-sonnet-4-6",

) -> Any:

"""

Test a custom skill with a prompt.

Args:

client: Anthropic client

skill\_id: ID of skill to test

test\_prompt: Prompt to test the skill

model: Model to use for testing

Returns:

Response from Claude

"""

response = client.beta.messages.create(

model=model,

max\_tokens=4096,

container={"skills": [{"type": "custom", "skill\_id": skill\_id, "version": "latest"}]},

tools=[{"type": "code\_execution\_20250825", "name": "code\_execution"}],

messages=[{"role": "user", "content": test\_prompt}],

betas=[

"code-execution-2025-08-25",

"files-api-2025-04-14",

"skills-2025-10-02",

],

)

return response

print("✓ Skill utility functions defined")

print(" - create\_skill()")

print(" - list\_custom\_skills()")

print(" - delete\_skill()")

print(" - test\_skill()")

###  Check Existing Custom Skills

Let's see if any custom skills already exist in your workspace:

###  ⚠️ Important: Clean Up Existing Skills Before Starting

If you're re-running this notebook, you may have skills from a previous session. Skills cannot have duplicate display titles, so you have three options:

1. **Delete existing skills** (recommended for testing) - Clean slate approach
2. **Use different display titles** - Add timestamps or version numbers to names
3. **Update existing skills with new versions** - See [Skill Management & Versioning](#management) section

Let's check for and optionally clean up existing skills:



# Check for existing skills that might conflict

existing\_skills = list\_custom\_skills(client)

skill\_titles\_to\_create = [

"Financial Ratio Analyzer",

"Corporate Brand Guidelines",

"Financial Modeling Suite",

]

conflicting\_skills = []

if existing\_skills:

print(f"Found {len(existing\_skills)} existing custom skill(s):")

for skill in existing\_skills:

print(f" - {skill['display\_title']} (ID: {skill['skill\_id']})")

if skill["display\_title"] in skill\_titles\_to\_create:

conflicting\_skills.append(skill)

if conflicting\_skills:

print(

f"\n⚠️ Found {len(conflicting\_skills)} skill(s) that will conflict with this notebook:"

)

for skill in conflicting\_skills:

print(f" - {skill['display\_title']} (ID: {skill['skill\_id']})")

print("\n" + "=" \* 70)

print("To clean up these skills and start fresh, uncomment and run:")

print("=" \* 70)

print("\n# UNCOMMENT THE LINES BELOW TO DELETE CONFLICTING SKILLS:")

print("# for skill in conflicting\_skills:")

print("# if delete\_skill(client, skill['skill\_id']):")

print("# print(f\"✅ Deleted: {skill['display\_title']}\")")

print("# else:")

print("# print(f\"❌ Failed to delete: {skill['display\_title']}\")")

# for skill in conflicting\_skills:

# if delete\_skill(client, skill['skill\_id']):

# print(f"✅ Deleted: {skill['display\_title']}")

# else:

# print(f"❌ Failed to delete: {skill['display\_title']}")

else:

print("\n✅ No conflicting skills found. Ready to proceed!")

else:

print("✅ No existing custom skills found. Ready to create new ones!")

##  3. Example 1: Financial Ratio Calculator

Let's create our first custom skill - a financial ratio calculator that can analyze company financial health.

###  Skill Overview

The **Financial Ratio Calculator** skill will:

* Calculate key financial ratios (ROE, P/E, Current Ratio, etc.)
* Interpret ratios with industry context
* Generate formatted reports
* Work with various data formats (CSV, JSON, text)

###  Upload the Financial Analyzer Skill

Now let's upload our financial analyzer skill to Claude:



# Upload the Financial Analyzer skill

financial\_skill\_path = SKILLS\_DIR / "analyzing-financial-statements"

if financial\_skill\_path.exists():

print("Uploading Financial Analyzer skill...")

result = create\_skill(client, str(financial\_skill\_path), "Financial Ratio Analyzer")

if result["success"]:

financial\_skill\_id = result["skill\_id"]

print("✅ Skill uploaded successfully!")

print(f" Skill ID: {financial\_skill\_id}")

print(f" Version: {result['latest\_version']}")

print(f" Created: {result['created\_at']}")

else:

print(f"❌ Upload failed: {result['error']}")

if "cannot reuse an existing display\_title" in str(result["error"]):

print("\n💡 Solution: A skill with this name already exists.")

print(" Run the 'Clean Up Existing Skills' cell above to delete it first,")

print(" or change the display\_title to something unique.")

else:

print(f"⚠️ Skill directory not found: {financial\_skill\_path}")

print(

"Please ensure the custom\_skills directory contains the analyzing-financial-statements folder."

)

###  Test the Financial Analyzer Skill

Let's test the skill with sample financial data:



# Test the Financial Analyzer skill

if "financial\_skill\_id" in locals():

test\_prompt = """

Calculate financial ratios for this company:

Income Statement:

- Revenue: $1,000M

- EBITDA: $200M

- Net Income: $120M

Balance Sheet:

- Total Assets: $2,000M

- Current Assets: $500M

- Current Liabilities: $300M

- Total Debt: $400M

- Shareholders Equity: $1,200M

Market Data:

- Share Price: $50

- Shares Outstanding: 100M

Please calculate key ratios and provide analysis.

"""

print("Testing Financial Analyzer skill...")

response = test\_skill(client, financial\_skill\_id, test\_prompt)

# Print response

for content in response.content:

if content.type == "text":

print(content.text)

else:

print("⚠️ Please upload the Financial Analyzer skill first (run the previous cell)")

##  4. Example 2: Company Brand Guidelines

Now let's create a skill that ensures all documents follow corporate brand standards.

###  Skill Overview

The **Brand Guidelines** skill will:

* Apply consistent colors, fonts, and layouts
* Ensure logo placement and usage
* Maintain professional tone and messaging
* Work across all document types (Excel, PowerPoint, PDF)



# Upload the Brand Guidelines skill

brand\_skill\_path = SKILLS\_DIR / "applying-brand-guidelines"

if brand\_skill\_path.exists():

print("Uploading Brand Guidelines skill...")

result = create\_skill(client, str(brand\_skill\_path), "Corporate Brand Guidelines")

if result["success"]:

brand\_skill\_id = result["skill\_id"]

print("✅ Skill uploaded successfully!")

print(f" Skill ID: {brand\_skill\_id}")

print(f" Version: {result['latest\_version']}")

else:

print(f"❌ Upload failed: {result['error']}")

if "cannot reuse an existing display\_title" in str(result["error"]):

print("\n💡 Solution: A skill with this name already exists.")

print(" Run the 'Clean Up Existing Skills' cell above to delete it first,")

print(" or change the display\_title to something unique.")

else:

print(f"⚠️ Skill directory not found: {brand\_skill\_path}")

###  Test Brand Guidelines with Document Creation

Let's test the brand skill by creating a branded PowerPoint presentation:



# Test Brand Guidelines skill with PowerPoint creation

if "brand\_skill\_id" in locals():

# Combine brand skill with Anthropic's pptx skill

response = client.beta.messages.create(

model=MODEL,

max\_tokens=4096,

container={

"skills": [

{"type": "custom", "skill\_id": brand\_skill\_id, "version": "latest"},

{"type": "anthropic", "skill\_id": "pptx", "version": "latest"},

]

},

tools=[{"type": "code\_execution\_20250825", "name": "code\_execution"}],

messages=[

{

"role": "user",

"content": """Create a 3-slide PowerPoint presentation following Acme Corporation brand guidelines:

Slide 1: Title slide for "Q4 2025 Results"

Slide 2: Revenue Overview with a chart showing Q1-Q4 growth

Slide 3: Key Achievements (3 bullet points)

Apply all brand colors, fonts, and formatting standards.

""",

}

],

betas=[

"code-execution-2025-08-25",

"files-api-2025-04-14",

"skills-2025-10-02",

],

)

print("Response from Claude:")

for content in response.content:

if content.type == "text":

print(content.text[:500] + "..." if len(content.text) > 500 else content.text)

# Download generated file

file\_ids = extract\_file\_ids(response)

if file\_ids:

results = download\_all\_files(

client, response, output\_dir=str(OUTPUT\_DIR), prefix="branded\_"

)

print\_download\_summary(results)

else:

print("⚠️ Please upload the Brand Guidelines skill first")

##  5. Example 3: Financial Modeling Suite

Let's create our most advanced skill - a comprehensive financial modeling suite for valuation and risk analysis.

###  Skill Overview

The **Financial Modeling Suite** skill provides:

* **DCF Valuation**: Complete discounted cash flow models
* **Sensitivity Analysis**: Test impact of variables on valuation
* **Monte Carlo Simulation**: Risk modeling with probability distributions
* **Scenario Planning**: Best/base/worst case analysis

This demonstrates a multi-file skill with complex calculations and professional-grade financial modeling.

###  Upload the Financial Modeling Suite

First, upload the financial modeling skill:



# Upload the Financial Modeling Suite skill

modeling\_skill\_path = SKILLS\_DIR / "creating-financial-models"

if modeling\_skill\_path.exists():

print("Uploading Financial Modeling Suite skill...")

result = create\_skill(client, str(modeling\_skill\_path), "Financial Modeling Suite")

if result["success"]:

modeling\_skill\_id = result["skill\_id"]

print("✅ Skill uploaded successfully!")

print(f" Skill ID: {modeling\_skill\_id}")

print(f" Version: {result['latest\_version']}")

print("\nThis skill includes:")

print(" - DCF valuation model (dcf\_model.py)")

print(" - Sensitivity analysis framework (sensitivity\_analysis.py)")

print(" - Monte Carlo simulation capabilities")

print(" - Scenario planning tools")

else:

print(f"❌ Upload failed: {result['error']}")

else:

print(f"⚠️ Skill directory not found: {modeling\_skill\_path}")

print(

"Please ensure the custom\_skills directory contains the creating-financial-models folder."

)

###  Test the Financial Modeling Suite

Let's test the advanced modeling capabilities with a DCF valuation request:



# Test the Financial Modeling Suite with a DCF valuation

if "modeling\_skill\_id" in locals():

dcf\_test\_prompt = """

Perform a DCF valuation for TechCorp with the following data:

Historical Financials (Last 3 Years):

- Revenue: $500M, $600M, $750M

- EBITDA Margin: 25%, 27%, 30%

- CapEx: $50M, $55M, $60M

- Working Capital: 15% of revenue

Projections:

- Revenue growth: 20% for years 1-3, then declining to 5% by year 5

- EBITDA margin expanding to 35% by year 5

- Terminal growth rate: 3%

Market Assumptions:

- WACC: 10%

- Tax rate: 25%

- Current net debt: $200M

- Shares outstanding: 100M

Please create a complete DCF model with sensitivity analysis on WACC and terminal growth.

Generate an Excel file with the full model including:

1. Revenue projections

2. Free cash flow calculations

3. Terminal value

4. Enterprise value to equity value bridge

5. Sensitivity table

"""

print("Testing Financial Modeling Suite with DCF valuation...")

print("=" \* 70)

print("\n⏱️ Note: Complex financial model generation may take 1-2 minutes.\n")

response = client.beta.messages.create(

model=MODEL,

max\_tokens=4096,

container={

"skills": [

{"type": "custom", "skill\_id": modeling\_skill\_id, "version": "latest"},

{"type": "anthropic", "skill\_id": "xlsx", "version": "latest"},

]

},

tools=[{"type": "code\_execution\_20250825", "name": "code\_execution"}],

messages=[{"role": "user", "content": dcf\_test\_prompt}],

betas=[

"code-execution-2025-08-25",

"files-api-2025-04-14",

"skills-2025-10-02",

],

)

# Print Claude's response

for content in response.content:

if content.type == "text":

# Print first 800 characters to keep output manageable

text = content.text

if len(text) > 800:

print(text[:800] + "\n\n[... Output truncated for brevity ...]")

else:

print(text)

# Download the DCF model if generated

file\_ids = extract\_file\_ids(response)

if file\_ids:

print("\n" + "=" \* 70)

print("Downloading generated DCF model...")

results = download\_all\_files(

client, response, output\_dir=str(OUTPUT\_DIR), prefix="dcf\_model\_"

)

print\_download\_summary(results)

print("\n💡 Open the Excel file to explore the complete DCF valuation model!")

else:

print("⚠️ Please upload the Financial Modeling Suite skill first (run the previous cell)")

##  6. Skill Management & Versioning

Managing skills over time requires understanding versioning, updates, and lifecycle management.

###  Listing Your Skills

Get an overview of all custom skills in your workspace:



# List all your custom skills

my\_skills = list\_custom\_skills(client)

if my\_skills:

print(f"You have {len(my\_skills)} custom skill(s):\n")

print("=" \* 70)

for i, skill in enumerate(my\_skills, 1):

print(f"\n{i}. {skill['display\_title']}")

print(f" Skill ID: {skill['skill\_id']}")

print(f" Current Version: {skill['latest\_version']}")

print(f" Created: {skill['created\_at']}")

if skill.get("updated\_at"):

print(f" Last Updated: {skill['updated\_at']}")

print("\n" + "=" \* 70)

else:

print("No custom skills found in your workspace.")

###  Creating New Versions

Skills support versioning to maintain history and enable rollback. Let's make an enhancement to our Financial Analyzer skill and create a new version.

####  Step 1: Enhance the Financial Analyzer

We'll add **healthcare industry** benchmarks to make our skill more versatile. This is a real-world scenario where you'd expand a skill's capabilities based on user needs.



# Add healthcare industry benchmarks to the Financial Analyzer

# This demonstrates a realistic skill enhancement scenario

if "financial\_skill\_id" in locals():

# Read the current interpret\_ratios.py file

interpret\_file\_path = SKILLS\_DIR / "analyzing-financial-statements" / "interpret\_ratios.py"

with open(interpret\_file\_path) as f:

content = f.read()

# Add healthcare benchmarks after the 'manufacturing' section

healthcare\_benchmarks = """ },

'healthcare': {

'current\_ratio': {'excellent': 2.3, 'good': 1.8, 'acceptable': 1.4, 'poor': 1.0},

'debt\_to\_equity': {'excellent': 0.3, 'good': 0.6, 'acceptable': 1.0, 'poor': 1.8},

'roe': {'excellent': 0.22, 'good': 0.16, 'acceptable': 0.11, 'poor': 0.07},

'gross\_margin': {'excellent': 0.65, 'good': 0.45, 'acceptable': 0.30, 'poor': 0.20},

'pe\_ratio': {'undervalued': 18, 'fair': 28, 'growth': 40, 'expensive': 55}

"""

# Find the position after manufacturing section and before the closing brace

insert\_pos = content.find(" }\n }") # Find the end of the BENCHMARKS dict

if insert\_pos != -1:

# Insert the healthcare benchmarks

new\_content = content[:insert\_pos] + healthcare\_benchmarks + content[insert\_pos:]

# Save the enhanced file

with open(interpret\_file\_path, "w") as f:

f.write(new\_content)

print("✅ Enhanced Financial Analyzer with healthcare industry benchmarks")

print("\nChanges made:")

print(" - Added healthcare industry to BENCHMARKS")

print(" - Includes specific thresholds for:")

print(" • Current ratio (liquidity)")

print(" • Debt-to-equity (leverage)")

print(" • ROE (profitability)")

print(" • Gross margin")

print(" • P/E ratio (valuation)")

print("\n📝 Now we can create a new version of the skill with this enhancement!")

else:

print("⚠️ Could not find the correct position to insert healthcare benchmarks")

print("The file structure may have changed.")

else:

print("⚠️ Please upload the Financial Analyzer skill first (run cells in Section 3)")

####  Step 2: Create a New Version

Now that we've enhanced our skill, let's create a new version to track this change:



# Create a new version of the enhanced Financial Analyzer skill

def create\_skill\_version(client: Anthropic, skill\_id: str, skill\_path: str):

"""Create a new version of an existing skill."""

try:

version = client.beta.skills.versions.create(

skill\_id=skill\_id, files=files\_from\_dir(skill\_path)

)

return {

"success": True,

"version": version.version,

"created\_at": version.created\_at,

}

except Exception as e:

return {"success": False, "error": str(e)}

# Create the new version with our healthcare enhancement

if "financial\_skill\_id" in locals():

print("Creating new version of Financial Analyzer with healthcare benchmarks...")

result = create\_skill\_version(

client, financial\_skill\_id, str(SKILLS\_DIR / "analyzing-financial-statements")

)

if result["success"]:

print("✅ New version created successfully!")

print(f" Version: {result['version']}")

print(f" Created: {result['created\_at']}")

print("\n📊 Version History:")

print(" v1: Original skill with tech, retail, financial, manufacturing")

print(f" v{result['version']}: Enhanced with healthcare industry benchmarks")

else:

print(f"❌ Version creation failed: {result['error']}")

else:

print("⚠️ Please run the previous cells to upload the skill and make enhancements first")

####  Step 3: Test the New Version

Let's verify our enhancement works by analyzing a healthcare company:



# Test the enhanced skill with healthcare industry data

if "financial\_skill\_id" in locals():

healthcare\_test\_prompt = """

Analyze this healthcare company using the healthcare industry benchmarks:

Company: MedTech Solutions (Healthcare Industry)

Income Statement:

- Revenue: $800M

- EBITDA: $320M

- Net Income: $160M

Balance Sheet:

- Total Assets: $1,200M

- Current Assets: $400M

- Current Liabilities: $200M

- Total Debt: $300M

- Shareholders Equity: $700M

Market Data:

- Share Price: $75

- Shares Outstanding: 50M

Please calculate key ratios and provide healthcare-specific analysis.

"""

print("Testing enhanced Financial Analyzer with healthcare company...")

print("=" \* 70)

response = test\_skill(client, financial\_skill\_id, healthcare\_test\_prompt, MODEL)

# Print Claude's analysis

for content in response.content:

if content.type == "text":

# Print first 1000 characters to keep output manageable

text = content.text

if len(text) > 1000:

print(text[:1000] + "\n\n[... Output truncated for brevity ...]")

else:

print(text)

print(

"\n✅ The skill now recognizes 'healthcare' as an industry and applies specific benchmarks!"

)

else:

print("⚠️ Please run the previous cells to create the enhanced version first")

###  Cleanup: Managing Your Skills

When you're done testing or need to clean up your workspace, you can selectively remove skills. Let's review what we've created and provide options for cleanup:



# Comprehensive skill cleanup with detailed reporting

def review\_and\_cleanup\_skills(client, dry\_run=True):

"""

Review all skills and optionally clean up the ones created in this notebook.

Args:

client: Anthropic client

dry\_run: If True, only show what would be deleted without actually deleting

"""

# Get all current skills

all\_skills = list\_custom\_skills(client)

# Skills we created in this notebook

notebook\_skill\_names = [

"Financial Ratio Analyzer",

"Corporate Brand Guidelines",

"Financial Modeling Suite",

]

# Track skills created by this notebook

notebook\_skills = []

other\_skills = []

for skill in all\_skills:

if skill["display\_title"] in notebook\_skill\_names:

notebook\_skills.append(skill)

else:

other\_skills.append(skill)

print("=" \* 70)

print("SKILL INVENTORY REPORT")

print("=" \* 70)

print(f"\nTotal custom skills in workspace: {len(all\_skills)}")

if notebook\_skills:

print(f"\n📚 Skills created by this notebook ({len(notebook\_skills)}):")

for skill in notebook\_skills:

print(f" • {skill['display\_title']}")

print(f" ID: {skill['skill\_id']}")

print(f" Version: {skill['latest\_version']}")

print(f" Created: {skill['created\_at']}")

else:

print("\n✅ No skills from this notebook found")

if other\_skills:

print(f"\n🔧 Other skills in workspace ({len(other\_skills)}):")

for skill in other\_skills:

print(f" • {skill['display\_title']} (v{skill['latest\_version']})")

# Cleanup options

if notebook\_skills:

print("\n" + "=" \* 70)

print("CLEANUP OPTIONS")

print("=" \* 70)

if dry\_run:

print("\n🔍 DRY RUN MODE - No skills will be deleted")

print("\nTo delete the notebook skills, uncomment and run:")

print("-" \* 40)

print("# review\_and\_cleanup\_skills(client, dry\_run=False)")

print("-" \* 40)

print("\nThis would delete:")

for skill in notebook\_skills:

print(f" • {skill['display\_title']}")

else:

print("\n⚠️ DELETION MODE - Skills will be permanently removed")

print("\nDeleting notebook skills...")

success\_count = 0

for skill in notebook\_skills:

if delete\_skill(client, skill["skill\_id"]):

print(f" ✅ Deleted: {skill['display\_title']}")

success\_count += 1

else:

print(f" ❌ Failed to delete: {skill['display\_title']}")

print(f"\n📊 Cleanup complete: {success\_count}/{len(notebook\_skills)} skills deleted")

return {

"total\_skills": len(all\_skills),

"notebook\_skills": len(notebook\_skills),

"other\_skills": len(other\_skills),

"notebook\_skill\_ids": [s["skill\_id"] for s in notebook\_skills],

}

# Run the review (in dry-run mode by default)

print("Reviewing your custom skills workspace...")

cleanup\_summary = review\_and\_cleanup\_skills(client, dry\_run=True)

# Store skill IDs for potential cleanup

if cleanup\_summary["notebook\_skill\_ids"]:

skills\_to\_cleanup = cleanup\_summary["notebook\_skill\_ids"]

print(f"\n💡 Tip: {len(skills\_to\_cleanup)} skill(s) can be cleaned up when you're done testing")

# UNCOMMENT THE LINE BELOW TO ACTUALLY DELETE THE NOTEBOOK SKILLS:

# review\_and\_cleanup\_skills(client, dry\_run=False)

##  7. Best Practices & Production Tips

###  Skill Design Principles

1. **Single Responsibility**: Each skill should focus on one area of expertise
2. **Clear Documentation**: SKILL.md should be comprehensive yet concise
3. **Error Handling**: Scripts should handle edge cases gracefully
4. **Version Control**: Use Git to track skill changes
5. **Testing**: Always test skills before production deployment

###  Directory Structure Best Practices



custom\_skills/

├── financial\_analyzer/ # Single purpose, clear naming

│ ├── SKILL.md # Under 5,000 tokens

│ ├── scripts/ # Modular Python/JS files

│ └── tests/ # Unit tests for scripts

├── brand\_guidelines/ # Organizational standards

│ ├── SKILL.md

│ ├── REFERENCE.md # Additional documentation

│ └── assets/ # Logos, templates

###  Performance Optimization

| Strategy | Impact | Implementation |
| --- | --- | --- |
| **Minimal Frontmatter** | Faster skill discovery | name: 64 chars, description: 1024 chars |
| **Lazy Loading** | Reduced token usage | Reference files only when needed |
| **Skill Composition** | Avoid duplication | Combine skills vs. mega-skill |
| **Caching** | Faster responses | Reuse skill containers |

###  Security Considerations

* **API Keys**: Never hardcode credentials in skills
* **Data Privacy**: Don't include sensitive data in skill files
* **Access Control**: Skills are workspace-specific
* **Validation**: Sanitize inputs in scripts
* **Audit Trail**: Log skill usage for compliance

##  Next Steps

🎉 **Congratulations!** You've learned how to create, deploy, and manage custom skills for Claude.

###  What You've Learned

* ✅ Custom skill architecture and requirements
* ✅ Creating skills with SKILL.md and Python scripts
* ✅ Uploading skills via the API
* ✅ Combining custom and Anthropic skills
* ✅ Best practices for production deployment
* ✅ Troubleshooting common issues

###  Continue Your Journey

1. **Experiment**: Modify the example skills for your use cases
2. **Build**: Create skills for your organization's workflows
3. **Optimize**: Monitor token usage and performance
4. **Share**: Document your skills for team collaboration

###  Resources

* [Claude API Documentation(opens in new tab)](https://docs.anthropic.com/en/api/messages)
* [Skills Documentation(opens in new tab)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
* [Best Practices(opens in new tab)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
* [Files API Documentation(opens in new tab)](https://docs.claude.com/en/api/files-content)
* Example Skills Repository (coming soon)

###  Skill Ideas to Try

* 📊 **Data Pipeline**: ETL workflows with validation
* 📝 **Document Templates**: Contracts, proposals, reports
* 🔍 **Code Review**: Style guides and best practices
* 📈 **Analytics Dashboard**: KPI tracking and visualization
* 🤖 **Automation Suite**: Repetitive task workflows

Happy skill building! 🚀
