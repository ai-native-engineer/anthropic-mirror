<!-- source: https://platform.claude.com/docs/en/api/java/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/java/messages -->

<!-- chunk-start -->

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserReadPageConfig> readPage`

              `read_page`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScrollToConfig> scrollTo`

              `scroll_to`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserSwitchTabConfig> switchTab`

              `switch_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class MemoryTool20250818`

          - `JsonValue type = "memory_20250818"`

          - `JsonValue name = "memory"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ComputerToolset20260801`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `JsonValue type = "computer_toolset_20260801"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<ComputerToolsetConfigs> configs`

            Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

            - `Optional<ComputerTypeConfig> type`

              `type`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerCursorPositionConfig> cursorPosition`

              `cursor_position`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerDoubleClickConfig> doubleClick`

              `double_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerHoldKeyConfig> holdKey`

              `hold_key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerKeyConfig> key`

              `key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftClickConfig> leftClick`

              `left_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

              `left_click_drag`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

              `left_mouse_down`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

              `left_mouse_up`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerMiddleClickConfig> middleClick`

              `middle_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerMouseMoveConfig> mouseMove`

              `mouse_move`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class ToolTextEditor20250124`

          - `JsonValue type = "text_editor_20250124"`

          - `JsonValue name = "str_replace_editor"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250429`

          - `JsonValue type = "text_editor_20250429"`

          - `JsonValue name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250728`

          - `JsonValue type = "text_editor_20250728"`

          - `JsonValue name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Long> maxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20250305`

          - `JsonValue type = "web_search_20250305"`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonValue type = "approximate"`

            - `Optional<String> city`

              The city of the user.

              minLength: 1, maxLength: 255

            - `Optional<String> country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

              minLength: 2, maxLength: 2

            - `Optional<String> region`

              The region of the user.

              minLength: 1, maxLength: 255

            - `Optional<String> timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

              minLength: 1, maxLength: 255

        - `class WebFetchTool20250910`

          - `JsonValue type = "web_fetch_20250910"`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            minimum: 1

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<WebFetchUrlSources> urlSources`

            Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

            - `Optional<ClientToolResults> clientToolResults`

              Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

              - `class WebFetchUrlSourceAll`

                The `url_sources` variant under which a source contributes in
                full: every result of the tool filter's source, or all user input.

                - `JsonValue type = "all"`

              - `class WebFetchUrlSourceNone`

                The `url_sources` variant under which a source contributes nothing:
                no result of the tool filter's source, or no user input.

                - `JsonValue type = "none"`

              - `class WebFetchUrlSourceOnly`

                The tool filter variant under which only the named tools' results
                contribute.

                - `JsonValue type = "only"`

                - `List<WebFetchUrlSourceToolReference> tools`

                  - `JsonValue type = "tool_reference"`

                  - `String name`

              - `class WebFetchUrlSourceExcept`

                The tool filter variant under which every result but the named
                tools' contributes.

                - `JsonValue type = "except"`

                - `List<WebFetchUrlSourceToolReference> tools`

                  - `JsonValue type = "tool_reference"`

                  - `String name`

            - `Optional<ServerToolResults> serverToolResults`

              Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

              - `class WebFetchUrlSourceAll`

                The `url_sources` variant under which a source contributes in
                full: every result of the tool filter's source, or all user input.

              - `class WebFetchUrlSourceNone`

                The `url_sources` variant under which a source contributes nothing:
                no result of the tool filter's source, or no user input.

              - `class WebFetchUrlSourceOnly`

                The tool filter variant under which only the named tools' results
                contribute.

              - `class WebFetchUrlSourceExcept`

                The tool filter variant under which every result but the named
                tools' contributes.

            - `Optional<UserInput> userInput`

              Whether URLs in user messages are fetchable: "all" or "none".

              - `class WebFetchUrlSourceAll`

                The `url_sources` variant under which a source contributes in
                full: every result of the tool filter's source, or all user input.

              - `class WebFetchUrlSourceNone`

                The `url_sources` variant under which a source contributes nothing:
                no result of the tool filter's source, or no user input.

        - `class WebSearchTool20260209`

          - `JsonValue type = "web_search_20260209"`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260209`

          - `JsonValue type = "web_fetch_20260209"`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            minimum: 1

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<WebFetchUrlSources> urlSources`

            Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

        - `class WebFetchTool20260309`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `JsonValue type = "web_fetch_20260309"`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            minimum: 1

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<WebFetchUrlSources> urlSources`

            Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

          - `Optional<Boolean> useCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class WebSearchTool20260318`

          - `JsonValue type = "web_search_20260318"`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<ResponseInclusion> responseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `FULL("full")`

            - `EXCLUDED("excluded")`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260318`

          - `JsonValue type = "web_fetch_20260318"`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            minimum: 1

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            minimum: 1

          - `Optional<ResponseInclusion> responseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `FULL("full")`

            - `EXCLUDED("excluded")`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<WebFetchUrlSources> urlSources`

            Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

          - `Optional<Boolean> useCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class ToolSearchToolBm25_20251119`

          - `Type type`

            - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue name = "tool_search_tool_bm25"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolRegex20251119`

          - `Type type`

            - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `JsonValue name = "tool_search_tool_regex"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

      - `Optional<Double> temperature`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        minimum: 0, maximum: 1

      - `Optional<Long> topK`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `Optional<Double> topP`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        minimum: 0, maximum: 1

#### Returns

- `class MessageBatch`

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.batches.BatchCreateParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .addRequest(BatchCreateParams.Request.builder()
                .customId("my-custom-id-1")
                .params(BatchCreateParams.Request.Params.builder()
                    .maxTokens(1024L)
                    .addUserMessage("Hello, world")
                    .model(Model.CLAUDE_OPUS_5)
                    .build())
                .build())
            .build();
        MessageBatch messageBatch = client.messages().batches().create(params);
    }
}
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

`MessageBatch messages().batches().retrieve(params = BatchRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchRetrieveParams params`

  - `Optional<String> messageBatchId` (path parameter)

    ID of the Message Batch.

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchRetrieveParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().retrieve("message_batch_id");
    }
}
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

`BatchListPage messages().batches().list(params = BatchListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchListParams params`

  - `Optional<String> afterId` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit` (query parameter)

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.BatchListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchListPage page = client.messages().batches().list();
    }
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

`MessageBatch messages().batches().cancel(params = BatchCancelParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchCancelParams params`

  - `Optional<String> messageBatchId` (path parameter)

    ID of the Message Batch.

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchCancelParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().cancel("message_batch_id");
    }
}
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

`DeletedMessageBatch messages().batches().delete(params = BatchDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchDeleteParams params`

  - `Optional<String> messageBatchId` (path parameter)

    ID of the Message Batch.

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class DeletedMessageBatch`

  - `JsonValue type = "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `String id`

    ID of the Message Batch.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchDeleteParams;
import com.anthropic.models.messages.batches.DeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeletedMessageBatch deletedMessageBatch = client.messages().batches().delete("message_batch_id");
    }
}
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`MessageBatchIndividualResponse messages().batches().resultsStreaming(params = BatchResultsParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchResultsParams params`

  - `Optional<String> messageBatchId` (path parameter)

    ID of the Message Batch.

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatchIndividualResponse`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult`

      - `JsonValue type = "succeeded"`

      - `Message message`

        - `JsonValue type = "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<Container> container`

          Information about the container used in this request.

          This will be non-null if a container tool (e.g. code execution) was used.

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<ContainerSkill>> skills`

            Skills loaded in the container

            - `Type type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `ANTHROPIC("anthropic")`

              - `CUSTOM("custom")`

            - `String skillId`

              Skill ID

              minLength: 1, maxLength: 64

            - `String version`

              The resolved version: a skill version ID for custom skills.

              minLength: 1, maxLength: 64

        - `List<ContentBlock> content`

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

          - `class TextBlock`

            - `JsonValue type = "text"`

            - `Optional<List<TextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation`

                - `JsonValue type = "char_location"`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

              - `class CitationPageLocation`

                - `JsonValue type = "page_location"`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

              - `class CitationContentBlockLocation`

                - `JsonValue type = "content_block_location"`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `Optional<String> fileId`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

              - `class CitationsWebSearchResultLocation`

                - `JsonValue type = "web_search_result_location"`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `String url`

              - `class CitationsSearchResultLocation`

                - `JsonValue type = "search_result_location"`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `long searchResultIndex`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `String source`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Optional<String> title`

            - `String text`

          - `class ThinkingBlock`

            - `JsonValue type = "thinking"`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

          - `class RedactedThinkingBlock`

            - `JsonValue type = "redacted_thinking"`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `class ToolUseBlock`

            - `JsonValue type = "tool_use"`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Caller caller`

              - `class DirectCaller`

                Tool invocation directly from the model.

                - `JsonValue type = "direct"`

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `JsonValue type = "code_execution_20250825"`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `class ServerToolCaller20260120`

                - `JsonValue type = "code_execution_20260120"`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Input input`

            - `String name`

              minLength: 1

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$

          - `class ServerToolUseBlock`

            - `JsonValue type = "server_tool_use"`

            - `String id`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Caller caller`

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

            - `Input input`

            - `Name name`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `class WebSearchToolResultBlock`

            - `JsonValue type = "web_search_tool_result"`

            - `Caller caller`

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

            - `WebSearchToolResultBlockContent content`

              - `class WebSearchToolResultError`

                - `JsonValue type = "web_search_tool_result_error"`

                - `WebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

              - `List<WebSearchResultBlock>`

                - `JsonValue type = "web_search_result"`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class WebFetchToolResultBlock`

            - `JsonValue type = "web_fetch_tool_result"`

            - `Caller caller`

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

            - `Content content`

              - `class WebFetchToolResultErrorBlock`

                - `JsonValue type = "web_fetch_tool_result_error"`

                - `WebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                  - `CONTENT_TOO_LARGE("content_too_large")`

              - `class WebFetchBlock`

                - `JsonValue type = "web_fetch_result"`

                - `DocumentBlock content`

                  - `JsonValue type = "document"`

                  - `Optional<CitationsConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class Base64PdfSource`

                      - `JsonValue type = "base64"`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType = "application/pdf"`

                    - `class PlainTextSource`

                      - `JsonValue type = "text"`

                      - `String data`

                      - `JsonValue mediaType = "text/plain"`

                  - `Optional<String> title`

                    The title of the document

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class CodeExecutionToolResultBlock`

            - `JsonValue type = "code_execution_tool_result"`

            - `CodeExecutionToolResultBlockContent content`

              - `class CodeExecutionToolResultError`

                - `JsonValue type = "code_execution_tool_result_error"`

                - `CodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `class CodeExecutionResultBlock`

                - `JsonValue type = "code_execution_result"`

                - `List<CodeExecutionOutputBlock> content`

                  - `JsonValue type = "code_execution_output"`

                  - `String fileId`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

              - `class EncryptedCodeExecutionResultBlock`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `JsonValue type = "encrypted_code_execution_result"`

                - `List<CodeExecutionOutputBlock> content`

                  - `JsonValue type = "code_execution_output"`

                  - `String fileId`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BashCodeExecutionToolResultBlock`

            - `JsonValue type = "bash_code_execution_tool_result"`

            - `Content content`

              - `class BashCodeExecutionToolResultError`

                - `JsonValue type = "bash_code_execution_tool_result_error"`

                - `BashCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `class BashCodeExecutionResultBlock`

                - `JsonValue type = "bash_code_execution_result"`

                - `List<BashCodeExecutionOutputBlock> content`

                  - `JsonValue type = "bash_code_execution_output"`

                  - `String fileId`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class TextEditorCodeExecutionToolResultBlock`

            - `JsonValue type = "text_editor_code_execution_tool_result"`

            - `Content content`

              - `class TextEditorCodeExecutionToolResultError`

                - `JsonValue type = "text_editor_code_execution_tool_result_error"`

                - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

              - `class TextEditorCodeExecutionViewResultBlock`

                - `JsonValue type = "text_editor_code_execution_view_result"`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

              - `class TextEditorCodeExecutionCreateResultBlock`

                - `JsonValue type = "text_editor_code_execution_create_result"`

                - `boolean isFileUpdate`

              - `class TextEditorCodeExecutionStrReplaceResultBlock`

                - `JsonValue type = "text_editor_code_execution_str_replace_result"`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class ToolSearchToolResultBlock`

            - `JsonValue type = "tool_search_tool_result"`

            - `Content content`

              - `class ToolSearchToolResultError`

                - `JsonValue type = "tool_search_tool_result_error"`

                - `ToolSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

              - `class ToolSearchToolSearchResultBlock`

                - `JsonValue type = "tool_search_tool_search_result"`

                - `List<ToolReferenceBlock> toolReferences`

                  - `JsonValue type = "tool_reference"`

                  - `String toolName`

                    minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class ContainerUploadBlock`

            Response model for a file uploaded to the container.

            - `JsonValue type = "container_upload"`

            - `String fileId`

        - `Optional<Diagnostics> diagnostics`

          Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected.

          - `Optional<CacheMissReason> cacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class CacheMissModelChanged`

              - `JsonValue type = "model_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class CacheMissSystemChanged`

              - `JsonValue type = "system_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class CacheMissToolsChanged`

              - `JsonValue type = "tools_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class CacheMissMessagesChanged`

              - `JsonValue type = "messages_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class CacheMissPreviousMessageNotFound`

              - `JsonValue type = "previous_message_not_found"`

            - `class CacheMissUnavailable`

              - `JsonValue type = "unavailable"`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_HAIKU_5_5("claude-haiku-5-5")`

            Fastest model for high-volume, real-time tasks

          - `CLAUDE_SONNET_5_5("claude-sonnet-5-5")`

            Efficient model for coding and agents

          - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `CLAUDE_OPUS_5_5("claude-opus-5-5")`

            Powerful intelligence for coding, knowledge work, and long-running agents

          - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

            Our most capable model for cybersecurity and biology research, available through trusted access programs

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            Efficient model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_MYTHOS_5("claude-mythos-5")`

            Most capable model for cybersecurity and biology research

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

            **Deprecated**: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            New class of intelligence, strongest in coding and cybersecurity

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

        - `JsonValue role = "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<RefusalStopDetails> stopDetails`

          Structured information about why model output stopped.

          This is `null` when the `stop_reason` has no additional detail to report.

          - `JsonValue type = "refusal"`

          - `Optional<Category> category`

            The policy category that triggered the refusal.

            `null` when the refusal doesn't map to a named category.

            - `CYBER("cyber")`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `BIO("bio")`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `FRONTIER_LLM("frontier_llm")`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `REASONING_EXTRACTION("reasoning_extraction")`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `GENERAL_HARMS("general_harms")`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `Optional<String> explanation`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `Optional<StopReason> stopReason`

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

          - `END_TURN("end_turn")`

          - `MAX_TOKENS("max_tokens")`

          - `STOP_SEQUENCE("stop_sequence")`

          - `TOOL_USE("tool_use")`

          - `PAUSE_TURN("pause_turn")`

          - `REFUSAL("refusal")`

          - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `Usage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<CacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

            - `long ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `long ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `Optional<Long> cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `Optional<Long> cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `Optional<OutputTokensDetails> outputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `long thinkingTokens`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `Optional<ServerToolUsage> serverToolUse`

            The number of server tool requests.

            - `long webFetchRequests`

              The number of web fetch tool requests.

              minimum: 0

            - `long webSearchRequests`

              The number of web search tool requests.

              minimum: 0

          - `Optional<ServiceTier> serviceTier`

            If the request used the priority, standard, or batch tier.

            - `STANDARD("standard")`

            - `PRIORITY("priority")`

            - `BATCH("batch")`

    - `class MessageBatchErroredResult`

      - `JsonValue type = "errored"`

      - `ErrorResponse error`

        - `JsonValue type = "error"`

        - `ErrorObject error`

          - `class InvalidRequestError`

            - `JsonValue type = "invalid_request_error"`

            - `String message`

          - `class AuthenticationError`

            - `JsonValue type = "authentication_error"`

            - `String message`

          - `class BillingError`

            - `JsonValue type = "billing_error"`

            - `String message`

          - `class PermissionError`

            - `JsonValue type = "permission_error"`

            - `String message`

          - `class NotFoundError`

            - `JsonValue type = "not_found_error"`

            - `String message`

          - `class RateLimitError`

            - `JsonValue type = "rate_limit_error"`

            - `String message`

          - `class GatewayTimeoutError`

            - `JsonValue type = "timeout_error"`

            - `String message`

          - `class ApiErrorObject`

            - `JsonValue type = "api_error"`

            - `String message`

          - `class OverloadedError`

            - `JsonValue type = "overloaded_error"`

            - `String message`

        - `Optional<String> requestId`

    - `class MessageBatchCanceledResult`

      - `JsonValue type = "canceled"`

    - `class MessageBatchExpiredResult`

      - `JsonValue type = "expired"`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.batches.BatchResultsParams;
import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<MessageBatchIndividualResponse> messageBatchIndividualResponse = client.messages().batches().resultsStreaming("message_batch_id");
    }
}
```
