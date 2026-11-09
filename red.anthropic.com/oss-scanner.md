<!-- source: https://red.anthropic.com/oss-scanner/ -->

# OSS Scanner

*OSS Scanner is a service by Anthropic to scan open-source repositories for security vulnerabilities. It’s an opt-in service informed by our experience using Claude to find vulnerabilities during [Project Glasswing](https://www.anthropic.com/glasswing). Projects that join will receive thorough, periodic security scans by our strongest models at no cost.*

We regularly scan open source software for vulnerabilities and send reports after they have undergone human review as part of our [coordinated vulnerability disclosure (CVD) process](https://red.anthropic.com/2026/cvd/). By October 2026, we had reviewed over 6,000 such reports. This helps many projects secure their code without being overwhelmed by false positives. However, these manual review steps take time, so we're not always able to share vulnerabilities as quickly as we would like.

OSS Scanner provides an optional fast track. Projects that enroll will receive reports as soon as they’re scanned directly from our strongest models. If your project would like to receive reports that have not undergone human review, you can enroll by submitting a PR to add your project per the instructions below.

Learn more about this project in our [launch post](http://anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source).

We aim to continue to improve this service particularly as models improve.

## FAQ

### What projects are eligible?

We will accept projects using a similar set of criteria to OSS-Fuzz, which states:

> *We accept established projects that have a critical impact on infrastructure and user security. We will consider each request on a case-by-case basis, but some things we keep in mind are: (1) Exposure to remote attacks (e.g. libraries that are used to process untrusted input); and (2) Number of users/other projects depending on this project.*

While we make a holistic determination, some of the factors we look at include age and update frequency, [OpenSSF criticality score](https://github.com/ossf/criticality_score), whether the project uses a commonly accepted [open-source](https://opensource.org/osd) license, stars/forks, usage statistics, how security-critical the project is and to what sectors, and the completeness of the required fields. We hope to further standardize this process, and may adjust the acceptance criteria over time. We encourage maintainers to write a short sentence explaining why their project is critical to security where it is not already self-evident.

Common exclusions: While we’re excited by brand new projects that want to build secure foundations from day one, they do not typically qualify. We typically do not scan forks of projects unless they are distinctly unique from the original project and independently qualify.

While there is little downside to signing up if you’re eligible, we recognize that many projects are already overwhelmed by the number of reports they’re receiving. This service is built for projects that are already able to keep up with verified high/critical vulnerability reports and are now looking to further secure their code.

### I’m a maintainer. How do I sign up?

The core maintainers of a project can enroll by opening a PR at <https://github.com/anthropics/oss-scanner> that adds a config file at `projects/<project>/project.yaml`. We’ve provided a [project template](https://github.com/anthropics/oss-scanner/blob/main/templates/project.yaml) as a starting point.

The project.yaml config requires the following fields:

* `repo`: a link to the git repository that should be cloned (optionally with a #branch)
* `primary_contact`: the email address of the primary contact (usually your own email address)
* `Dockerfile`: a repo-relative path to the Dockerfile that sets up the environment, pre-installs all dependencies and builds the project, so that a fully offline agent can conduct its security audit. Optionally, you can place a file named `Dockerfile` next to your `project.yaml` in our repository and omit this entry from your `project.yaml`—in this case the field should be left out.

It may optionally include:

* `auto_ccs`: additional email addresses that we will CC on all reports
* `homepage`: your project homepage
* `threat_model`: a repo-relative path to a threat model file that documents your preferences for the scanner (default `.oss-scanner/threat_model.md`), or place a file named `threat_model.md` next to your `project.yaml` in our repository
* `pgp`: a GPG public key that will be used to encrypt report emails
* `disabled`: a field you can set to true if you want to stop receiving bug reports, with the option to re-enable it at a later date

The link to the project homepage, git repository, and email addresses are hopefully self-explanatory. We use the project homepage for our own information and to help understand the importance of the project. The git repository is the URL that will be cloned; it does not have to be hosted on GitHub. The primary email address will receive all communication and will be used for any out-of-the-ordinary contact we may need to make. We will CC every report to any additional addresses provided.

The Dockerfile configures the environment that the project will run in and installs all dependencies so that the agent can perform its security audit without any internet access. We recommend verifying that the test cases pass inside of the built container. The Dockerfile itself is built with network access; everything after it runs without. We have provided a sample Dockerfile in our project template.

Before opening your PR, you can run `tools/validate.py` to check the config file. We also recommend building your Dockerfile locally and confirming it succeeds. After your project is accepted, we will attempt to build it on our own infrastructure and will email promptly if the build fails so you can make any necessary corrections.

The threat model file gives you the opportunity to describe any facts about your project that might not otherwise be documented that you would like agents to know. It has no required format or sections. For example, you might wish to include the following pieces of information:

* A threat model describing what code should be tested, which inputs should be treated as adversarial, and what is out of scope and should be ignored
* A severity rubric documenting how you would like vulnerabilities to be classified as critical, high, medium, or low
* Guidance on how reports should be formatted, how candidate patches should be produced (minimally to demonstrate the vulnerability or maximally as a merge-ready patch), and what types of proof-of-concepts are useful
* Guidance for how granular deduplication should be performed

This file is optional, and without it the scanner will still be able to function, but it will make guesses at what it thinks is the best way to handle any corner cases. If you place this file in your repository, feel free to modify it between scans to alter the report format.

If you would like to receive email reports encrypted, you can include a GPG public key in the config file (the `pgp` field) and we will encrypt emails before they are sent. If you include a GPG key then you cannot include additional CCs; mail will only go to the primary email address.

By signing up you agree to our [terms and conditions](https://red.anthropic.com/oss-scanner/terms/).

### What will maintainers receive?

After first enrolling a project, we will scan it for vulnerabilities. Our pipeline includes agents to double-check bugs, propose patches, and perform root cause analysis. Maintainers then receive a bundle of bug reports via email. After the first scan, we will regularly scan projects to identify potential new vulnerabilities introduced since the last scan, and vulnerabilities that we may have missed in prior scans. The frequency of these additional scans may depend on the number of projects in our pipeline, how widely it's used, and other factors.

In the future we may alter the exact reporting format. For example, we’re starting out by sending email reports because it is easy for everyone involved, but we may move to a different medium.

### What is the public disclosure policy?

We will not place any form of 90-day coordinated disclosure period on these unvalidated findings. Because it is possible these findings may contain false positives, we do not feel comfortable forcing maintainers to carefully read each finding if we have not yet done the same.

If we later validate one of these reports manually through our existing CVD program, we may disclose it under our CVD policy starting 90 days from when you are notified that a human has validated this report. As we gain greater confidence in OSS Scanner’s performance, we may in the future impose a disclosure period on some high-severity vulnerability reports. We’ll provide adequate notice with the option for projects to opt-out if we make this change.

### Can I pause or opt-out?

If you do not want to receive further reports, you can either submit a PR by adding the line `disabled: true` to your configuration file to temporarily pause reports, or you can remove your project outright by submitting a PR that deletes your projects/<project>/ directory. If you do this, we will not send you automated unvalidated reports until you re-enable your project or submit a PR to re-introduce your project.

Once you’ve opted-out, you will revert to only receiving vulnerability reports under our standard CVD process.

### Can I send feedback about findings?

Yes, we’d love feedback about findings. Please reply to the emailed reports, and you can comment on the bugs in any way you may like. If you’re not enrolled, please email questions to [oss-scanner-questions@anthropic.com](mailto:oss-scanner-questions@anthropic.com). A human will monitor this mailbox.

### How does attribution work?

It's not required, but if you patch a vulnerability identified by this scanner, we'd appreciate a line in your commit message (or wherever you put credits) with the ID of the report, similar to:

> Discovered by Anthropic's OSS Scanner, as vulnerability `ANT-2026-ABCD1234`.

Including the ID helps us track the impact this scanner has had (e.g., which vulnerabilities we got right and got patched).

### How do you ensure reports reach only a project’s maintainers and cover only their code?

OSS Scanner is designed to share vulnerabilities, so it’s critical it only reports findings to the people who develop and maintain the code.

Every sign-up request is reviewed by a human, who will work to confirm that the request comes from a GitHub account or email belonging to a core maintainer, and we validate that the security contact we send our reports to is indeed a security contact for the project (e.g., because it is listed in `SECURITY.md` or similar). Where we're uncertain, we may contact the project through other means or use independent data sources to confirm. We verify again before any results are sent, so only maintainers who remain eligible receive results. If a project's maintainers or security contact should change, a maintainer can update the sign-up PR with the correct address. We’ll review the change through the same process.

At sign up, we manually validate that the Dockerfile configures the intended repository and is only scoped to the given project. Before sending out reports our harness automatically verifies that each report corresponds to a vulnerability in the given target (vs. any dependencies). Any time a Dockerfile changes between runs, we review the changes before the subsequent runs, so the code being scanned stays scoped to the project.

### How is the data secured?

We follow the same practices as how we hold and manage vulnerabilities found as part of our standard CVD process. Reports are held in an isolated locked-down cloud project available only to Anthropic security staff who need access to reports, in order to develop the scanner and run the program. We run scanning agents only after fully disabling Internet access inside of hardened sandboxes.

### How does this differ from [Claude Security](https://claude.com/product/claude-security)?

Claude Security is our commercial offering that enables users to find and fix vulnerabilities in their source code. It allows enterprise users to easily bring the power of Claude Mythos into their software development lifecycle.

OSS Scanner aims to give open-source maintainers a larger defensive advantage given how critical they are to all other software:

* We use a variety of harnesses and techniques to scan code. We apply additional token-hungry and experimental harnesses to find even deeper bugs.
* We cover the full cost.

### What other support do you offer maintainers?

We offer maintainers [Claude for OSS](https://claude.com/contact-sales/claude-for-oss), which provides free Claude Max 20x subscriptions to help you remediate vulnerabilities and improve your project. Our [Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program) also makes advanced cyber capabilities and reduced blocking classifiers available to qualifying security professionals.

*This project is a collaboration between Anthropic’s Frontier Red Team and Safeguards Research team.*

Changelog

* October 13, 2026: Added further explanation on the eligibility criteria and how we ensure reports only reach maintainers covering their own code.
* October 8, 2026: Launched OSS Scanner.
