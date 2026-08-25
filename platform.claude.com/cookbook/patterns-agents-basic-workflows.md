<!-- source: https://platform.claude.com/cookbook/patterns-agents-basic-workflows -->

##  Basic Multi-LLM Workflows

This notebook demonstrates three simple multi-LLM workflows. They trade off cost or latency for potentially improved task performances:

1. **Prompt-Chaining**: Decomposes a task into sequential subtasks, where each step builds on previous results
2. **Parallelization**: Distributes independent subtasks across multiple LLMs for concurrent processing
3. **Routing**: Dynamically selects specialized LLM paths based on input characteristics

Note: These are sample implementations meant to demonstrate core concepts - not production code.

from concurrent.futures import ThreadPoolExecutor

from util import extract\_xml, llm\_call

def chain(input: str, prompts: list[str]) -> str:

"""Chain multiple LLM calls sequentially, passing results between steps."""

result = input

for i, prompt in enumerate(prompts, 1):

print(f"\nStep {i}:")

result = llm\_call(f"{prompt}\nInput: {result}")

print(result)

return result

def parallel(prompt: str, inputs: list[str], n\_workers: int = 3) -> list[str]:

"""Process multiple inputs concurrently with the same prompt."""

with ThreadPoolExecutor(max\_workers=n\_workers) as executor:

futures = [executor.submit(llm\_call, f"{prompt}\nInput: {x}") for x in inputs]

return [f.result() for f in futures]

def route(input: str, routes: dict[str, str]) -> str:

"""Route input to specialized prompt using content classification."""

# First determine appropriate route using LLM with chain-of-thought

print(f"\nAvailable routes: {list(routes.keys())}")

selector\_prompt = f"""

Analyze the input and select the most appropriate support team from these options: {list(routes.keys())}

First explain your reasoning, then provide your selection in this XML format:

<reasoning>

Brief explanation of why this ticket should be routed to a specific team.

Consider key terms, user intent, and urgency level.

</reasoning>

<selection>

The chosen team name

</selection>

Input: {input}""".strip()

route\_response = llm\_call(selector\_prompt)

reasoning = extract\_xml(route\_response, "reasoning")

route\_key = extract\_xml(route\_response, "selection").strip().lower()

print("Routing Analysis:")

print(reasoning)

print(f"\nSelected route: {route\_key}")

# Process input with selected specialized prompt

selected\_prompt = routes[route\_key]

return llm\_call(f"{selected\_prompt}\nInput: {input}")

##  Example Usage

Below are practical examples demonstrating each workflow:

1. Chain workflow for structured data extraction and formatting
2. Parallelization workflow for stakeholder impact analysis
3. Route workflow for customer support ticket handling

# Example 1: Chain workflow for structured data extraction and formatting

# Each step progressively transforms raw text into a formatted table

data\_processing\_steps = [

"""Extract only the numerical values and their associated metrics from the text.

Format each as 'value: metric' on a new line.

Example format:

92: customer satisfaction

45%: revenue growth""",

"""Convert all numerical values to percentages where possible.

If not a percentage or points, convert to decimal (e.g., 92 points -> 92%).

Keep one number per line.

Example format:

92%: customer satisfaction

45%: revenue growth""",

"""Sort all lines in descending order by numerical value.

Keep the format 'value: metric' on each line.

Example:

92%: customer satisfaction

87%: employee satisfaction""",

"""Format the sorted data as a markdown table with columns:

| Metric | Value |

|:--|--:|

| Customer Satisfaction | 92% |""",

]

report = """

Q3 Performance Summary:

Our customer satisfaction score rose to 92 points this quarter.

Revenue grew by 45% compared to last year.

Market share is now at 23% in our primary market.

Customer churn decreased to 5% from 8%.

New user acquisition cost is $43 per user.

Product adoption rate increased to 78%.

Employee satisfaction is at 87 points.

Operating margin improved to 34%.

"""

print("\nInput text:")

print(report)

formatted\_result = chain(report, data\_processing\_steps)

```
Input text:

Q3 Performance Summary:
Our customer satisfaction score rose to 92 points this quarter.
Revenue grew by 45% compared to last year.
Market share is now at 23% in our primary market.
Customer churn decreased to 5% from 8%.
New user acquisition cost is $43 per user.
Product adoption rate increased to 78%.
Employee satisfaction is at 87 points.
Operating margin improved to 34%.

Step 1:
92: customer satisfaction points
45%: revenue growth
23%: market share
5%: customer churn
8%: previous customer churn
$43: user acquisition cost
78%: product adoption rate
87: employee satisfaction points
34%: operating margin

Step 2:
92%: customer satisfaction
45%: revenue growth
23%: market share
5%: customer churn
8%: previous customer churn
43.0: user acquisition cost
78%: product adoption rate
87%: employee satisfaction
34%: operating margin

Step 3:
Here are the lines sorted in descending order by numerical value:

92%: customer satisfaction
87%: employee satisfaction
78%: product adoption rate
45%: revenue growth
43.0: user acquisition cost
34%: operating margin
23%: market share
8%: previous customer churn
5%: customer churn

Step 4:
| Metric | Value |
|:--|--:|
| Customer Satisfaction | 92% |
| Employee Satisfaction | 87% |
| Product Adoption Rate | 78% |
| Revenue Growth | 45% |
| User Acquisition Cost | 43.0 |
| Operating Margin | 34% |
| Market Share | 23% |
| Previous Customer Churn | 8% |
| Customer Churn | 5% |
```

# Example 2: Parallelization workflow for stakeholder impact analysis

# Process impact analysis for multiple stakeholder groups concurrently

stakeholders = [

"""Customers:

- Price sensitive

- Want better tech

- Environmental concerns""",

"""Employees:

- Job security worries

- Need new skills

- Want clear direction""",

"""Investors:

- Expect growth

- Want cost control

- Risk concerns""",

"""Suppliers:

- Capacity constraints

- Price pressures

- Tech transitions""",

]

impact\_results = parallel(

"""Analyze how market changes will impact this stakeholder group.

Provide specific impacts and recommended actions.

Format with clear sections and priorities.""",

stakeholders,

)

for result in impact\_results:

print(result)

print("+" \* 80)

```
MARKET IMPACT ANALYSIS FOR CUSTOMERS
==================================

HIGH PRIORITY IMPACTS
-------------------
1. Price Sensitivity
- Rising inflation and costs likely to reduce purchasing power
- Increased competition for value-oriented products
- Risk of trading down to lower-cost alternatives

Recommended Actions:
• Introduce tiered pricing options
• Develop value-focused product lines
• Create loyalty programs with price benefits
• Highlight total cost of ownership benefits

2. Technology Demands
- Accelerating tech advancement creating higher expectations
- Integration of AI and smart features becoming standard
- Mobile/digital-first experience requirements

Recommended Actions:
• Accelerate digital transformation initiatives
• Invest in user experience improvements
• Develop smart product features
• Provide tech education and support

MEDIUM PRIORITY IMPACTS
----------------------
3. Environmental Consciousness
- Growing demand for sustainable products
- Increased scrutiny of environmental practices
- Willingness to pay premium for eco-friendly options

Recommended Actions:
• Develop eco-friendly product lines
• Improve packaging sustainability
• Communicate environmental initiatives
• Create recycling programs

MONITORING & METRICS
-------------------
• Track customer satisfaction scores
• Monitor price sensitivity metrics
• Measure adoption of new technologies
• Track sustainability-related purchases
• Regular customer feedback surveys

RISK FACTORS
------------
• Economic downturn impact on spending
• Tech adoption learning curve
• Cost vs. sustainability trade-offs
• Competition from specialized providers

TIMELINE PRIORITIES
------------------
Immediate (0-3 months):
- Price optimization
- Digital experience improvements

Short-term (3-12 months):
- Tech feature development
- Sustainability initiatives

Long-term (12+ months):
- Advanced technology integration
- Comprehensive eco-friendly transformation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
MARKET IMPACT ANALYSIS FOR EMPLOYEES

Priority 1: Job Security Concerns
Impacts:
• Market volatility creating uncertainty about positions
• Potential restructuring or role changes
• Stress affecting productivity and morale

Recommended Actions:
- Provide regular, transparent communications about company stability
- Create clear performance metrics tied to job security
- Establish early warning systems for at-risk positions
- Develop retention programs for key talent

Priority 2: Skills Gap & Development
Impacts:
• Current skills becoming outdated due to market changes
• New technologies/processes requiring additional training
• Competitive disadvantage without upskilling

Recommended Actions:
- Conduct skills gap analysis
- Implement targeted training programs
- Provide learning stipends/resources
- Create mentorship programs
- Partner with educational institutions

Priority 3: Strategic Direction & Leadership
Impacts:
• Uncertainty about career paths
• Lack of alignment with company goals
• Reduced engagement and commitment

Recommended Actions:
- Develop clear career progression frameworks
- Create individual development plans
- Increase leadership visibility and communication
- Establish regular strategy updates and town halls
- Implement feedback mechanisms

Implementation Timeline:
Short-term (0-3 months):
• Begin transparent communications
• Launch initial training assessments
• Start regular strategy updates

Medium-term (3-6 months):
• Roll out training programs
• Implement retention initiatives
• Develop career frameworks

Long-term (6+ months):
• Monitor and adjust programs
• Measure effectiveness
• Refine strategic alignment

Success Metrics:
• Employee retention rates
• Skills assessment scores
• Employee satisfaction surveys
• Productivity measures
• Career progression rates
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
MARKET IMPACT ANALYSIS FOR INVESTORS

Priority 1: Financial Performance
Impacts:
• Market volatility may affect expected returns
• Economic uncertainty could slow growth targets
• Cost inflation may squeeze margins

Recommended Actions:
- Implement enhanced financial reporting and forecasting
- Develop contingency plans for different market scenarios
- Identify cost optimization opportunities
- Consider strategic M&A opportunities at lower valuations

Priority 2: Risk Management
Impacts:
• Increased market risks require stronger controls
• New regulatory requirements possible
• Competitive landscape changes

Recommended Actions:
- Strengthen risk management frameworks
- Increase frequency of risk assessments
- Diversify investment portfolio
- Maintain higher cash reserves

Priority 3: Communication & Transparency
Impacts:
• Heightened investor scrutiny expected
• Need for more detailed market analysis
• Demand for regular updates

Recommended Actions:
- Enhance investor communications
- Provide more frequent market updates
- Share detailed mitigation strategies
- Maintain open dialogue with key stakeholders

Timeline Recommendations:
Short-term (0-6 months):
- Implement enhanced reporting
- Review risk controls
- Increase communication frequency

Medium-term (6-18 months):
- Execute cost optimization
- Develop new growth strategies
- Build strategic partnerships

Long-term (18+ months):
- Evaluate market position
- Adjust investment strategy
- Consider structural changes

Key Success Metrics:
• ROI performance
• Cost reduction achievements
• Risk incident rates
• Investor satisfaction scores
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
MARKET IMPACT ANALYSIS FOR SUPPLIERS

HIGH PRIORITY IMPACTS:
1. Capacity Constraints
- Reduced ability to meet customer demand
- Risk of losing market share to competitors
- Strain on existing infrastructure and resources
- Potential breach of supply agreements

Recommended Actions:
• Invest in capacity expansion
• Implement better demand forecasting
• Develop contingency supplier network
• Negotiate flexible delivery terms

2. Price Pressures
- Squeezed profit margins
- Difficulty maintaining quality standards
- Risk of losing customers to lower-cost alternatives
- Cash flow challenges

Recommended Actions:
• Review cost structure and identify efficiencies
• Negotiate long-term contracts with price adjustment clauses
• Explore automation/process improvements
• Consider strategic partnerships to share costs

3. Technology Transitions
- Need for new equipment and systems
- Training requirements for workforce
- R&D investment demands
- Risk of obsolescence

Recommended Actions:
• Develop technology roadmap
• Invest in workforce training
• Seek innovation partnerships
• Phase implementation of new technologies

MEDIUM PRIORITY CONSIDERATIONS:
- Supply chain resilience
- Quality control processes
- Market positioning
- Customer relationship management

LONG-TERM STRATEGIC RECOMMENDATIONS:
1. Build financial reserves for future investments
2. Develop diversification strategies
3. Create innovation partnerships
4. Strengthen customer relationships
5. Invest in sustainability initiatives

MONITORING METRICS:
• Production capacity utilization
• Price competitiveness
• Technology adoption rates
• Customer satisfaction levels
• Market share trends
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```

# Example 3: Route workflow for customer support ticket handling

# Route support tickets to appropriate teams based on content analysis

support\_routes = {

"billing": """You are a billing support specialist. Follow these guidelines:

1. Always start with "Billing Support Response:"

2. First acknowledge the specific billing issue

3. Explain any charges or discrepancies clearly

4. List concrete next steps with timeline

5. End with payment options if relevant

Keep responses professional but friendly.

Input: """,

"technical": """You are a technical support engineer. Follow these guidelines:

1. Always start with "Technical Support Response:"

2. List exact steps to resolve the issue

3. Include system requirements if relevant

4. Provide workarounds for common problems

5. End with escalation path if needed

Use clear, numbered steps and technical details.

Input: """,

"account": """You are an account security specialist. Follow these guidelines:

1. Always start with "Account Support Response:"

2. Prioritize account security and verification

3. Provide clear steps for account recovery/changes

4. Include security tips and warnings

5. Set clear expectations for resolution time

Maintain a serious, security-focused tone.

Input: """,

"product": """You are a product specialist. Follow these guidelines:

1. Always start with "Product Support Response:"

2. Focus on feature education and best practices

3. Include specific examples of usage

4. Link to relevant documentation sections

5. Suggest related features that might help

Be educational and encouraging in tone.

Input: """,

}

# Test with different support tickets

tickets = [

"""Subject: Can't access my account

Message: Hi, I've been trying to log in for the past hour but keep getting an 'invalid password' error.

I'm sure I'm using the right password. Can you help me regain access? This is urgent as I need to

submit a report by end of day.

- John""",

"""Subject: Unexpected charge on my card

Message: Hello, I just noticed a charge of $49.99 on my credit card from your company, but I thought

I was on the $29.99 plan. Can you explain this charge and adjust it if it's a mistake?

Thanks,

Sarah""",

"""Subject: How to export data?

Message: I need to export all my project data to Excel. I've looked through the docs but can't

figure out how to do a bulk export. Is this possible? If so, could you walk me through the steps?

Best regards,

Mike""",

]

print("Processing support tickets...\n")

for i, ticket in enumerate(tickets, 1):

print(f"\nTicket {i}:")

print("-" \* 40)

print(ticket)

print("\nResponse:")

print("-" \* 40)

response = route(ticket, support\_routes)

print(response)

print("+" \* 80)

```
Processing support tickets...

Ticket 1:
----------------------------------------
Subject: Can't access my account
    Message: Hi, I've been trying to log in for the past hour but keep getting an 'invalid password' error.
    I'm sure I'm using the right password. Can you help me regain access? This is urgent as I need to
    submit a report by end of day.
    - John

Response:
----------------------------------------

Available routes: ['billing', 'technical', 'account', 'product']
Routing Analysis:

This issue is clearly related to account access and authentication problems. The user is experiencing login difficulties with their password, which is a core account security and access issue. While there might be technical aspects involved, the primary concern is account access restoration. The urgency mentioned by the user and the nature of the problem (password/login issues) makes this a typical account support case. Account team specialists are best equipped to handle password resets, account verification, and access restoration procedures.

Selected route: account
Account Support Response:

Dear John,

I understand your urgency regarding account access. Before proceeding with account recovery, we must verify your identity to maintain security protocols.

Immediate Steps for Account Recovery:
1. Visit our secure password reset page at [secure portal URL]
2. Click "Forgot Password"
3. Enter your email address associated with the account
4. Follow the verification instructions sent to your email

Important Security Notes:
• The reset link expires in 30 minutes
• Do not share reset links or verification codes with anyone
• Ensure you're on our official website (check for https:// and correct domain)

WARNING: If you're unable to access your email or receive the reset link, additional verification will be required through our identity verification process.

Additional Security Recommendations:
- Enable Two-Factor Authentication after regaining access
- Review recent account activity for unauthorized access
- Update passwords on other accounts using similar credentials

Expected Resolution Time:
• Password reset: 5-10 minutes
• Identity verification (if needed): 1-2 business hours

If you continue experiencing issues, please respond with:
1. Account email address
2. Last successful login date
3. Any recent account changes

For urgent report submission, please contact your supervisor about deadline extension while we secure your account.

Regards,
Account Security Team
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ticket 2:
----------------------------------------
Subject: Unexpected charge on my card
    Message: Hello, I just noticed a charge of $49.99 on my credit card from your company, but I thought
    I was on the $29.99 plan. Can you explain this charge and adjust it if it's a mistake?
    Thanks,
    Sarah

Response:
----------------------------------------

Available routes: ['billing', 'technical', 'account', 'product']
Routing Analysis:

This is clearly a billing-related inquiry as it involves:
1. Questions about charges on a credit card
2. Pricing plan discrepancy ($49.99 vs $29.99)
3. Request for explanation of charges
4. Potential request for refund/adjustment
The customer is specifically questioning a financial transaction, which falls under the billing team's expertise. While it touches on account plans, the core issue is about charges and payment processing.

Selected route: billing
Billing Support Response:

Dear Sarah,

I understand your concern about the unexpected charge of $49.99 when you were expecting to be billed $29.99.

After reviewing the charge, this difference typically occurs when:
1. The promotional period for the $29.99 rate has ended
2. There was a plan upgrade or change in service tier
3. Additional services were added to the account

To resolve this, I will:
1. Review your account history within 1 business day
2. Send you a detailed breakdown of the charges by email
3. If an error is confirmed, process a refund within 2-3 business days
4. Ensure your plan is set to the correct rate moving forward

For immediate action, you can:
- Review your current plan settings in your account dashboard
- Send us your last billing statement for comparison
- Provide any promotional codes you may have applied previously

Payment options available:
- If a refund is due, it will be credited to your original payment method
- You can adjust your plan back to $29.99 through your account settings if eligible
- Monthly auto-pay can be reviewed and updated as needed

Please let me know if you need any additional information or have questions about these next steps.

Best regards,
Billing Support Team
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ticket 3:
----------------------------------------
Subject: How to export data?
    Message: I need to export all my project data to Excel. I've looked through the docs but can't
    figure out how to do a bulk export. Is this possible? If so, could you walk me through the steps?
    Best regards,
    Mike

Response:
----------------------------------------

Available routes: ['billing', 'technical', 'account', 'product']
Routing Analysis:

This is clearly a technical/how-to question about product functionality. The user is asking for specific instructions about a feature (data export), and mentions looking through documentation. The question is about product usage and requires technical knowledge to explain the export process. Keywords like "export," "data," "bulk export," and reference to documentation strongly indicate this is a technical support matter rather than billing, account, or general product inquiry.

Selected route: technical
Technical Support Response:

I'll help you export your project data to Excel. Here's the complete process:

Steps to Export Data:
1. Log into your project dashboard
2. Navigate to "Project Settings" in the top right corner
3. Select "Data Management" from the dropdown menu
4. Click the "Export" tab
5. Choose "Bulk Export" option
6. Select data range and specific fields to export
7. Choose "Excel (.xlsx)" as the output format
8. Click "Generate Export"
9. Wait for the system to process (may take 1-15 minutes depending on data size)
10. Download the exported file when ready

System Requirements:
- Supported browsers: Chrome 90+, Firefox 88+, Edge 91+
- Minimum 2GB RAM available
- Stable internet connection
- Excel 2016 or later for opening exported files

Common Issues & Workarounds:
A. If export times out:
   - Break data into smaller date ranges
   - Export during off-peak hours
   - Use filters to reduce data size

B. If download fails:
   - Clear browser cache
   - Use incognito/private window
   - Try a different supported browser

Escalation Path:
If you continue experiencing issues:
1. Contact your project administrator
2. Submit a ticket to technical support at support@company.com
3. Include your project ID and any error messages received
4. For urgent matters, call our support hotline: 1-800-XXX-XXXX
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
