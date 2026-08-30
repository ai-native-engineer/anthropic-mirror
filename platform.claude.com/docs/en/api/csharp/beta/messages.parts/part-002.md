<!-- source: https://platform.claude.com/docs/en/api/csharp/beta/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta/messages -->

<!-- chunk-start -->

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `Type? Type`

        - `class BetaToolBash20241022:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolBash20250124:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250522:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250825:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260521:`

          Code execution tool with REPL state persistence.

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaBrowserToolset20260801:`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `JsonElement Type constant`

          - `IReadOnlyList<BetaBrowserToolset20260801AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaBrowserToolsetConfigs? Configs`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `BetaBrowserCloseTabConfig? CloseTab`

              `close_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserDoubleClickConfig? DoubleClick`

              `double_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserFileUploadConfig? FileUpload`

              `file_upload`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserFindConfig? Find`

              `find`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserFormInputConfig? FormInput`

              `form_input`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserGetPageTextConfig? GetPageText`

              `get_page_text`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserHoldKeyConfig? HoldKey`

              `hold_key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserHoverConfig? Hover`

              `hover`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserJavascriptExecConfig? JavascriptExec`

              `javascript_exec`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserKeyConfig? Key`

              `key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserLeftClickConfig? LeftClick`

              `left_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserLeftClickDragConfig? LeftClickDrag`

              `left_click_drag`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserLeftMouseDownConfig? LeftMouseDown`

              `left_mouse_down`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserLeftMouseUpConfig? LeftMouseUp`

              `left_mouse_up`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserListTabsConfig? ListTabs`

              `list_tabs`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserMiddleClickConfig? MiddleClick`

              `middle_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserMouseMoveConfig? MouseMove`

              `mouse_move`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserNavigateConfig? Navigate`

              `navigate`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserNewTabConfig? NewTab`

              `new_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserReadConsoleConfig? ReadConsole`

              `read_console`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserReadNetworkConfig? ReadNetwork`

              `read_network`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserReadPageConfig? ReadPage`

              `read_page`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserRightClickConfig? RightClick`

              `right_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserScreenshotConfig? Screenshot`

              `screenshot`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserScrollConfig? Scroll`

              `scroll`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserScrollToConfig? ScrollTo`

              `scroll_to`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserSwitchTabConfig? SwitchTab`

              `switch_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserTripleClickConfig? TripleClick`

              `triple_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserTypeConfig? Type`

              `type`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserWaitConfig? Wait`

              `wait`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaBrowserZoomConfig? Zoom`

              `zoom`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class BetaToolComputerUse20241022:`

          - `required long DisplayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `required long DisplayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? DisplayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaMemoryTool20250818:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolComputerUse20250124:`

          - `required long DisplayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `required long DisplayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? DisplayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20241022:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolComputerUse20251124:`

          - `required long DisplayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `required long DisplayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? DisplayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `bool EnableZoom`

            Whether to enable an action to take a zoomed-in screenshot of the screen.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaComputerToolset20260801:`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `JsonElement Type constant`

          - `IReadOnlyList<BetaComputerToolset20260801AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaComputerToolsetConfigs? Configs`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `BetaComputerCursorPositionConfig? CursorPosition`

              `cursor_position`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerDoubleClickConfig? DoubleClick`

              `double_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerHoldKeyConfig? HoldKey`

              `hold_key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerKeyConfig? Key`

              `key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerLeftClickConfig? LeftClick`

              `left_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerLeftClickDragConfig? LeftClickDrag`

              `left_click_drag`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerLeftMouseDownConfig? LeftMouseDown`

              `left_mouse_down`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerLeftMouseUpConfig? LeftMouseUp`

              `left_mouse_up`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerMiddleClickConfig? MiddleClick`

              `middle_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerMouseMoveConfig? MouseMove`

              `mouse_move`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerRightClickConfig? RightClick`

              `right_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerScreenshotConfig? Screenshot`

              `screenshot`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerScrollConfig? Scroll`

              `scroll`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerTripleClickConfig? TripleClick`

              `triple_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerTypeConfig? Type`

              `type`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerWaitConfig? Wait`

              `wait`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BetaComputerZoomConfig? Zoom`

              `zoom`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class BetaToolTextEditor20250124:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250429:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250728:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `long? MaxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaWebSearchTool20250305:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `IReadOnlyList<string>? BlockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `BetaUserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonElement Type constant`

            - `string? City`

              The city of the user.

              maxLength: 255, minLength: 1

            - `string? Country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

              maxLength: 2, minLength: 2

            - `string? Region`

              The region of the user.

              maxLength: 255, minLength: 1

            - `string? Timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

              maxLength: 255, minLength: 1

        - `class BetaWebFetchTool20250910:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaWebSearchTool20260209:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `IReadOnlyList<string>? BlockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `BetaUserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class BetaWebFetchTool20260209:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaWebFetchTool20260309:`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `bool UseCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class BetaWebSearchTool20260318:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `IReadOnlyList<string>? BlockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion ResponseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `Full`

            - `Excluded`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `BetaUserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class BetaWebFetchTool20260318:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion ResponseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `Full`

            - `Excluded`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `bool UseCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class BetaAdvisorTool20260301:`

          - `required Model Model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCacheControlEphemeral? Caching`

            Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxTokens`

            Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

            minimum: 1024

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolSearchToolBm25_20251119:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `ToolSearchToolBm25_20251119`

            - `ToolSearchToolBm25`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolSearchToolRegex20251119:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `ToolSearchToolRegex20251119`

            - `ToolSearchToolRegex`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaMcpToolset:`

          Configuration for a group of tools from an MCP server.

          Allows configuring enabled status and defer_loading for all tools
          from an MCP server, with optional per-tool overrides.

          - `required string McpServerName`

            Name of the MCP server to configure tools for

            maxLength: 255, minLength: 1

          - `JsonElement Type constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `IReadOnlyDictionary<string, BetaMcpToolConfig>? Configs`

            Configuration overrides for specific tools, keyed by tool name

            - `bool DeferLoading`

            - `bool Enabled`

          - `BetaMcpToolDefaultConfig DefaultConfig`

            Default configuration applied to all tools from this server

            - `bool DeferLoading`

            - `bool Enabled`

      - `BetaJsonOutputFormat? OutputFormat`

        **Deprecated**

        Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

      - `double Temperature`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        maximum: 1, minimum: 0

      - `long TopK`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `double TopP`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        maximum: 1, minimum: 0

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

  - `string userProfileID`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

#### Returns

- `class BetaMessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `InProgress`

    - `Canceling`

    - `Ended`

  - `required BetaMessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Processing`

      Number of requests in the Message Batch that are processing.

    - `required long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```csharp
BatchCreateParams parameters = new()
{
    Requests =
    [
        new()
        {
            CustomID = "my-custom-id-1",
            Params = new()
            {
                MaxTokens = 1024,
                Messages =
                [
                    new()
                    {
                        Content = "Hello, world",
                        Role = Role.User,
                    },
                ],
                Model = Model.ClaudeOpus5,
                CacheControl = new() { Ttl = Ttl.Ttl5m },
                Container = new BetaContainerParams()
                {
                    ID = "id",
                    Skills =
                    [
                        new()
                        {
                            SkillID = "pdf",
                            Type = Type.Anthropic,
                            Version = "latest",
                        },
                    ],
                },
                ContextManagement = new()
                {
                    Edits =
                    [
                        new BetaClearToolUses20250919Edit()
                        {
                            ClearAtLeast = new(0),
                            ClearToolInputs = true,
                            ExcludeTools =
                            [
                                "string"
                            ],
                            Keep = new(0),
                            Trigger = new BetaInputTokensTrigger(1),
                        },
                    ],
                },
                Diagnostics = new()
                {
                    PreviousMessageID = "previous_message_id"
                },
                FallbackCreditToken = "x",
                Fallbacks = new Default(),
                InferenceGeo = "inference_geo",
                McpServers =
                [
                    new()
                    {
                        Name = "name",
                        Url = "url",
                        AuthorizationToken = "authorization_token",
                        ToolConfiguration = new()
                        {
                            AllowedTools =
                            [
                                "string"
                            ],
                            Enabled = true,
                        },
                    },
                ],
                Metadata = new()
                {
                    UserID = "13803d75-b4b5-4c3e-b2a2-6f21399b021b"
                },
                OutputConfig = new()
                {
                    Effort = Effort.Low,
                    Format = new()
                    {
                        Schema = new Dictionary<string, JsonElement>()
                        {
                            { "foo", JsonSerializer.SerializeToElement("bar") }
                        },
                    },
                    TaskBudget = new()
                    {
                        Total = 1024,
                        Remaining = 0,
                    },
                },
                OutputFormat = new()
                {
                    Schema = new Dictionary<string, JsonElement>()
                    {
                        { "foo", JsonSerializer.SerializeToElement("bar") }
                    },
                },
                ServiceTier = ServiceTier.Auto,
                Speed = Speed.Standard,
                StopSequences =
                [
                    "string"
                ],
                Stream = false,
                System = new(

                    [
                        new BetaTextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new BetaCitationCharLocationParam()
                                {
                                    CitedText = "The grass is green. The sky is blue.",
                                    DocumentIndex = 0,
                                    DocumentTitle = "x",
                                    EndCharIndex = 0,
                                    StartCharIndex = 0,
                                },
                            ],
                        },
                    ]
                ),
                Temperature = 1,
                Thinking = new BetaThinkingConfigAdaptive()
                {
                    Display = Display.Summarized
                },
                ToolChoice = new BetaToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new BetaTool()
                    {
                        InputSchema = new()
                        {
                            Properties = new Dictionary<string, JsonElement>()
                            {
                                { "location", JsonSerializer.SerializeToElement("bar") },
                                { "unit", JsonSerializer.SerializeToElement("bar") },
                            },
                            Required =
                            [
                                "location"
                            ],
                        },
                        Name = "name",
                        AllowedCallers =
                        [
                            AllowedCaller.Direct
                        ],
                        CacheControl = new() { Ttl = Ttl.Ttl5m },
                        DeferLoading = true,
                        Description = "Get the current weather in a given location",
                        EagerInputStreaming = true,
                        InputExamples =
                        [
                            new Dictionary<string, JsonElement>()
                            {
                                { "foo", JsonSerializer.SerializeToElement("bar") },
                            },
                        ],
                        Strict = true,
                        Type = Type.Custom,
                    },
                ],
                TopK = 5,
                TopP = 0.7,
            },
        },
    ],
};

var betaMessageBatch = await client.Beta.Messages.Batches.Create(parameters);

Console.WriteLine(betaMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

### Retrieve a Message Batch

`BetaMessageBatch Beta.Messages.Batches.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchRetrieveParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaMessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `InProgress`

    - `Canceling`

    - `Ended`

  - `required BetaMessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Processing`

      Number of requests in the Message Batch that are processing.

    - `required long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```csharp
BatchRetrieveParams parameters = new() { MessageBatchID = "message_batch_id" };

var betaMessageBatch = await client.Beta.Messages.Batches.Retrieve(parameters);

Console.WriteLine(betaMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

### List Message Batches

`BatchListPage Beta.Messages.Batches.List(parameters, cancellationToken = default)`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaMessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `InProgress`

    - `Canceling`

    - `Ended`

  - `required BetaMessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Processing`

      Number of requests in the Message Batch that are processing.

    - `required long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```csharp
BatchListParams parameters = new();

var page = await client.Beta.Messages.Batches.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Cancel a Message Batch

`BetaMessageBatch Beta.Messages.Batches.Cancel(parameters, cancellationToken = default)`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchCancelParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaMessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `InProgress`

    - `Canceling`

    - `Ended`

  - `required BetaMessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Processing`

      Number of requests in the Message Batch that are processing.

    - `required long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```csharp
BatchCancelParams parameters = new() { MessageBatchID = "message_batch_id" };

var betaMessageBatch = await client.Beta.Messages.Batches.Cancel(parameters);

Console.WriteLine(betaMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

### Delete a Message Batch

`BetaDeletedMessageBatch Beta.Messages.Batches.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchDeleteParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDeletedMessageBatch:`

  - `required string ID`

    ID of the Message Batch.

  - `JsonElement Type constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

#### Example

```csharp
BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var betaDeletedMessageBatch = await client.Beta.Messages.Batches.Delete(parameters);

Console.WriteLine(betaDeletedMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`BetaMessageBatchIndividualResponse Beta.Messages.Batches.ResultsStreaming(parameters, cancellationToken = default)`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchResultsParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaMessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `required string CustomID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `required BetaMessageBatchResult Result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class BetaMessageBatchSucceededResult:`

      - `required BetaMessage Message`

        - `required string ID`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `required BetaContainer? Container`

          Information about the container used in the request (for the code execution tool)

          - `required string ID`

            Identifier for the container used in this request

          - `required DateTimeOffset ExpiresAt`

            The time at which the container will expire.

            format: date-time

          - `required IReadOnlyList<BetaContainerSkill>? Skills`

            Skills loaded in the container

            - `required string SkillID`

              Skill ID

              maxLength: 64, minLength: 1

            - `required Type Type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `Anthropic`

              - `Custom`

            - `required string Version`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `required IReadOnlyList<BetaContentBlock> Content`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `class BetaTextBlock:`

            - `required IReadOnlyList<BetaTextCitation>? Citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class BetaCitationCharLocation:`

                - `required string CitedText`

                - `required long DocumentIndex`

                  minimum: 0

                - `required string? DocumentTitle`

                - `required long EndCharIndex`

                - `required string? FileID`

                - `required long StartCharIndex`

                  minimum: 0

                - `JsonElement Type constant`

              - `class BetaCitationPageLocation:`

                - `required string CitedText`

                - `required long DocumentIndex`

                  minimum: 0

                - `required string? DocumentTitle`

                - `required long EndPageNumber`

                - `required string? FileID`

                - `required long StartPageNumber`

                  minimum: 1

                - `JsonElement Type constant`

              - `class BetaCitationContentBlockLocation:`

                - `required string CitedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `required long DocumentIndex`

                  minimum: 0

                - `required string? DocumentTitle`

                - `required long EndBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `required string? FileID`

                - `required long StartBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `JsonElement Type constant`

              - `class BetaCitationsWebSearchResultLocation:`

                - `required string CitedText`

                - `required string EncryptedIndex`

                - `required string? Title`

                  maxLength: 512

                - `JsonElement Type constant`

                - `required string Url`

              - `class BetaCitationSearchResultLocation:`

                - `required string CitedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `required long EndBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `required long SearchResultIndex`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `required string Source`

                - `required long StartBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `required string? Title`

                - `JsonElement Type constant`

            - `required string Text`

              maxLength: 5000000, minLength: 0

            - `JsonElement Type constant`

          - `class BetaThinkingBlock:`

            - `required string Signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `required string Thinking`

              The text of Claude's thinking process for this block.

            - `JsonElement Type constant`

          - `class BetaRedactedThinkingBlock:`

            - `required string Data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `JsonElement Type constant`

          - `class BetaToolUseBlock:`

            - `required string ID`

              pattern: ^[a-zA-Z0-9_-]+$

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required string Name`

              minLength: 1

            - `JsonElement Type constant`

            - `Caller Caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type constant`

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonElement Type constant`

              - `class BetaServerToolCaller20260120:`

                - `required string ToolID`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonElement Type constant`

            - `string? ToolsetName`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlock:`

            - `required string ID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required Name Name`

              - `Advisor`

              - `WebSearch`

              - `WebFetch`

              - `CodeExecution`

              - `BashCodeExecution`

              - `TextEditorCodeExecution`

              - `ToolSearchToolRegex`

              - `ToolSearchToolBm25`

            - `JsonElement Type constant`

            - `Caller Caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebSearchToolResultBlock:`

            - `required BetaWebSearchToolResultBlockContent Content`

              - `class BetaWebSearchToolResultError:`

                - `required BetaWebSearchToolResultErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `Unavailable`

                  - `MaxUsesExceeded`

                  - `TooManyRequests`

                  - `QueryTooLong`

                  - `RequestTooLarge`

                - `JsonElement Type constant`

              - `IReadOnlyList<BetaWebSearchResultBlock>`

                - `required string EncryptedContent`

                - `required string? PageAge`

                - `required string Title`

                - `JsonElement Type constant`

                - `required string Url`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

            - `Caller Caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebFetchToolResultBlock:`

            - `required Content Content`

              - `class BetaWebFetchToolResultErrorBlock:`

                - `required BetaWebFetchToolResultErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `UrlTooLong`

                  - `UrlNotAllowed`

                  - `UrlNotInPriorContext`

                  - `UrlNotAccessible`

                  - `UnsupportedContentType`

                  - `TooManyRequests`

                  - `MaxUsesExceeded`

                  - `Unavailable`

                - `JsonElement Type constant`

              - `class BetaWebFetchBlock:`

                - `required BetaDocumentBlock Content`

                  - `required BetaCitationConfig? Citations`

                    Citation configuration for the document

                    - `required bool Enabled`

                  - `required Source Source`

                    - `class BetaBase64PdfSource:`

                      - `required string Data`

                        format: byte

                      - `JsonElement MediaType constant`

                      - `JsonElement Type constant`

                    - `class BetaPlainTextSource:`

                      - `required string Data`

                      - `JsonElement MediaType constant`

                      - `JsonElement Type constant`

                  - `required string? Title`

                    The title of the document

                  - `JsonElement Type constant`

                - `required string? RetrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonElement Type constant`

                - `required string Url`

                  Fetched content URL

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

            - `Caller Caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaAdvisorToolResultBlock:`

            - `required Content Content`

              - `class BetaAdvisorToolResultError:`

                - `required ErrorCode ErrorCode`

                  - `MaxUsesExceeded`

                  - `PromptTooLong`

                  - `TooManyRequests`

                  - `Overloaded`

                  - `Unavailable`

                  - `ExecutionTimeExceeded`

                  - `ModelNotFound`

                - `JsonElement Type constant`

              - `class BetaAdvisorResultBlock:`

                - `required string? StopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `required string Text`

                - `JsonElement Type constant`

              - `class BetaAdvisorRedactedResultBlock:`

                - `required string EncryptedContent`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `required string? StopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `JsonElement Type constant`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

          - `class BetaCodeExecutionToolResultBlock:`

            - `required BetaCodeExecutionToolResultBlockContent Content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class BetaCodeExecutionToolResultError:`

                - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `Unavailable`

                  - `TooManyRequests`

                  - `ExecutionTimeExceeded`

                - `JsonElement Type constant`

              - `class BetaCodeExecutionResultBlock:`

                - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type constant`

                - `required long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type constant`

              - `class BetaEncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type constant`

                - `required string EncryptedStdout`

                - `required long ReturnCode`

                - `required string Stderr`

                - `JsonElement Type constant`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

          - `class BetaBashCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class BetaBashCodeExecutionToolResultError:`

                - `required ErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `Unavailable`

                  - `TooManyRequests`

                  - `ExecutionTimeExceeded`

                  - `OutputFileTooLarge`

                - `JsonElement Type constant`

              - `class BetaBashCodeExecutionResultBlock:`

                - `required IReadOnlyList<BetaBashCodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type constant`

                - `required long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type constant`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

          - `class BetaTextEditorCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class BetaTextEditorCodeExecutionToolResultError:`

                - `required ErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `Unavailable`

                  - `TooManyRequests`

                  - `ExecutionTimeExceeded`

                  - `FileNotFound`

                - `required string? ErrorMessage`

                - `JsonElement Type constant`

              - `class BetaTextEditorCodeExecutionViewResultBlock:`

                - `required string Content`

                - `required FileType FileType`

                  - `Text`

                  - `Image`

                  - `Pdf`

                - `required long? NumLines`

                - `required long? StartLine`

                - `required long? TotalLines`

                - `JsonElement Type constant`

              - `class BetaTextEditorCodeExecutionCreateResultBlock:`

                - `required bool IsFileUpdate`

                - `JsonElement Type constant`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

                - `required IReadOnlyList<string>? Lines`

                - `required long? NewLines`

                - `required long? NewStart`

                - `required long? OldLines`

                - `required long? OldStart`

                - `JsonElement Type constant`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

          - `class BetaToolSearchToolResultBlock:`

            - `required Content Content`

              - `class BetaToolSearchToolResultError:`

                - `required ErrorCode ErrorCode`

                  - `InvalidToolInput`

                  - `Unavailable`

                  - `TooManyRequests`

                  - `ExecutionTimeExceeded`

                - `required string? ErrorMessage`

                - `JsonElement Type constant`

              - `class BetaToolSearchToolSearchResultBlock:`

                - `required IReadOnlyList<BetaToolReferenceBlock> ToolReferences`

                  - `required string ToolName`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `JsonElement Type constant`

                - `JsonElement Type constant`

            - `required string ToolUseID`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonElement Type constant`

          - `class BetaMcpToolUseBlock:`

            - `required string ID`

              pattern: ^[a-zA-Z0-9_-]+$

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required string Name`

              The name of the MCP tool

            - `required string ServerName`

              The name of the MCP server

            - `JsonElement Type constant`

          - `class BetaMcpToolResultBlock:`

            - `required Content Content`

              - `string`

              - `IReadOnlyList<BetaTextBlock>`

                - `required IReadOnlyList<BetaTextCitation>? Citations`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `required string Text`

                  maxLength: 5000000, minLength: 0

                - `JsonElement Type constant`

            - `required bool IsError`

            - `required string ToolUseID`

              pattern: ^[a-zA-Z0-9_-]+$

            - `JsonElement Type constant`

          - `class BetaContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `required string FileID`

            - `JsonElement Type constant`

          - `class BetaCompactionBlock:`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `required string? Content`

              Summary of compacted content, or null if compaction failed

            - `required string? EncryptedContent`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `JsonElement Type constant`

          - `class BetaFallbackBlock:`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `required BetaFallbackInfo From`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `required Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `ClaudeSonnet5`

                  High-performance model for coding and agents

                - `ClaudeFable5`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `ClaudeMythos5`

                  Most capable model for cybersecurity and biology research

                - `ClaudeOpus5`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeOpus4_8`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeOpus4_7`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeMythosPreview`

                  New class of intelligence, strongest in coding and cybersecurity

                - `ClaudeOpus4_6`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeSonnet4_6`

                  Best combination of speed and intelligence

                - `ClaudeHaiku4_5`

                  Fastest model with near-frontier intelligence

                - `ClaudeHaiku4_5_20251001`

                  Fastest model with near-frontier intelligence

                - `ClaudeOpus4_5`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeOpus4_5_20251101`

                  Powerful intelligence for long-running agents and coding

                - `ClaudeSonnet4_5`

                  High-performance model for agents and coding

                - `ClaudeSonnet4_5_20250929`

                  High-performance model for agents and coding

            - `required BetaFallbackInfo To`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `required BetaFallbackRefusalTrigger Trigger`

              What caused the `from` model to hand over at this hop.

              - `required BetaFallbackRefusalTriggerCategory? Category`

                The policy category that triggered a refusal.

                - `Cyber`

                  The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

                - `Bio`

                  The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

                - `FrontierLlm`

                  The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

                - `ReasoningExtraction`

                  The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

                - `GeneralHarms`

                  The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

              - `JsonElement Type constant`

            - `JsonElement Type constant`

        - `required BetaContextManagementResponse? ContextManagement`

          Context management response.

          Information about context management strategies applied during the request.

          - `required IReadOnlyList<AppliedEdit> AppliedEdits`

            List of context management edits that were applied.

            - `class BetaClearToolUses20250919EditResponse:`

              - `required long ClearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `required long ClearedToolUses`

                Number of tool uses that were cleared.

                minimum: 0

              - `JsonElement Type constant`

                The type of context management edit applied.

            - `class BetaClearThinking20251015EditResponse:`

              - `required long ClearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `required long ClearedThinkingTurns`

                Number of thinking turns that were cleared.

                minimum: 0

              - `JsonElement Type constant`

                The type of context management edit applied.

        - `required BetaDiagnostics? Diagnostics`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `required CacheMissReason? CacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class BetaCacheMissModelChanged:`

              - `required long CacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonElement Type constant`

            - `class BetaCacheMissSystemChanged:`

              - `required long CacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonElement Type constant`

            - `class BetaCacheMissToolsChanged:`

              - `required long CacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonElement Type constant`

            - `class BetaCacheMissMessagesChanged:`

              - `required long CacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonElement Type constant`

            - `class BetaCacheMissPreviousMessageNotFound:`

              - `JsonElement Type constant`

            - `class BetaCacheMissUnavailable:`

              - `JsonElement Type constant`

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `JsonElement Role constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `required BetaRefusalStopDetails? StopDetails`

          Structured information about a refusal.

          - `required Category? Category`

            The policy category that triggered a refusal.

            - `Cyber`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `Bio`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `FrontierLlm`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `ReasoningExtraction`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `GeneralHarms`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `required string? Explanation`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `required string? FallbackCreditToken`

            Opaque code that refunds the cache-miss cost when retrying this refused
            request on the fallback model. Pass it as `fallback_credit_token` on the
            retry request. Expires 5 minutes after the refusal.

            The retry is sent either with the same request body (`system`, `messages`,
            `tools`, and other render-shaping fields), or with the same body plus one
            appended `assistant` message whose content is the partial text (with any
            trailing whitespace stripped from the final text block) and paired
            server-tool blocks from this refusal — which also authorizes that
            appended turn as an assistant-prefill continuation on models that otherwise
            disallow prefill. A token minted mid-server-tool-loop whose partial content
            was continuable may only be redeemed the second way — if a same-body retry
            is rejected with a 400 saying the token must be redeemed by continuing the
            partial response, retry the second way instead. Either way: same workspace,
            same platform; a mismatch is a 400. Resending a token for an already-warm
            prefix is permitted but yields no additional credit.

            `null` when the refused model isn't eligible for a fallback credit.

          - `required bool? FallbackHasPrefillClaim`

            Whether the accompanying `fallback_credit_token` may be redeemed with the
            appended-assistant retry form. Only set when `fallback_credit_token` is
            present.

            `true`: retry by resending the same request body plus one appended
            `assistant` message whose content is this response's `content` with any
            trailing whitespace stripped from the final text block and unpaired
            `tool_use` blocks omitted (the same appended-turn shape described on
            `fallback_credit_token`), with the token attached. `false`: retry by
            resending the original request body unchanged, with the token attached —
            the appended-assistant form is not available for this refusal (no
            continuable partial content, or the request uses `output_format` or a
            `tool_choice` that forces tool use). One exception: when the request used
            `output_format` or a forced `tool_choice` and the refusal arrived after
            server tools (including MCP connector tools) had already executed, the
            token may not be redeemable by either retry form; if the exact-body retry
            is then rejected with a 400 saying the token must be redeemed by
            continuing the partial response, discard the token and retry without it.

            Advisory: if an appended-assistant retry is rejected with a 400 despite
            `true`, fall back to resending the original request body with the token.

          - `required string? RecommendedModel`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `JsonElement Type constant`

        - `required BetaStopReason? StopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `EndTurn`

          - `MaxTokens`

          - `StopSequence`

          - `ToolUse`

          - `PauseTurn`

          - `Compaction`

          - `Refusal`

          - `ModelContextWindowExceeded`

        - `required string? StopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonElement Type constant`

          Object type.

          For Messages, this is always `"message"`.

        - `required BetaUsage Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `required BetaCacheCreation? CacheCreation`

            Breakdown of cached tokens by TTL

            - `required long Ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `required long Ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `required long? CacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `required long? CacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `required BetaFallbackCreditUsage? FallbackCredit`

            Outcome of the `fallback_credit_token` presented on this request.

            - `required Status Status`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `class BetaFallbackCreditRedeemed:`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `JsonElement Type constant`

              - `class BetaFallbackCreditNotApplied:`

                No reprice was applied; `reason` says why.

                - `required Reason Reason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `BodyMismatch`

                  - `ContinuationExcluded`

                  - `ContinuationOnly`

                  - `Expired`

                  - `InvalidTargetModel`

                  - `NotEnabled`

                  - `RepriceUnavailable`

                  - `TemporarilyUnavailable`

                  - `VariantFieldsPresent`

                  - `WrongOrganization`

                  - `WrongPlatform`

                  - `WrongWorkspace`

                - `JsonElement Type constant`

                - `IReadOnlyList<string>? RemoveToRedeem`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `required string? InferenceGeo`

            The geographic region where inference was performed for this request.

          - `required long InputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `required IReadOnlyList<Iteration>? Iterations`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `class BetaMessageIterationUsage:`

              Token usage for a sampling iteration.

              - `required BetaCacheCreation? CacheCreation`

                Breakdown of cached tokens by TTL

              - `required long CacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `required long CacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `required long InputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `required Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `required long OutputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonElement Type constant`

                Usage for a sampling iteration

            - `class BetaCompactionIterationUsage:`

              Token usage for a compaction iteration.

              - `required BetaCacheCreation? CacheCreation`

                Breakdown of cached tokens by TTL

              - `required long CacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `required long CacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `required long InputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `required long OutputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonElement Type constant`

                Usage for a compaction iteration

            - `class BetaAdvisorMessageIterationUsage:`

              Token usage for an advisor sub-inference iteration.

              - `required BetaCacheCreation? CacheCreation`

                Breakdown of cached tokens by TTL

              - `required long CacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `required long CacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `required long InputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `required Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `required long OutputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonElement Type constant`

                Usage for an advisor sub-inference iteration

            - `class BetaFallbackMessageIterationUsage:`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `required BetaCacheCreation? CacheCreation`

                Breakdown of cached tokens by TTL

              - `required long CacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `required long CacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `required long InputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `required Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `required long OutputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonElement Type constant`

                Usage for the fallback-model attempt that served the response

          - `required long OutputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `required BetaOutputTokensDetails? OutputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `required long ThinkingTokens`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `required BetaServerToolUsage? ServerToolUse`

            The number of server tool requests.

            - `required long WebFetchRequests`

              The number of web fetch tool requests.

              minimum: 0

            - `required long WebSearchRequests`

              The number of web search tool requests.

              minimum: 0

          - `required ServiceTier? ServiceTier`

            If the request used the priority, standard, or batch tier.

            - `Standard`

            - `Priority`

            - `Batch`

          - `required Speed? Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `Standard`

            - `Fast`

      - `JsonElement Type constant`

    - `class BetaMessageBatchErroredResult:`

      - `required BetaErrorResponse Error`

        - `required BetaError Error`

          - `class BetaInvalidRequestError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaAuthenticationError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaBillingError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaPermissionError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaNotFoundError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaRateLimitError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaGatewayTimeoutError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaApiError:`

            - `required string Message`

            - `JsonElement Type constant`

          - `class BetaOverloadedError:`

            - `required string Message`

            - `JsonElement Type constant`

        - `required string? RequestID`

        - `JsonElement Type constant`

      - `JsonElement Type constant`

    - `class BetaMessageBatchCanceledResult:`

      - `JsonElement Type constant`

    - `class BetaMessageBatchExpiredResult:`

      - `JsonElement Type constant`

#### Example

```csharp
BatchResultsParams parameters = new() { MessageBatchID = "message_batch_id" };

await foreach (var betaMessageBatchIndividualResponse in client.Beta.Messages.Batches.ResultsStreaming(parameters))
{
    Console.WriteLine(betaMessageBatchIndividualResponse);
}
```
