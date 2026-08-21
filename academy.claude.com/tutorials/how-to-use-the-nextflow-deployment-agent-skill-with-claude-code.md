<!-- source: https://academy.claude.com/tutorials/how-to-use-the-nextflow-deployment-agent-skill-with-claude-code -->

## **What is the Nextflow Deployment agent skill?**

This skill enables Claude Code to deploy nf-core Nextflow pipelines for common omics analyses (RNA-seq, variant calling, ATAC-seq) by automating environment validation, data acquisition from GEO/SRA, sample sheet generation, and pipeline execution — turning natural language prompts into reproducible Nextflow workflows.

Check out the [Skill README(opens in new tab)](https://github.com/anthropics/life-sciences/releases/download/v1.1.1/nextflow-development-v1.1.1.zip) for more information.

## **Who should use the Nextflow Deployment agent skill?**

This agent skill is designed for bench scientists and researchers who want to run nf-core Nextflow pipelines and desire to execute standardized sequencing analyses or reanalyze public datasets without writing code from scratch.

## **How to access the agent skill in Claude Code**

Command

`/plugin marketplace add anthropics/life-sciences`

`/plugin install nextflow-development@life-sciences`
