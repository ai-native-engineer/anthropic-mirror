<!-- source: https://platform.claude.com/cookbook/observability-usage-cost-api -->

#  Usage & Cost Admin API Cookbook

**A practical guide to programmatically accessing your Claude API usage and cost data**

###  What You Can Do

**Usage Tracking:**

* Monitor token consumption (uncached input, output, cache creation/reads)
* Track usage across models, workspaces, and API keys
* Analyze cache efficiency and server tool usage

**Cost Analysis:**

* Retrieve detailed cost breakdowns by service type
* Monitor spending trends across workspaces
* Generate reports for finance and chargeback scenarios

**Common Use Cases:**

* **Usage Monitoring**: Track consumption patterns and optimize costs
* **Cost Attribution**: Allocate expenses across teams/projects by workspace
* **Cache Analysis**: Measure and improve cache efficiency
* **Financial Reporting**: Generate executive summaries and budget reports

###  API Overview

Two main endpoints:

1. **Messages Usage API**: Token-level usage data with flexible grouping
2. **Cost API**: Financial data in USD with service breakdowns

###  Prerequisites & Security

* **Admin API Key**: Get from [Claude Console(opens in new tab)](https://console.anthropic.com/settings/admin-keys) (format: `sk-ant-admin...`)
* **Security**: Store keys in environment variables, rotate regularly, never commit to version control

import os

from datetime import datetime, time, timedelta

from typing import Any

import requests

class AnthropicAdminAPI:

"""Secure wrapper for Anthropic Admin API endpoints."""

def \_\_init\_\_(self, api\_key: str | None = None):

self.api\_key = api\_key or os.getenv("ANTHROPIC\_ADMIN\_API\_KEY")

if not self.api\_key:

raise ValueError(

"Admin API key required. Set ANTHROPIC\_ADMIN\_API\_KEY environment variable."

)

if not self.api\_key.startswith("sk-ant-admin"):

raise ValueError("Invalid Admin API key format.")

self.base\_url = "https://api.anthropic.com/v1/organizations"

self.headers = {

"anthropic-version": "2023-06-01",

"x-api-key": self.api\_key,

"Content-Type": "application/json",

}

def \_make\_request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:

"""Make authenticated request with basic error handling."""

url = f"{self.base\_url}/{endpoint}"

try:

response = requests.get(url, headers=self.headers, params=params, timeout=30)

response.raise\_for\_status()

return response.json()

except requests.exceptions.HTTPError as e:

if response.status\_code == 401:

raise ValueError("Invalid API key or insufficient permissions") from e

elif response.status\_code == 429:

raise requests.exceptions.RequestException(

"Rate limit exceeded - try again later"

) from e

else:

raise requests.exceptions.RequestException(f"API error: {e}") from e

# Test connection

def test\_connection():

try:

client = AnthropicAdminAPI()

# Simple test query - snap to start of day to align with bucket boundaries

params = {

"starting\_at": (

datetime.combine(datetime.utcnow(), time.min) - timedelta(days=1)

).strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": datetime.combine(datetime.utcnow(), time.min).strftime(

"%Y-%m-%dT%H:%M:%SZ"

),

"bucket\_width": "1d",

"limit": 1,

}

client.\_make\_request("usage\_report/messages", params)

print("✅ Connection successful!")

return client

except Exception as e:

print(f"❌ Connection failed: {e}")

return None

client = test\_connection()

##  Basic Usage & Cost Tracking

###  Understanding Usage Data

The Messages Usage API provides token consumption in **time buckets** - fixed intervals containing aggregated usage.

**Key Metrics:**

* **uncached\_input\_tokens**: New input tokens (prompts, system messages)
* **output\_tokens**: Claude's responses
* **cache\_creation**: Tokens cached for reuse
* **cache\_read\_input\_tokens**: Previously cached tokens reused

###  Basic Usage Query

def get\_daily\_usage(client, days\_back=7):

"""Get usage data for the last N days."""

end\_time = datetime.combine(datetime.utcnow(), time.min)

start\_time = end\_time - timedelta(days=days\_back)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"bucket\_width": "1d",

"limit": days\_back,

}

return client.\_make\_request("usage\_report/messages", params)

def analyze\_usage\_data(response):

"""Process and display usage data."""

if not response or not response.get("data"):

print("No usage data found.")

return

total\_uncached\_input = total\_output = total\_cache\_creation = 0

total\_cache\_reads = total\_web\_searches = 0

daily\_data = []

for bucket in response["data"]:

date = bucket["starting\_at"][:10]

# Sum all results in bucket

bucket\_uncached = bucket\_output = bucket\_cache\_creation = 0

bucket\_cache\_reads = bucket\_web\_searches = 0

for result in bucket["results"]:

bucket\_uncached += result.get("uncached\_input\_tokens", 0)

bucket\_output += result.get("output\_tokens", 0)

cache\_creation = result.get("cache\_creation", {})

bucket\_cache\_creation += cache\_creation.get(

"ephemeral\_1h\_input\_tokens", 0

) + cache\_creation.get("ephemeral\_5m\_input\_tokens", 0)

bucket\_cache\_reads += result.get("cache\_read\_input\_tokens", 0)

server\_tools = result.get("server\_tool\_use", {})

bucket\_web\_searches += server\_tools.get("web\_search\_requests", 0)

daily\_data.append(

{

"date": date,

"uncached\_input\_tokens": bucket\_uncached,

"output\_tokens": bucket\_output,

"cache\_creation": bucket\_cache\_creation,

"cache\_reads": bucket\_cache\_reads,

"web\_searches": bucket\_web\_searches,

"total\_tokens": bucket\_uncached + bucket\_output,

}

)

# Add to totals

total\_uncached\_input += bucket\_uncached

total\_output += bucket\_output

total\_cache\_creation += bucket\_cache\_creation

total\_cache\_reads += bucket\_cache\_reads

total\_web\_searches += bucket\_web\_searches

# Calculate cache efficiency

total\_input\_tokens = total\_uncached\_input + total\_cache\_creation + total\_cache\_reads

cache\_efficiency = (

(total\_cache\_reads / total\_input\_tokens \* 100) if total\_input\_tokens > 0 else 0

)

# Display summary

print("📊 Usage Summary:")

print(f"Uncached input tokens: {total\_uncached\_input:,}")

print(f"Output tokens: {total\_output:,}")

print(f"Cache creation: {total\_cache\_creation:,}")

print(f"Cache reads: {total\_cache\_reads:,}")

print(f"Cache efficiency: {cache\_efficiency:.1f}%")

print(f"Web searches: {total\_web\_searches:,}")

return daily\_data

# Example usage

if client:

usage\_response = get\_daily\_usage(client, days\_back=7)

daily\_usage = analyze\_usage\_data(usage\_response)

```
📊 Usage Summary:
Uncached input tokens: 267,751
Output tokens: 2,848,746
Cache creation: 0
Cache reads: 0
Cache efficiency: 0.0%
Web searches: 0
```

##  Basic Cost Tracking

Note: Priority Tier costs use a different billing model and will never appear in the cost endpoint. You can track Priority Tier usage in the usage endpoint, but not costs.

def get\_daily\_costs(client, days\_back=7):

"""Get cost data for the last N days."""

end\_time = datetime.combine(datetime.utcnow(), time.min)

start\_time = end\_time - timedelta(days=days\_back)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"bucket\_width": "1d", # Only 1d supported for cost API

"limit": min(days\_back, 31), # Max 31 days per request

}

return client.\_make\_request("cost\_report", params)

def analyze\_cost\_data(response):

"""Process and display cost data."""

if not response or not response.get("data"):

print("No cost data found.")

return

total\_cost\_minor\_units = 0

daily\_costs = []

for bucket in response["data"]:

date = bucket["starting\_at"][:10]

# Sum all costs in this bucket

bucket\_cost = 0

for result in bucket["results"]:

# Convert string amounts to float if needed

amount = result.get("amount", 0)

if isinstance(amount, str):

try:

amount = float(amount)

except (ValueError, TypeError):

amount = 0

bucket\_cost += amount

daily\_costs.append(

{

"date": date,

"cost\_minor\_units": bucket\_cost,

"cost\_usd": bucket\_cost / 100, # Convert to dollars

}

)

total\_cost\_minor\_units += bucket\_cost

total\_cost\_usd = total\_cost\_minor\_units / 100

print("💰 Cost Summary:")

print(f"Total cost: ${total\_cost\_usd:.4f}")

print(f"Average daily cost: ${total\_cost\_usd / len(daily\_costs):.4f}")

return daily\_costs

# Example usage

if client:

cost\_response = get\_daily\_costs(client, days\_back=7)

daily\_costs = analyze\_cost\_data(cost\_response)

```
💰 Cost Summary:
Total cost: $83.7574
Average daily cost: $11.9653
```

##  Grouping, Filtering & Pagination

###  Time Granularity Options

**Usage API** supports three granularities:

* `1m` (1 minute): High-resolution analysis, max 1440 buckets per request
* `1h` (1 hour): Medium-resolution, max 168 buckets per request
* `1d` (1 day): Daily analysis, max 31 buckets per request

**Cost API** supports:

* `1d` (1 day): Only option available, max 31 buckets per request

###  Grouping and Filtering

def get\_usage\_by\_model(client, days\_back=7):

"""Get usage data grouped by model, handling pagination automatically."""

end\_time = datetime.combine(datetime.utcnow(), time.min)

start\_time = end\_time - timedelta(days=days\_back)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"group\_by[]": ["model"],

"bucket\_width": "1d",

}

# Aggregate across all pages of data

model\_usage = {}

page\_count = 0

max\_pages = 10 # Reasonable limit to avoid infinite loops

try:

next\_page = None

while page\_count < max\_pages:

current\_params = params.copy()

if next\_page:

current\_params["page"] = next\_page

response = client.\_make\_request("usage\_report/messages", current\_params)

page\_count += 1

# Process this page's data

for bucket in response.get("data", []):

for result in bucket.get("results", []):

model = result.get("model", "Unknown")

uncached = result.get("uncached\_input\_tokens", 0)

output = result.get("output\_tokens", 0)

cache\_creation = result.get("cache\_creation", {})

cache\_creation\_tokens = cache\_creation.get(

"ephemeral\_1h\_input\_tokens", 0

) + cache\_creation.get("ephemeral\_5m\_input\_tokens", 0)

cache\_reads = result.get("cache\_read\_input\_tokens", 0)

tokens = uncached + output + cache\_creation\_tokens + cache\_reads

if model not in model\_usage:

model\_usage[model] = 0

model\_usage[model] += tokens

# Check if there's more data

if not response.get("has\_more", False):

break

next\_page = response.get("next\_page")

if not next\_page:

break

except Exception as e:

print(f"❌ Error retrieving usage data: {e}")

return {}

# Display results

print("📊 Usage by Model:")

if not model\_usage:

print(f" No usage data found in the last {days\_back} days")

print(" 💡 Try increasing the time range or check if you have recent API usage")

else:

for model, tokens in sorted(model\_usage.items(), key=lambda x: x[1], reverse=True):

print(f" {model}: {tokens:,} tokens")

return model\_usage

def filter\_usage\_example(client):

"""Example of filtering usage data."""

params = {

"starting\_at": (datetime.combine(datetime.utcnow(), time.min) - timedelta(days=7)).strftime(

"%Y-%m-%dT%H:%M:%SZ"

),

"ending\_at": datetime.combine(datetime.utcnow(), time.min).strftime("%Y-%m-%dT%H:%M:%SZ"),

"models[]": ["claude-sonnet-4-6"], # Filter to specific model

"service\_tiers[]": ["standard"], # Filter to standard tier

"bucket\_width": "1d",

}

response = client.\_make\_request("usage\_report/messages", params)

print(f"Found {len(response.get('data', []))} days of filtered usage data")

return response

# Example usage

if client:

model\_usage = get\_usage\_by\_model(client, days\_back=14)

filtered\_usage = filter\_usage\_example(client)

```
📊 Usage by Model:
  claude-3-5-haiku-20241022: 995,781 tokens
  claude-sonnet-4-6: 861,880 tokens
  claude-opus-4-1: 394,646 tokens
  claude-sonnet-4-6: 356,766 tokens
  claude-opus-4-20250514: 308,223 tokens
  claude-opus-4-1: 199,201 tokens
Found 7 days of filtered usage data
```

###  Pagination for Large Datasets

def fetch\_all\_usage\_data(client, params, max\_pages=10):

"""Fetch all paginated usage data."""

all\_data = []

page\_count = 0

next\_page = None

print("📥 Fetching paginated data...")

while page\_count < max\_pages:

current\_params = params.copy()

if next\_page:

current\_params["page"] = next\_page

try:

response = client.\_make\_request("usage\_report/messages", current\_params)

if not response or not response.get("data"):

break

page\_data = response["data"]

all\_data.extend(page\_data)

page\_count += 1

print(f" Page {page\_count}: {len(page\_data)} time buckets")

if not response.get("has\_more", False):

print(f"✅ Complete: Retrieved all data in {page\_count} pages")

break

next\_page = response.get("next\_page")

if not next\_page:

break

except Exception as e:

print(f"❌ Error on page {page\_count + 1}: {e}")

break

print(f"📊 Total retrieved: {len(all\_data)} time buckets")

return all\_data

def large\_dataset\_example(client, days\_back=3):

"""Example of handling a large dataset with pagination."""

# Use recent time range to ensure we have data

start\_time = datetime.combine(datetime.utcnow(), time.min) - timedelta(days=days\_back)

end\_time = datetime.combine(datetime.utcnow(), time.min)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"bucket\_width": "1h", # Hourly data for more buckets

"group\_by[]": ["model"],

"limit": 24, # One day per page

}

all\_buckets = fetch\_all\_usage\_data(client, params, max\_pages=5)

# Process the large dataset

if all\_buckets:

total\_tokens = sum(

sum(

result.get("uncached\_input\_tokens", 0) + result.get("output\_tokens", 0)

for result in bucket["results"]

)

for bucket in all\_buckets

)

print(f"📈 Total tokens across all data: {total\_tokens:,}")

return all\_buckets

# Example usage - use shorter time range to find recent data

if client:

large\_dataset = large\_dataset\_example(client, days\_back=3)

```
📥 Fetching paginated data...
  Page 1: 24 time buckets
  Page 2: 24 time buckets
  Page 3: 24 time buckets
✅ Complete: Retrieved all data in 3 pages
📊 Total retrieved: 72 time buckets
📈 Total tokens across all data: 1,336,287
```

##  Simple Data Export

###  CSV Export for External Analysis

import csv

def export\_usage\_to\_csv(client, output\_file="usage\_data.csv", days\_back=30):

"""Export usage data to CSV for external analysis."""

end\_time = datetime.combine(datetime.utcnow(), time.min)

start\_time = end\_time - timedelta(days=days\_back)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"group\_by[]": ["model", "service\_tier", "workspace\_id"],

"bucket\_width": "1d",

}

try:

# Collect all data across pages

rows = []

page\_count = 0

max\_pages = 20 # Allow more pages for export

next\_page = None

while page\_count < max\_pages:

current\_params = params.copy()

if next\_page:

current\_params["page"] = next\_page

response = client.\_make\_request("usage\_report/messages", current\_params)

page\_count += 1

# Process this page's data

for bucket in response.get("data", []):

date = bucket["starting\_at"][:10]

for result in bucket["results"]:

rows.append(

{

"date": date,

"model": result.get("model", ""),

"service\_tier": result.get("service\_tier", ""),

"workspace\_id": result.get("workspace\_id", ""),

"uncached\_input\_tokens": result.get("uncached\_input\_tokens", 0),

"output\_tokens": result.get("output\_tokens", 0),

"cache\_creation\_tokens": (

result.get("cache\_creation", {}).get("ephemeral\_1h\_input\_tokens", 0)

+ result.get("cache\_creation", {}).get(

"ephemeral\_5m\_input\_tokens", 0

)

),

"cache\_read\_tokens": result.get("cache\_read\_input\_tokens", 0),

"web\_search\_requests": result.get("server\_tool\_use", {}).get(

"web\_search\_requests", 0

),

}

)

# Check if there's more data

if not response.get("has\_more", False):

break

next\_page = response.get("next\_page")

if not next\_page:

break

# Write CSV

if rows:

with open(output\_file, "w", newline="") as csvfile:

writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())

writer.writeheader()

writer.writerows(rows)

print(f"✅ Exported {len(rows)} rows to {output\_file}")

else:

print(f"No usage data to export for the last {days\_back} days")

print("💡 Try increasing days\_back or check if you have recent API usage")

except Exception as e:

print(f"❌ Export failed: {e}")

def export\_costs\_to\_csv(client, output\_file="cost\_data.csv", days\_back=30):

"""Export cost data to CSV."""

end\_time = datetime.combine(datetime.utcnow(), time.min)

start\_time = end\_time - timedelta(days=days\_back)

params = {

"starting\_at": start\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"ending\_at": end\_time.strftime("%Y-%m-%dT%H:%M:%SZ"),

"group\_by[]": ["workspace\_id", "description"],

}

try:

# Collect all data across pages

rows = []

page\_count = 0

max\_pages = 20

next\_page = None

while page\_count < max\_pages:

current\_params = params.copy()

if next\_page:

current\_params["page"] = next\_page

response = client.\_make\_request("cost\_report", current\_params)

page\_count += 1

# Process this page's data

for bucket in response.get("data", []):

date = bucket["starting\_at"][:10]

for result in bucket["results"]:

# Handle both string and numeric amounts

amount = result.get("amount", 0)

if isinstance(amount, str):

try:

amount = float(amount)

except (ValueError, TypeError):

amount = 0

rows.append(

{

"date": date,

"workspace\_id": result.get(

"workspace\_id", ""

), # null for default workspace

"description": result.get("description", ""),

"currency": result.get("currency", "USD"),

"amount\_usd": amount / 100,

}

)

# Check if there's more data

if not response.get("has\_more", False):

break

next\_page = response.get("next\_page")

if not next\_page:

break

if rows:

with open(output\_file, "w", newline="") as csvfile:

writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())

writer.writeheader()

writer.writerows(rows)

print(f"✅ Exported {len(rows)} cost records to {output\_file}")

else:

print(f"No cost data to export for the last {days\_back} days")

print("💡 Try increasing days\_back or check if you have recent API usage")

except Exception as e:

print(f"❌ Cost export failed: {e}")

# Example usage

if client:

export\_usage\_to\_csv(client, "my\_usage\_data.csv", days\_back=14)

export\_costs\_to\_csv(client, "my\_cost\_data.csv", days\_back=14)

```
✅ Exported 36 rows to my_usage_data.csv
✅ Exported 72 cost records to my_cost_data.csv
```

##  Wrapping Up

This cookbook covers the essential patterns for working with the Usage & Cost Admin API:

* **Basic queries** for usage and cost data
* **Grouping and filtering** for detailed analysis
* **Pagination** for large datasets
* **Cost description parsing** for categorization
* **Common gotchas** to avoid issues
* **Simple CSV export** for external tools

###  Next Steps

* Check the [official API documentation(opens in new tab)](https://docs.claude.com) for the latest field definitions
* Test your integration with small date ranges first
* Consider data retention needs for your use case
* Monitor for new API features that may enhance your analysis

###  Important Notes

* Field names and available options may evolve as the API matures
* Always handle unknown values gracefully in production code
* The API is designed for historical analysis, not real-time monitoring
* Priority Tier costs use a different billing model and don't appear in cost endpoints

Happy analyzing! 📊
