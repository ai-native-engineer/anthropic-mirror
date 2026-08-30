<!-- source: https://academy.claude.com/tutorials/using-the-blender-connector-in-claude -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Using the Blender Connector in Claude

Connect Claude to Blender so it can read and work with your open scene directly.

10 minClaude Cowork

[Open Cowork](claude://cowork/new)

![](https://academy.claude.com/assets/v1/thumbnail.light-m4ibfqqy.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-n82pdpre.png)

## What this connector provides[](#what-this-connector-provides)

The Blender connector gives Claude access to your open Blender scene through Blender's Python API. With it connected, you can ask Claude to read and explain a complex node or modifier setup, batch-apply changes across many objects, clean out unused data, and write Python that adds new tools to Blender's interface.

The connector was built by the Blender developers and released as part of [Claude for Creative Work(opens in new tab)](https://www.anthropic.com/news/claude-for-creative-work).

## Setting up the Blender connector[](#setting-up-the-blender-connector)

First, add the Blender connector in Claude Desktop, then install an add-on inside Blender so the two can communicate. After setting up once, start the connection from inside Blender each time you work.

### **Prerequisites**[](#prerequisites)

* [**Claude Desktop**(opens in new tab)](https://claude.ai/download) — any Claude plan, including Free
* **Blender 4.2 or later** — free at [blender.org/download(opens in new tab)](https://www.blender.org/download/)

### **Step 1: Add the connector in Claude Desktop**[](#step-1-add-the-connector-in-claude-desktop)

In Claude Desktop, go to **Customize > Connectors**, search for **Blender**, and select **Add**.

![](https://academy.claude.com/assets/media/d4391b5d9435fd7fa3ae8d240049d3152ab91d08e754314bfdd9df4090cdb761.png)

### **Step 2: Install the add-on in Blender**[](#step-2-install-the-add-on-in-blender)

1. Open the [Blender MCP Server page(opens in new tab)](https://www.blender.org/lab/mcp-server/) in a browser alongside Blender.
2. Drag the install link from that page into the Blender window. Blender will prompt you to add the **lab** extension repository; allow it.
3. Drag the same link into Blender a second time. This installs the add-on. Blender will notify you in the status bar when updates are available.

### **Step 3: Start the connection**[](#step-3-start-the-connection)

1. Open your Blender project.
2. Go to Edit > Preferences > Add-ons
3. Find BlenderMCP tab and enable/ click 'start MCP server'

For more on installing connectors from the directory, see [Browsing the Connectors Directory(opens in new tab)](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory).

The connector is built on the open Model Context Protocol and works with other MCP clients, including Claude Code. For setup outside Claude Desktop, see Blender's [MCP server documentation(opens in new tab)](https://www.blender.org/lab/mcp-server/) and the [Claude Code MCP guide(opens in new tab)](https://code.claude.com/docs/en/mcp).

## Example use cases[](#example-use-cases)

#### **Clean up scene naming**

Your scene has objects, collections, and materials with default or misleading names left over from earlier iterations.

Look at the open scene and rename the data blocks so each name matches what it contains. Flag any names that are misleading, like a collection called "rocks" that only contains pebble meshes.

Open in Cowork

#### **Understand a complex setup you didn't build**

You've opened a .blend file from the community and want to understand how its Geometry Nodes tree works before you change anything.

Walk through the Geometry Nodes modifier on the active object. Explain what each node group does in the order data flows through them, and write your notes as frame labels inside the node editor so the explanation is saved in the file.

Open in Cowork

#### **Find what's using an object or material**

You want to change or delete something but aren't sure what else in the file depends on it.

List everything in this file that uses the "Glass\_Tinted" material, including objects, node groups, and Geometry Nodes setups. Tell me what would break if I removed it.

Open in Cowork

#### **Find the heaviest objects in a scene**

Render times are long and you want to know where the polygon budget is going relative to what's visible on screen.

For each mesh in the scene, report its polygon count alongside how large it appears in the active camera's final render. Sort by polygon count and flag anything that's heavy but small on screen.

Open in Cowork

![](https://academy.claude.com/assets/media/2e2c8a050fe83d42f91004bf7b460c3cf476b579d977dad095fac9940c209d41.png)

## Frequently asked questions[](#frequently-asked-questions)

* **Does the connector work on claude.ai in the browser?** — No. The connector needs Blender running on the same machine as Claude, so it requires Claude Desktop.
* **Does Claude edit my .blend file directly?** — Claude operates on the open scene through Blender's Python API. Changes apply to your session and are written to disk when you save in Blender.
* **Do I need to know Python?** — No. You describe what you want and Claude writes and runs the Python. You can ask to see the code first if you want to review it or learn from it.

* [What this connector provides](#what-this-connector-provides)
* [Setting up the Blender connector](#setting-up-the-blender-connector)
* [Example use cases](#example-use-cases)
* [Frequently asked questions](#frequently-asked-questions)
