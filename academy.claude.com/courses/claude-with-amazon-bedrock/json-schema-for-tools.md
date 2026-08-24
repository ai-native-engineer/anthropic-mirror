<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/json-schema-for-tools -->

Lesson 23 of 65 · Claude with Amazon BedrockJSON Schema for tools

After creating your tool function, the next step is writing a JSON schema to describe it. This schema tells Claude what arguments your function expects and how to use it properly. While the configuration might look intimidating at first, it's actually straightforward once you understand the process.

## Understanding JSON Schema

JSON Schema isn't something invented just for AI tools - it's been around for years as a standard way to validate data. The schema has two main parts: the name and description at the top (which help Claude understand when to use the tool), and the actual schema that describes the function's arguments.

![](https://academy.claude.com/assets/media/4f9eb92ac92c4d104bd4188885d3eff8ed7b78c962a75bf4c3b1cc456894aff1.png)

The top section contains the tool's name and description, which helps Claude understand when to use it. The bottom section is the actual schema that describes your function's arguments in detail.

## Creating a JSON Schema: Step-by-Step

Here's the simplest way to create a JSON schema for any function:

### Step 1: Write a Dictionary with Sample Data

Take your function and create a dictionary of all keyword arguments with sample data. For example, if you have a function like this:

python

```
def process_data(ids, profile, primary_id, value):
    pass
```

Create a dictionary with sample values:

![](https://academy.claude.com/assets/media/45dc10d709dd7a8967367cbec8a349090f3613e3ef8dc7c7633e761e30d2cde7.png)

### Step 2: Convert to JSON

Convert your Python dictionary to proper JSON format. The main difference is changing Python's `True` to JSON's `true`.

![](https://academy.claude.com/assets/media/d177a699af0fe1303683ea4279df2ea3466ded1f78370ae949e062f3ddf260e0.png)

### Step 3: Use an Online Converter

Search for "JSON to JSON Schema converter" and use one of the many free online tools. Paste your JSON data and let it generate the schema automatically.

![](https://academy.claude.com/assets/media/fac5eb551cc26408c62aa5e1ea21ffa04b1b4dbeacb7312089a99b84ebad974e.png)

The tool will analyze your sample data and create a proper schema structure. Remove any `$schema` declarations from the output - you don't need them.

### Step 4: Add Descriptions

The most important step is adding detailed descriptions to each property. These descriptions help Claude understand exactly what each argument does and how to use it.

![](https://academy.claude.com/assets/media/1e49419e1af6a7f4e9b0ee35e6e2c01c0b85012d6819463b4f87122c3e915a97.png)

## Writing Good Descriptions

When writing descriptions for your tools and properties, follow these best practices:

* Explain what the tool does, when to use it, and what it returns
* Aim for 3-4 sentences in your tool description
* Provide super detailed descriptions for each property
* If you're stuck, paste your function into Claude and ask it to write descriptions for you

Here's an example of a well-described tool schema:

![](https://academy.claude.com/assets/media/cf9af981071dbfc4414f4402c77be9c86a55a210fd62fb3daf543839d9685f4d.png)

Notice how the description clearly explains what the weather tool does, when to use it, what data it returns, and provides specific examples of valid location formats.

## Putting It All Together

Your final JSON schema should look something like this structure, with the `toolSpec` containing the name, description, and `inputSchema` with the detailed argument specifications:

![](https://academy.claude.com/assets/media/62744d87fb2e71403697f8f18ecf2be24fe1f1ffefff3c8ea39c04cc27652aec.png)

The schema acts as a contract between your code and Claude, ensuring that when Claude decides to use your tool, it knows exactly what information to provide and in what format. This clear communication is what makes tool use reliable and effective.
