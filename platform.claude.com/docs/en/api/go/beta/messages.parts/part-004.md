<!-- source: https://platform.claude.com/docs/en/api/go/beta/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta/messages -->

<!-- chunk-start -->

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"`

                          - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260521 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `BlockedDomains []string Optional`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `UserLocation BetaUserLocation Optional`

                          Parameters for the user's location. Used to provide more relevant search results.

                          - `Type Approximate`

                          - `City string Optional`

                            The city of the user.

                            minLength: 1, maxLength: 255

                          - `Country string Optional`

                            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

                            minLength: 2, maxLength: 2

                          - `Region string Optional`

                            The region of the user.

                            minLength: 1, maxLength: 255

                          - `Timezone string Optional`

                            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

                            minLength: 1, maxLength: 255

                      - `type BetaWebFetchTool20250910`

                        - `Type WebFetch20250910`

                        - `Name WebFetch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"`

                          - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260521 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          List of domains to allow fetching from

                        - `BlockedDomains []string Optional`

                          List of domains to block fetching from

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Citations BetaCitationsConfigParamResp Optional`

                          Citations configuration for fetched documents. Citations are disabled by default.

                          - `Enabled bool Optional`

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxContentTokens int64 Optional`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `URLSources BetaWebFetchURLSources Optional`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                          - `ClientToolResults BetaWebFetchURLSourcesClientToolResultsUnion Optional`

                            Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

                            - `type BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                              - `Type All`

                            - `type BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                              - `Type None`

                            - `type BetaWebFetchURLSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                              - `Type Only`

                              - `Tools []BetaWebFetchURLSourceToolReference`

                                - `Type ToolReference`

                                - `Name string`

                            - `type BetaWebFetchURLSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                              - `Type Except`

                              - `Tools []BetaWebFetchURLSourceToolReference`

                                - `Type ToolReference`

                                - `Name string`

                          - `ServerToolResults BetaWebFetchURLSourcesServerToolResultsUnion Optional`

                            Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

                            - `type BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `type BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                            - `type BetaWebFetchURLSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                            - `type BetaWebFetchURLSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                          - `UserInput BetaWebFetchURLSourcesUserInputUnion Optional`

                            Whether URLs in user messages are fetchable: "all" or "none".

                            - `type BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `type BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                      - `type BetaWebSearchTool20260209`

                        - `Type WebSearch20260209`

                        - `Name WebSearch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"`

                          - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260521 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `BlockedDomains []string Optional`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `UserLocation BetaUserLocation Optional`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `type BetaWebFetchTool20260209`

                        - `Type WebFetch20260209`

                        - `Name WebFetch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"`

                          - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260521 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          List of domains to allow fetching from

                        - `BlockedDomains []string Optional`

                          List of domains to block fetching from

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Citations BetaCitationsConfigParamResp Optional`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxContentTokens int64 Optional`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `URLSources BetaWebFetchURLSources Optional`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                      - `type BetaWebFetchTool20260309`

                        Web fetch tool with use_cache parameter for bypassing cached content.

                        - `Type WebFetch20260309`

                        - `Name WebFetch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"`

                          - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260521 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          List of domains to allow fetching from

                        - `BlockedDomains []string Optional`

                          List of domains to block fetching from

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Citations BetaCitationsConfigParamResp Optional`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxContentTokens int64 Optional`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `URLSources BetaWebFetchURLSources Optional`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                        - `UseCache bool Optional`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `type BetaWebSearchTool20260318`

                        - `Type WebSearch20260318`

                        - `Name WebSearch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebSearchTool20260318AllowedCallerDirect BetaWebSearchTool20260318AllowedCaller = "direct"`

                          - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20250825 BetaWebSearchTool20260318AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260120 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260521 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `BlockedDomains []string Optional`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `ResponseInclusion BetaWebSearchTool20260318ResponseInclusion Optional`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `const BetaWebSearchTool20260318ResponseInclusionFull BetaWebSearchTool20260318ResponseInclusion = "full"`

                          - `const BetaWebSearchTool20260318ResponseInclusionExcluded BetaWebSearchTool20260318ResponseInclusion = "excluded"`

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `UserLocation BetaUserLocation Optional`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `type BetaWebFetchTool20260318`

                        - `Type WebFetch20260318`

                        - `Name WebFetch`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaWebFetchTool20260318AllowedCallerDirect BetaWebFetchTool20260318AllowedCaller = "direct"`

                          - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20250825 BetaWebFetchTool20260318AllowedCaller = "code_execution_20250825"`

                          - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260120 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260120"`

                          - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260521 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260521"`

                        - `AllowedDomains []string Optional`

                          List of domains to allow fetching from

                        - `BlockedDomains []string Optional`

                          List of domains to block fetching from

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Citations BetaCitationsConfigParamResp Optional`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxContentTokens int64 Optional`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `ResponseInclusion BetaWebFetchTool20260318ResponseInclusion Optional`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `const BetaWebFetchTool20260318ResponseInclusionFull BetaWebFetchTool20260318ResponseInclusion = "full"`

                          - `const BetaWebFetchTool20260318ResponseInclusionExcluded BetaWebFetchTool20260318ResponseInclusion = "excluded"`

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                        - `URLSources BetaWebFetchURLSources Optional`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                        - `UseCache bool Optional`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `type BetaAdvisorTool20260301`

                        - `Type Advisor20260301`

                        - `Model Model`

                          The model that will complete your prompt.

                          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                          - `const ModelClaudeHaiku5_5 Model = "claude-haiku-5-5"`

                            Fastest model for high-volume, real-time tasks

                          - `const ModelClaudeSonnet5_5 Model = "claude-sonnet-5-5"`

                            Efficient model for coding and agents

                          - `const ModelClaudeFable5_1 Model = "claude-fable-5-1"`

                            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                          - `const ModelClaudeOpus5_5 Model = "claude-opus-5-5"`

                            Powerful intelligence for coding, knowledge work, and long-running agents

                          - `const ModelClaudeMythos5_1 Model = "claude-mythos-5-1"`

                            Our most capable model for cybersecurity and biology research, available through trusted access programs

                          - `const ModelClaudeSonnet5 Model = "claude-sonnet-5"`

                            Efficient model for coding and agents

                          - `const ModelClaudeFable5 Model = "claude-fable-5"`

                            Next generation of intelligence for the hardest knowledge work and coding problems

                          - `const ModelClaudeMythos5 Model = "claude-mythos-5"`

                            Most capable model for cybersecurity and biology research

                          - `const ModelClaudeOpus5 Model = "claude-opus-5"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeOpus4_8 Model = "claude-opus-4-8"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeOpus4_7 Model = "claude-opus-4-7"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeOpus4_6 Model = "claude-opus-4-6"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"`

                            Best combination of speed and intelligence

                          - `const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"`

                            Fastest model with near-frontier intelligence

                          - `const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"`

                            Fastest model with near-frontier intelligence

                          - `const ModelClaudeOpus4_5 Model = "claude-opus-4-5"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"`

                            Powerful intelligence for long-running agents and coding

                          - `const ModelClaudeMythosPreview Model = "claude-mythos-preview"`

                            **Deprecated**: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

                            New class of intelligence, strongest in coding and cybersecurity

                          - `const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"`

                            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

                            High-performance model for agents and coding

                          - `const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"`

                            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

                            High-performance model for agents and coding

                        - `Name Advisor`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"`

                          - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code_execution_20250825"`

                          - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260120"`

                          - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260521 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260521"`

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Caching BetaCacheControlEphemeral Optional`

                          Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `MaxTokens int64 Optional`

                          Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

                          minimum: 1024

                        - `MaxUses int64 Optional`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                      - `type BetaToolSearchToolBm25_20251119`

                        - `Type BetaToolSearchToolBm25_20251119Type`

                          - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"`

                          - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"`

                        - `Name ToolSearchToolBm25`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaToolSearchToolBm25_20251119AllowedCallerDirect BetaToolSearchToolBm25_20251119AllowedCaller = "direct"`

                          - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"`

                          - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"`

                          - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260521"`

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                      - `type BetaToolSearchToolRegex20251119`

                        - `Type BetaToolSearchToolRegex20251119Type`

                          - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"`

                          - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex"`

                        - `Name ToolSearchToolRegex`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `AllowedCallers []string Optional`

                          - `const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"`

                          - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"`

                          - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"`

                          - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260521"`

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `DeferLoading bool Optional`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Strict bool Optional`

                          When true, guarantees schema validation on tool names and inputs

                      - `type BetaMCPToolset`

                        Configuration for a group of tools from an MCP server.

                        Allows configuring enabled status and defer_loading for all tools
                        from an MCP server, with optional per-tool overrides.

                        - `Type MCPToolset`

                        - `MCPServerName string`

                          Name of the MCP server to configure tools for

                          minLength: 1, maxLength: 255

                        - `CacheControl BetaCacheControlEphemeral Optional`

                          Create a cache control breakpoint at this content block.

                        - `Configs map[string, BetaMCPToolConfig] Optional`

                          Configuration overrides for specific tools, keyed by tool name

                          - `DeferLoading bool Optional`

                          - `Enabled bool Optional`

                        - `DefaultConfig BetaMCPToolDefaultConfig Optional`

                          Default configuration applied to all tools from this server

                          - `DeferLoading bool Optional`

                          - `Enabled bool Optional`

                        - `Tools []BetaMCPToolParamResp Optional`

                          The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

                          - `InputSchema map[string, any]`

                            The tool's input schema as the MCP server lists it, verbatim.

                          - `Name string`

                            The tool's name as the MCP server lists it (not prefixed with the server name).

                            minLength: 1

                          - `Description string Optional`

                            The tool's description as the MCP server lists it.

              - `type BetaResponseToolRemovalBlock`

                An entry of a `compaction` block's `tool_changes`: a tool of the
                request's `tools` (or an MCP tool or toolset) that the compacted range
                withdrew. Send it back unchanged.

                - `Type ToolRemoval`

                  default: tool_removal

                - `Tool BetaResponseToolRemovalBlockToolUnion`

                  A reference to the withdrawn `tools` entry, MCP tool or MCP toolset.

                  - `type BetaResponseToolChangeToolReference`

                    Reference to a single tool, by the name the model uses to call it, as
                    a `compaction` block's `tool_changes` entry reports it: a tool
                    declared in `tools` or defined by an earlier `tool_addition` block.
                    Send it back unchanged with the block.

                  - `type BetaResponseToolChangeMCPToolReference`

                    Reference to a single MCP tool, by its server and its name on that
                    server, as a `compaction` block's `tool_changes` entry reports it.
                    Send it back unchanged with the block.

                  - `type BetaResponseToolChangeMCPToolsetReference`

                    Reference to every tool in the named MCP server's toolset, as a
                    `compaction` block's `tool_changes` entry reports it. Send it back
                    unchanged with the block.

          - `type BetaFallbackBlock`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `Type Fallback`

              default: fallback

            - `From BetaFallbackInfo`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `To BetaFallbackInfo`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `Trigger BetaFallbackRefusalTrigger`

              What caused the `from` model to hand over at this hop.

              - `Type Refusal`

                default: refusal

              - `Category BetaFallbackRefusalTriggerCategory`

                The policy category that triggered the `from` model's refusal at this hop. `null` when the refusal doesn't map to a named category. Same vocabulary as `stop_details.category`.

                - `const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"`

                  The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"`

                  The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier_llm"`

                  The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning_extraction"`

                  The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

                - `const BetaFallbackRefusalTriggerCategoryGeneralHarms BetaFallbackRefusalTriggerCategory = "general_harms"`

                  The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `type BetaMCPToolListingBlock`

            The tool listing the server fetched from an MCP server while producing
            this response. Send the assistant message back unchanged, this block
            included, so later requests use this listing instead of asking the MCP
            server again.

            - `Type MCPToolListing`

              default: mcp_tool_listing

            - `MCPServerName string`

            - `Tools []BetaMCPTool`

              - `InputSchema map[string, any]`

              - `Name string`

              - `Description string Optional`

        - `ContextManagement BetaContextManagementResponse`

          Context management response.

          Information about context management strategies applied during the request.

          - `AppliedEdits []BetaContextManagementResponseAppliedEditUnion`

            List of context management edits that were applied.

            - `type BetaClearToolUses20250919EditResponse`

              - `Type ClearToolUses20250919`

                The type of context management edit applied.

                default: clear_tool_uses_20250919

              - `ClearedInputTokens int64`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `ClearedToolUses int64`

                Number of tool uses that were cleared.

                minimum: 0

            - `type BetaClearThinking20251015EditResponse`

              - `Type ClearThinking20251015`

                The type of context management edit applied.

                default: clear_thinking_20251015

              - `ClearedInputTokens int64`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `ClearedThinkingTurns int64`

                Number of thinking turns that were cleared.

                minimum: 0

        - `Diagnostics BetaDiagnostics`

          Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected.

          - `CacheMissReason BetaCacheMissReasonUnion`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `type BetaCacheMissModelChanged`

              - `Type ModelChanged`

                default: model_changed

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type BetaCacheMissSystemChanged`

              - `Type SystemChanged`

                default: system_changed

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type BetaCacheMissToolsChanged`

              - `Type ToolsChanged`

                default: tools_changed

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type BetaCacheMissMessagesChanged`

              - `Type MessagesChanged`

                default: messages_changed

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type BetaCacheMissPreviousMessageNotFound`

              - `Type PreviousMessageNotFound`

                default: previous_message_not_found

            - `type BetaCacheMissUnavailable`

              - `Type Unavailable`

                default: unavailable

        - `Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Role Assistant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          default: assistant

        - `StopDetails BetaRefusalStopDetails`

          Structured information about why model output stopped.

          This is `null` when the `stop_reason` has no additional detail to report.

          - `Type Refusal`

            default: refusal

          - `Category BetaRefusalStopDetailsCategory`

            The policy category that triggered the refusal.

            `null` when the refusal doesn't map to a named category.

            - `const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier_llm"`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning_extraction"`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `const BetaRefusalStopDetailsCategoryGeneralHarms BetaRefusalStopDetailsCategory = "general_harms"`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `Explanation string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `FallbackCreditToken string`

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

          - `FallbackHasPrefillClaim bool`

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

          - `RecommendedModel string`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

        - `StopReason BetaStopReason`

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

          - `const BetaStopReasonEndTurn BetaStopReason = "end_turn"`

          - `const BetaStopReasonMaxTokens BetaStopReason = "max_tokens"`

          - `const BetaStopReasonStopSequence BetaStopReason = "stop_sequence"`

          - `const BetaStopReasonToolUse BetaStopReason = "tool_use"`

          - `const BetaStopReasonPauseTurn BetaStopReason = "pause_turn"`

          - `const BetaStopReasonCompaction BetaStopReason = "compaction"`

          - `const BetaStopReasonRefusal BetaStopReason = "refusal"`

          - `const BetaStopReasonModelContextWindowExceeded BetaStopReason = "model_context_window_exceeded"`

        - `StopSequence string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `Usage BetaUsage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `CacheCreation BetaCacheCreation`

            Breakdown of cached tokens by TTL

            - `Ephemeral1hInputTokens int64`

              The number of input tokens used to create the 1 hour cache entry.

              default: 0, minimum: 0

            - `Ephemeral5mInputTokens int64`

              The number of input tokens used to create the 5 minute cache entry.

              default: 0, minimum: 0

          - `CacheCreationInputTokens int64`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `CacheReadInputTokens int64`

            The number of input tokens read from the cache.

            minimum: 0

          - `FallbackCredit BetaFallbackCreditUsage`

            Outcome of the `fallback_credit_token` presented on this request.

            Present on every response to a non-batch request that carried a
            `fallback_credit_token`, in either redemption mode; absent otherwise (batch
            items accept and ignore the token and carry no outcome object).

            - `Status BetaFallbackCreditUsageStatusUnion`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `type BetaFallbackCreditRedeemed`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `Type Redeemed`

                  default: redeemed

              - `type BetaFallbackCreditNotApplied`

                No reprice was applied; `reason` says why.

                - `Type NotApplied`

                  default: not_applied

                - `Reason BetaFallbackCreditNotAppliedReason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `const BetaFallbackCreditNotAppliedReasonBodyMismatch BetaFallbackCreditNotAppliedReason = "body_mismatch"`

                  - `const BetaFallbackCreditNotAppliedReasonContinuationExcluded BetaFallbackCreditNotAppliedReason = "continuation_excluded"`

                  - `const BetaFallbackCreditNotAppliedReasonContinuationOnly BetaFallbackCreditNotAppliedReason = "continuation_only"`

                  - `const BetaFallbackCreditNotAppliedReasonExpired BetaFallbackCreditNotAppliedReason = "expired"`

                  - `const BetaFallbackCreditNotAppliedReasonInvalidTargetModel BetaFallbackCreditNotAppliedReason = "invalid_target_model"`

                  - `const BetaFallbackCreditNotAppliedReasonNotEnabled BetaFallbackCreditNotAppliedReason = "not_enabled"`

                  - `const BetaFallbackCreditNotAppliedReasonRepriceUnavailable BetaFallbackCreditNotAppliedReason = "reprice_unavailable"`

                  - `const BetaFallbackCreditNotAppliedReasonTemporarilyUnavailable BetaFallbackCreditNotAppliedReason = "temporarily_unavailable"`

                  - `const BetaFallbackCreditNotAppliedReasonVariantFieldsPresent BetaFallbackCreditNotAppliedReason = "variant_fields_present"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongOrganization BetaFallbackCreditNotAppliedReason = "wrong_organization"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongPlatform BetaFallbackCreditNotAppliedReason = "wrong_platform"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongWorkspace BetaFallbackCreditNotAppliedReason = "wrong_workspace"`

                - `RemoveToRedeem []string Optional`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `InferenceGeo string`

            The geographic region where inference was performed for this request.

          - `InputTokens int64`

            The number of input tokens which were used.

            minimum: 0

          - `Iterations BetaIterationsUsage`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `type BetaMessageIterationUsage`

              Token usage for a sampling iteration.

              - `Type Message`

                Usage for a sampling iteration

                default: message

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

            - `type BetaCompactionIterationUsage`

              Token usage for a compaction iteration.

              - `Type Compaction`

                Usage for a compaction iteration

                default: compaction

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

            - `type BetaAdvisorMessageIterationUsage`

              Token usage for an advisor sub-inference iteration.

              - `Type AdvisorMessage`

                Usage for an advisor sub-inference iteration

                default: advisor_message

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

            - `type BetaFallbackMessageIterationUsage`

              Token usage for the fallback-model attempt of a server-side fallback request.

              The terminal entry of a fallback-served turn: when a fallback hop's
              output is the returned message, the entry for the iteration that
              completed it carries this type in place of `message`. A declined hop
              and the serving hop's earlier tool-loop iterations produce `message`
              entries. Whether a fallback model served the response is signalled by
              the presence of this entry in `usage.iterations`.

              - `Type FallbackMessage`

                Usage for the fallback-model attempt that served the response

                default: fallback_message

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

          - `OutputTokens int64`

            The number of output tokens which were used.

            minimum: 0

          - `OutputTokensDetails BetaOutputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `ThinkingTokens int64`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              default: 0, minimum: 0

          - `ServerToolUse BetaServerToolUsage`

            The number of server tool requests.

            - `WebFetchRequests int64`

              The number of web fetch tool requests.

              default: 0, minimum: 0

            - `WebSearchRequests int64`

              The number of web search tool requests.

              default: 0, minimum: 0

          - `ServiceTier BetaUsageServiceTier`

            If the request used the priority, standard, or batch tier.

            - `const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"`

            - `const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"`

            - `const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"`

          - `Speed BetaUsageSpeed`

            The inference speed mode used for this request.

            - `const BetaUsageSpeedStandard BetaUsageSpeed = "standard"`

            - `const BetaUsageSpeedFast BetaUsageSpeed = "fast"`

        - `InputTransformations []BetaInputTransformationUnion Optional`

          Changes the API made to the request's input before showing it to the model,
          and blocks that failed a binding check but were left unchanged: one entry per
          block, in request order. Two entry types today. `thinking_dropped` — a
          `thinking`, `redacted_thinking` or `connector_text` block from the request's
          `messages` that was removed from the prompt instead of being shown to the
          model because it failed a binding check. `thinking_mismatch_allowed` — a
          `thinking` or `redacted_thinking` block that failed the conversation check
          (the conversation before it differs from the one it was created in, or it
          carries no record of one on a model that requires it) and was shown to the
          model all the same, because that check is not enforced for this request.
          More entry types may be added over time; ignore types you do not recognize.

          Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
          every such response from a model that supports extended thinking, as `[]`
          when there is no entry to report; without the beta, blocks are removed or
          left in place all the same but nothing is reported. Removed blocks contribute
          nothing to `usage.input_tokens`; blocks left in place count as sent. When
          streaming, the array is final in `message_start`; the final `message_delta`
          event carries it only when a server-side model fallback happened mid-stream,
          in which case it holds the serving model's entries and replaces the one in
          `message_start`.

          - `type BetaThinkingDroppedInputTransformation`

            - `Type ThinkingDropped`

              Always `thinking_dropped` for this entry type.

              default: thinking_dropped

            - `Path string`

              Where the removed block was in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `Reason BetaThinkingDroppedInputTransformationReason`

              Which binding check removed the block: `model_binding_mismatch` — it was
              created by a model whose reasoning the requested model may not read;
              `prefix_binding_mismatch` — the conversation before it differs from the
              conversation it was created in (the rest of that turn's consecutive thinking
              blocks are removed with it, each with this reason);
              `organization_binding_mismatch` — it was created under a different
              organization (an Anthropic organization, AWS account or Google Cloud project)
              and this organization is not one of its additional organizations;
              `end_user_binding_mismatch` — it was created for a different end user, or
              was removed by the consumer-organization binding. A block that would fail
              several checks reports one reason, in this order of precedence:
              `organization_binding_mismatch`, `end_user_binding_mismatch`,
              `model_binding_mismatch`, `prefix_binding_mismatch`.

              - `const BetaThinkingDroppedInputTransformationReasonModelBindingMismatch BetaThinkingDroppedInputTransformationReason = "model_binding_mismatch"`

              - `const BetaThinkingDroppedInputTransformationReasonPrefixBindingMismatch BetaThinkingDroppedInputTransformationReason = "prefix_binding_mismatch"`

              - `const BetaThinkingDroppedInputTransformationReasonOrganizationBindingMismatch BetaThinkingDroppedInputTransformationReason = "organization_binding_mismatch"`

              - `const BetaThinkingDroppedInputTransformationReasonEndUserBindingMismatch BetaThinkingDroppedInputTransformationReason = "end_user_binding_mismatch"`

          - `type BetaThinkingMismatchAllowedInputTransformation`

            - `Type ThinkingMismatchAllowed`

              Always `thinking_mismatch_allowed` for this entry type.

              default: thinking_mismatch_allowed

            - `Path string`

              Where the block is in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `Reason BetaThinkingMismatchAllowedInputTransformationReason`

              Which binding check the block failed; the block was shown to the model all
              the same. Always `prefix_binding_mismatch` today — the conversation before
              the block differs from the conversation it was created in, or the block
              carries no record of one on a model that requires it. Were the check
              enforced for this request, the block would have been removed or the request
              rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also
              takes the rest of that turn's consecutive thinking blocks, whereas here each
              block is checked on its own, so `thinking_mismatch_allowed` entries are a
              lower bound on what enforcement would remove.

              - `const BetaThinkingMismatchAllowedInputTransformationReasonModelBindingMismatch BetaThinkingMismatchAllowedInputTransformationReason = "model_binding_mismatch"`

              - `const BetaThinkingMismatchAllowedInputTransformationReasonPrefixBindingMismatch BetaThinkingMismatchAllowedInputTransformationReason = "prefix_binding_mismatch"`

              - `const BetaThinkingMismatchAllowedInputTransformationReasonOrganizationBindingMismatch BetaThinkingMismatchAllowedInputTransformationReason = "organization_binding_mismatch"`

              - `const BetaThinkingMismatchAllowedInputTransformationReasonEndUserBindingMismatch BetaThinkingMismatchAllowedInputTransformationReason = "end_user_binding_mismatch"`

    - `type BetaMessageBatchErroredResult`

      - `Type Errored`

        default: errored

      - `Error BetaErrorResponse`

        - `Type Error`

          default: error

        - `Error BetaErrorUnion`

          - `type BetaInvalidRequestError`

            - `Type InvalidRequestError`

              default: invalid_request_error

            - `Message string`

              default: Invalid request

          - `type BetaAuthenticationError`

            - `Type AuthenticationError`

              default: authentication_error

            - `Message string`

              default: Authentication error

          - `type BetaBillingError`

            - `Type BillingError`

              default: billing_error

            - `Message string`

              default: Billing error

          - `type BetaPermissionError`

            - `Type PermissionError`

              default: permission_error

            - `Message string`

              default: Permission denied

          - `type BetaNotFoundError`

            - `Type NotFoundError`

              default: not_found_error

            - `Message string`

              default: Not found

          - `type BetaRateLimitError`

            - `Type RateLimitError`

              default: rate_limit_error

            - `Message string`

              default: Rate limited

          - `type BetaGatewayTimeoutError`

            - `Type TimeoutError`

              default: timeout_error

            - `Message string`

              default: Request timeout

          - `type BetaAPIError`

            - `Type APIError`

              default: api_error

            - `Message string`

              default: Internal server error

          - `type BetaOverloadedError`

            - `Type OverloadedError`

              default: overloaded_error

            - `Message string`

              default: Overloaded

        - `RequestID string`

    - `type BetaMessageBatchCanceledResult`

      - `Type Canceled`

        default: canceled

    - `type BetaMessageBatchExpiredResult`

      - `Type Expired`

        default: expired

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	stream := client.Beta.Messages.Batches.ResultsStreaming(
		context.TODO(),
		"message_batch_id",
		anthropic.BetaMessageBatchResultsParams{},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```
