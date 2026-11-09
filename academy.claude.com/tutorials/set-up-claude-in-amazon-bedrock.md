<!-- source: https://academy.claude.com/tutorials/set-up-claude-in-amazon-bedrock -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Set up Claude in Amazon Bedrock

Get a first reply from Claude in your own AWS account. Sign in from your terminal as a role that's allowed to call Claude, then run one short Python file with Anthropic's Python SDK.

25 minClaude Platform

**With Claude in Amazon Bedrock, you call Claude from your own AWS account.** You use your AWS sign-in, and the usage goes on your AWS bill. One short Python file gets you a first reply from Claude. You don't need an Anthropic API key.

Before you start, you need an AWS account, Python 3.10 or later, and the AWS CLI. The AWS CLI is the tool for using AWS from a terminal.

## Get permission to call Claude[](#get-permission-to-call-claude)

On this page, you sign in as a role to call Claude. A role is a set of permissions in an AWS account. That role is created in IAM Identity Center, AWS's service for signing in. IAM Identity Center is also where you sign in as that role.

**The steps below are for whoever administers your AWS account, so if that isn't you, send these steps to your admin.** If you've never set up IAM Identity Center, start with AWS's [getting started guide for IAM Identity Center(opens in new tab)](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).

1. **Create a permission set.** A permission set holds the policies that list what a role may do. Follow AWS's steps to [create a permission set(opens in new tab)](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html). Add to it the AWS managed policy `AmazonBedrockMantleInferenceAccess`, which AWS provides to allow calls to Claude in Amazon Bedrock.
2. **Add these permissions for AWS Marketplace, AWS's store, to the same permission set.**

   * `aws-marketplace:Subscribe`
   * `aws-marketplace:Unsubscribe`
   * `aws-marketplace:ViewSubscriptions`

   The first call to each Claude model in an account can start a subscription to that model through AWS Marketplace, and that call needs these permissions. The account also needs a payment method set up for AWS Marketplace purchases. These permissions are needed only for a model's first use in an account, so you can remove them from the permission set once the subscription to each model the account will use is complete.
3. **Assign the permission set to the person who will call Claude.** Do this in the AWS account they'll call Claude from, following AWS's steps to [assign access to AWS accounts(opens in new tab)](https://docs.aws.amazon.com/singlesignon/latest/userguide/assignusers.html). Assigning it creates the role in that account, named after the permission set.

## Sign in from your terminal[](#sign-in-from-your-terminal)

Ask your admin for the details you need to sign in:

* The AWS account to use.
* The name of the role.
* The IAM Identity Center start URL, the web address where you sign in.
* The AWS Region that hosts IAM Identity Center. A Region is one of the places where AWS runs its services.

You sign in as the role with the AWS CLI. If you don't have it yet, [install the AWS CLI(opens in new tab)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) first. Then work through these steps in order.

1. **Set up a sign-in profile.** A profile is a named set of sign-in settings that the CLI saves. Run this command:

   bash

   ```
   aws configure sso
   ```

   It asks its questions one at a time. Answer the first ones like this:

   1. For the session name, enter any short name, such as `my-sso`.
   2. For the start URL, enter the one your admin gave you.
   3. For the Region that hosts IAM Identity Center, enter the one your admin gave you.
   4. For the registration scopes, enter `sso:account:access`.

   Next the command opens your browser, and you sign in there. If the browser doesn't open, follow the instructions the command prints. When the command lists AWS accounts and then roles, pick the account and the role your admin named.

   At the end it asks for these settings:

   1. For the profile's Region, enter `us-east-1`, which is US East (N. Virginia).
   2. For the output format, enter `json`.
   3. For the profile name, enter `default`. The CLI uses the `default` profile when a command doesn't name one, so the commands below run as written.
2. **Sign in.**

   bash

   ```
   aws sso login
   ```

   Your browser opens. Finish signing in there, and the terminal prints a line that starts "Successfully logged into Start URL". The CLI now holds your credentials. Credentials are short-lived keys that prove to AWS who you are. When they expire, run this command again.
3. **Check which account and role you're signed in as.**

   bash

   ```
   aws sts get-caller-identity
   ```

   In the output, `Account` should be the ID of your AWS account. `Arn` is AWS's full name for the role you're signed in as, and it should include the name of the role you picked. If either is wrong, run `aws configure sso` again and pick the right account and role.

## Get a first reply[](#get-a-first-reply)

Now send Claude one request from Python.

1. **Install Anthropic's Python SDK, with its Amazon Bedrock support.** The SDK is Anthropic's library for calling Claude from code.

   bash

   ```
   pip install -U "anthropic[bedrock]"
   ```
2. **Save this file as `first_reply.py`.**

   python

   ```
   from anthropic import (
       AnthropicBedrockMantle,
   )

   client = AnthropicBedrockMantle(
       aws_region="us-east-1",
   )

   message = client.messages.create(
       model="anthropic.claude-sonnet-5",
       max_tokens=1024,
       messages=[{
           "role": "user",
           "content": "Hello, Claude",
       }],
   )

   for block in message.content:
       if block.type == "text":
           print(block.text)
   ```

   The file creates a client, the object your code sends requests through. The client is for Claude in Amazon Bedrock in `us-east-1`, the Region you gave your profile.

   The client finds your AWS credentials by itself, including the ones from your IAM Identity Center sign-in, so no key goes in the file.

   The file then sends one message, "Hello, Claude", to Claude Sonnet 5. The `model` line names that model by its model ID. Last, the file prints the text of Claude's reply.
3. **Run the file.**

   bash

   ```
   python first_reply.py
   ```

   Claude's reply prints in your terminal. If Python stops with an error instead, go to "If the request fails" below.
4. **Check the account again.** In the same terminal, run `aws sts get-caller-identity`. It shows which account and role you're signed in as. The usage goes on your AWS bill, so make sure the account is the one your admin named.

## If the request fails[](#if-the-request-fails)

When a request fails, the SDK raises an error, which Python prints in the terminal. Look in that output for `PermissionDeniedError` or `NotFoundError`.

### A permission error[](#a-permission-error)

`PermissionDeniedError` means AWS refused the request with status 403. A status is the number a server sends back to say how a request went. The credentials you sent aren't allowed to make this request. Try these fixes in order:

1. Sign in again, because your sign-in may have expired. Run `aws sso login`, then run `first_reply.py` again.
2. Ask your admin to check that the role and the account have everything listed under "Get permission to call Claude."
3. If this is the first call to Claude Sonnet 5 in your account, wait 2 minutes after the permissions are in place, then run `first_reply.py` again. The subscription to the model can take up to 2 minutes to complete, and calls may be refused until it's done.

### A not-found error[](#a-not-found-error)

`NotFoundError` means AWS answered with status 404 and couldn't find something the request named. Check the model ID in `first_reply.py`. Model IDs in Claude in Amazon Bedrock start with `anthropic.`, so it must read `anthropic.claude-sonnet-5` exactly.

### Any other error[](#any-other-error)

Look up any other error on AWS's page of [Amazon Bedrock error codes(opens in new tab)](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html).

## Where to go next[](#where-to-go-next)

Next, take the course [Claude Platform 101(opens in new tab)](https://academy.claude.com/courses/claude-platform-101), which teaches building on the Claude Platform. Several of its lessons have Python samples that create their client with `anthropic.Anthropic()`.

**In those samples, use the import, the client line, and the model ID from `first_reply.py` instead.** Some of the course's samples use features that Claude in Amazon Bedrock does not support, which the [Claude in Amazon Bedrock docs page(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock) lists.

* [Get permission to call Claude](#get-permission-to-call-claude)
* [Sign in from your terminal](#sign-in-from-your-terminal)
* [Get a first reply](#get-a-first-reply)
* [If the request fails](#if-the-request-fails)
* [Where to go next](#where-to-go-next)
