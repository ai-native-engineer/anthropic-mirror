<!-- source: https://academy.claude.com/use-cases/design-a-local-foraging-guide -->

![Design a local foraging guide result](https://academy.claude.com/assets/v1/design-a-local-foraging-guide-dh2oo11j.png)[Open artifact](https://claude.ai/public/artifacts/fb72e7a7-3e0f-4f81-859b-0e7a4667cb21)

Build a location-aware guide to wild plants in your region. Select your state on an interactive map, browse plants by category, see what's in season now, and export a printable field reference.

Tell Claude the tool's purpose, the interaction flow, and your design direction. Specific functional requirements and aesthetic cues produce more polished results.

I want to build a foraging guide for someone new to wild edibles and unsure where to start.

What it should do:

* Let users click their state on an interactive US map to see regional foraging data (fetch map data from the us-atlas TopoJSON CDN at [https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json(opens in new tab)](https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json) and render with D3's geoAlbersUsa projection)
* Browse edible plants by category and show a 12-month season bar for each species so users see harvest windows at a glance
* Let users tap any plant to expand details, then let users add plants to a personal foraging list and export a printable field guide with their selected species and safety reminders

Design: Quiet and organic. Warm cream, muted sage, soft olive. Think field journal meets editorial magazine—sophisticated but approachable. Smooth transitions, rounded corners, good type hierarchy.

Claude builds working artifacts directly in conversation. Enable Artifacts in settings so Claude can create interactive applications you can use immediately.

Turn on Artifacts in your settings. This lets Claude generate apps with full interactivity—maps, state management, data visualization—that render right in the chat. No setup or deployment needed.

For complex, multi-component apps, turn on [Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) so Claude can plan architecture before building.

### Optional context

[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

Claude produces a complete, working foraging guide beginning with an interactive US map where clicking a state reveals regional plant data.

I've built your Wild Edibles Field Guide. Here's what you can do:

**Explore by region** — Click any highlighted state on the map. The guide currently includes data for the Pacific Northwest (Washington, Oregon, Idaho) and Northeast (Maine through Maryland). Other regions show as coming soon.

**Browse by category** — Once you've selected a state, use the tabs to explore wild greens, berries, mushrooms, roots, and nuts available in your region.

**Check seasonality** — Each plant card shows a 12-month bar indicating harvest windows. The current month is highlighted so you immediately see what's in season.

**Dig deeper** — Tap any card to expand details: where to find it, how to prepare it, and any look-alikes to watch for. Plants with dangerous look-alikes show a warning panel.

**Build your list** — Click the + button to add plants to your foraging list. Your selections appear in a floating panel that tracks your count.

**Export a field guide** — When you're ready, export generates a printable reference with your selected species, preparation notes, and safety reminders.

View your Field Guide

### Swap in verified information

The guide uses sample data to demonstrate how it works. Once you're happy with how it looks and feels, ask Claude to research real species for your region—actual harvest seasons, verified identification details, up to date safety warnings.

Replace the examples in the artifact with current foraging data for my region. Research verified harvest windows, accurate identification tips, and documented look-alikes. I want to use this in the field.

### Identify something in the field

Upload a photo and work backwards from what's in front of you.

I've attached a photo of something I've found along the trail. Based on the image and my region, what could it be? What should I check in person—gill structure, spore print, smell—to confirm? Tell me what you can and can't determine from the photo alone.

### Learn from what Claude builds—or reuse it directly

Ask Claude to walk through the logic so you understand the pattern, not just the output. Or skip the explanation and copy the code directly from the artifact as a starting point for something new. See an example that reuses this pattern to create an [interactive gardening guide(opens in new tab)](https://claude.ai/public/artifacts/0a2e112a-90e2-4219-8d3e-5bfc12d26e2c).

### Keep refining in the same conversation

Claude holds context across many exchanges, so you can iterate extensively without starting over. Add a feature, test it, notice something off, describe the issue, get a fix. This back-and-forth—sometimes dozens of rounds—is how complex tools come together. You're not bothering Claude by asking for changes; that's how the process works.

### Interactive maps work best with a data source

Claude doesn't have precise geographic boundaries memorized—state outlines, coastlines, county borders. Without a pointer to real cartographic data, it sometimes approximates with placeholder shapes instead of accurate maps. The prompt solves this by specifying a TopoJSON source (a standard format for map data). Claude fetches the real boundaries and renders them correctly. If your map looks off, check whether you've pointed to actual geographic data.

Create interactive tools with custom interfaces, tailored to how you like to explore and learn. Describe and refine your ideas with Claude to make tools useful for you.

I want to build a foraging guide for someone new to wild edibles and unsure where to start.

What it should do:

* Let users click their state on an interactive US map to see regional foraging data (fetch map data from the us-atlas TopoJSON CDN at [https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json(opens in new tab)](https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json) and render with D3's geoAlbersUsa projection)
* Browse edible plants by category and show a 12-month season bar for each species so users see harvest windows at a glance
* Let users tap any plant to expand details, then let users add plants to a personal foraging list and export a printable field guide with their selected species and safety reminders

Design: Quiet and organic. Warm cream, muted sage, soft olive. Think field journal meets editorial magazine—sophisticated but approachable. Smooth transitions, rounded corners, good type hierarchy.

Try in Claude
