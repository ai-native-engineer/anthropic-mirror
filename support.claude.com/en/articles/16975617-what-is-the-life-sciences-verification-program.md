<!-- source: https://support.claude.com/en/articles/16975617-what-is-the-life-sciences-verification-program -->

# What is the Life Sciences Verification Program?

Updated this week

Table of contents

This article explains what the Life Sciences Verification Program (LSVP) is, supported use cases, and how to apply.

This program is currently in beta. During the beta, LSVP runs on Anthropic's first-party products only: Claude Enterprise plans, Team plans, and the Claude Platform (API). This program doesn’t currently support Pro plans, Max plans, or cloud providers. We’ll continue to improve the program and expand access over time. You can read more in our **[blog post announcement](https://www.anthropic.com/news/life-sciences-verification-program)**.

---

## About the Life Sciences Verification Program

The Life Sciences Verification Program gives verified life sciences organizations access to Claude's most capable models for internal research and development. It has a refined set of biology safeguards for these organizations so everyday scientific work runs without interruption.

Claude's generally available models include safeguards that block some biology requests, because the same knowledge that advances medicine can also be misused. These safeguards can sometimes interrupt normal work such as target discovery, molecular design, clinical development, and manufacturing. LSVP lets verified organizations keep protections in place while preventing against the most serious misuse.

We’ve designed these new safeguards specifically to defend against three concerning threat models:

* Access compromise: malware or account takeover diverting access to a bad actor
* Insider threats: rogue or coerced employees intentionally taking malicious action or diverting their access to a bad actor
* Agent misuse: agents, especially working in swarms or over long-horizon tasks, taking unintended dangerous actions

## Requirements

* 30-day data retention for program usage, with automated safety monitoring and human review of flagged activity in rare circumstances.
* A dedicated workspace, with phishing-resistant multi-factor authentication for the Claude apps or Workload Identity Federation for the API.
* Use by your own organization, for internal work only.

---

## What's included with LSVP?

### Models

Access grants apply to Claude Opus 5.5, Claude Mythos 5.1, Claude Opus 5, and Claude Sonnet 5 today, and to select future models as they launch.

On Sonnet 5.5, LSVP relaxes biology safeguards only through the High-risk Use add-on.

Claude Fable models aren't part of LSVP and keep their full biology safeguards under every grant. If you hold an LSVP grant, use Claude Mythos 5.1 instead of Fable. The older Claude Mythos 5 preview is not offered under LSVP access.

### Seats

The program includes up to 100 seats for each approved team (each team is its own grant). An organization can apply for multiple grants for different teams.

### High-risk Use add-on

You’ll have access to an optional High-risk Use add-on for specific projects, such as virology or toxin research, that need further safeguards relaxed.

### Not available during the beta

* **Workloads involving protected health information (PHI).** Your organization can still join for research that doesn't use PHI. See **Can we use LSVP with protected health information?** below.
* **Customers who use Claude only through a cloud provider** (Amazon Web Services, Google Cloud, Microsoft Azure). The beta runs on Anthropic's first-party products only, so you need a first-party Anthropic organization. We’ll continue to improve the program and expand access over time.
* **Individuals and researchers not affiliated with an organization**. We grant access to a verified organization, not to a person.
* **Platforms passing access through to their own customers.** A platform can apply for its own internal research and development (R&D) today.

---

## Supported use cases

LSVP is designed to support and enable the following use cases:

* Drug and countermeasure discovery and preclinical support
* Understanding how diseases work
* Clinical development and operations
* Bioinformatics, computational biology, and research data infrastructure
* Diagnostics and laboratory medicine
* Manufacturing, quality, and supply chain for regulated products
* Regulatory affairs, medical affairs, and market access
* Public health, biosurveillance, biosafety, and biosecurity
* Agricultural, veterinary, and environmental biosciences
* Life sciences funding and diligence
* Life sciences education and training

---

## How do I apply?

To apply to the Life Sciences Verification Program:

1. **Express interest.** Submit the **[Life Sciences Verification Program interest form](https://claude.com/form/life-sciences-verification-program)**. If your Anthropic account team has already invited you, skip this step.
2. **We review your interest.** If your organization is a fit for the current phase, we'll contact you and ask which Anthropic organization you'd like to use. Not every organization that submits the form will be invited during the beta.
3. **We open the application for your organization.** Once we've enabled the application, it appears in the **[Verification Portal](https://portal.anthropic.com/programs)**. It won't be visible before then. To submit an application you’ll need to verify your identity. For more information, see **[Identity verification on Claude](https://support.claude.com/en/articles/14328960-identity-verification-on-claude)**.
4. **Your organization's admin applies.** Only an Admin, Owner, or Primary Owner for your organization can submit. The application takes about 15 minutes, starting with a business verification step.
5. **We review.** Decisions typically come within about three business days. We may email your admin for more details first.
6. **You set up access.** When your application is approved, your account team will let you know and send you a guide to get started for your plan. We provision the grant to your organization automatically.

## What the application asks

* Details about your organization.
* One life sciences reference, such as an FDA registration, a clinical trial ID, or a public grant number. If none apply, choose "none of the above" and write a couple of sentences about your life sciences work, plus your website.
* The team, what it will use Claude for, and how it will use the results.
* The name of your IT admin.
* A short set of attestations, including that use is internal to your organization.

The application doesn’t ask for program-level science, targets, or readouts. Anything you share is subject to our confidentiality obligations.

---

## Data retention, safety review, and privacy

### Why is data retention required?

LSVP relaxes the real-time classifiers that normally interrupt biology work. Without them, the way we catch misuse is through an automated review that spots patterns across many conversations. That review is designed to protect against serious biological misuse, insider misuse, and account takeover.

* Program usage is retained for 30 days.
* Zero data retention isn’t available. Existing zero-retention or custom-retention agreements don't apply to usage under an LSVP grant.
* Retention covers only the program workspace or organization. Your other Anthropic organizations are unaffected.
* Retained data is used only to identify and prevent misuse. It’s never used for training or product improvement, and it isn't analyzed for any commercial or research purpose.
* Anthropic monitors program usage against the scope you shared. If something looks out of scope, we'll notify your admin directly and give you one week to explain, narrow the scope, or dispute it.

### Can we use LSVP with protected health information?

Not during the beta. LSVP isn't covered under a Business Associate Agreement (BAA), so workloads involving protected health information (PHI) are out of scope.

If your organization has non-PHI workloads, you can still apply. Use a separate Anthropic organization that isn't set up under your BAA and doesn't handle PHI. Organizations set up under a BAA can't receive LSVP grants.

---

Related Articles

* [Anthropic's AI for Science Program](https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program)
* [Covered Models](https://support.claude.com/en/articles/15425695-covered-models)
* [Data retention practices for Covered Models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
* [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5)
* [Why Claude switched models in your conversation with Sonnet 5.5](https://support.claude.com/en/articles/17161993-why-claude-switched-models-in-your-conversation-with-sonnet-5-5)

Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents
