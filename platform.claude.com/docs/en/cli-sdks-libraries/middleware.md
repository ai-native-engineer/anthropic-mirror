<!-- source: https://platform.claude.com/docs/en/cli-sdks-libraries/middleware -->

# SDK middleware
Intercept and modify requests and responses in the Anthropic SDKs.
The Anthropic SDKs provide a middleware (or interceptor) hook that lets you run code before a request is sent and after the response is received. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and refusal fallback handling.
Each middleware can inspect or replace the request before calling `next()`, and the response after `next()` returns.
Registering middleware
Each middleware is a function that receives the outgoing request and a `next` callable. Call `next` to forward the request to the rest of the chain (or directly to the SDK core if this is the last middleware), and return its response. Anything before the `next` call runs on the way out; anything after runs on the way back.
Python
Python
TypeScript
TypeScript
Go
Go
Java
Java
C#
C#
Ruby
Ruby
PHP
PHP

def logging_middleware(request: APIRequest, call_next: CallNext):
    # Before the request
    print(f"-> {request.method} {request.url}")

    # Forward the request to the rest of the chain
    response = call_next(request)

    # After the request
    print(f"<- {response.status_code}")

    return response

client = Anthropic(middleware=[logging_middleware])

Middleware ordering
When you register multiple middleware, they apply in the order given: the first middleware's "before" code runs first, and its "after" code runs last. Middleware registered on the client runs before middleware passed as a per-request option.
In the Go SDK, repeated `option.WithMiddleware` calls concatenate (client first, then method). In the other SDKs, pass an array; later entries wrap inner.
Replacing the HTTP client
Each SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used per SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.
Built-in middleware
The SDKs ship a refusal-fallback middleware that automatically retries requests Claude Fable 5 declines on a fallback model. See [Detect and retry on a fallback model](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) for setup and per-language examples.
  * [Registering middleware](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware#registering-middleware)
  * [Middleware ordering](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware#middleware-ordering)
  * [Replacing the HTTP client](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware#replacing-the-http-client)
  * [Built-in middleware](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware#built-in-middleware)

CLI, SDKs, and libraries/Client SDKs
# SDK middleware
Intercept and modify requests and responses in the Anthropic SDKs.
The Anthropic SDKs provide a middleware (or interceptor) hook that lets you run code before a request is sent and after the response is received. Use middleware for cross-cutting concerns such as logging, custom retries, request annotation, and refusal fallback handling.
Each middleware can inspect or replace the request before calling `next()`, and the response after `next()` returns.
Registering middleware
Each middleware is a function that receives the outgoing request and a `next` callable. Call `next` to forward the request to the rest of the chain (or directly to the SDK core if this is the last middleware), and return its response. Anything before the `next` call runs on the way out; anything after runs on the way back.
Python
Python
TypeScript
TypeScript
Go
Go
Java
Java
C#
C#
Ruby
Ruby
PHP
PHP

def logging_middleware(request: APIRequest, call_next: CallNext):
    # Before the request
    print(f"-> {request.method} {request.url}")

    # Forward the request to the rest of the chain
    response = call_next(request)

    # After the request
    print(f"<- {response.status_code}")

    return response

client = Anthropic(middleware=[logging_middleware])

Middleware ordering
When you register multiple middleware, they apply in the order given: the first middleware's "before" code runs first, and its "after" code runs last. Middleware registered on the client runs before middleware passed as a per-request option.
In the Go SDK, repeated `option.WithMiddleware` calls concatenate (client first, then method). In the other SDKs, pass an array; later entries wrap inner.
Replacing the HTTP client
Each SDK also accepts a custom HTTP client (for proxy configuration, custom TLS, or connection pooling). Only one HTTP client is used per SDK client; setting it replaces the default. The custom HTTP client receives requests after all middleware has run.
Built-in middleware
The SDKs ship a refusal-fallback middleware that automatically retries requests Claude Fable 5 declines on a fallback model. See [Detect and retry on a fallback model](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) for setup and per-language examples.
