<!-- source: https://claude.com/resources/guides/claude-science-product-guide/claude-science-product-overview -->

Chapter 039 min read

# Claude Science product overview

9 min read

31 min remaining

Claude Science is an AI daily driver that takes the toil out of science so researchers spend their time on the work only they can do. It's an agentic research app for the digital workflows core to scientific progress, from planning research and running analysis to explaining the results, all through natural language with Claude. It covers the six workflow archetypes that fill a biologist's day—literature review, experiment planning, data management, data analysis, figure generation, and scientific writing—and its starting thesis is to remove the toil between them: the database schemas, format conversions, and package interop that sit between a question and its answer, so the scientist keeps the design decisions and the interpretation.

The product is built first for computational and dry-lab biologists, and Anthropic's early-access program found that wet-lab scientists and PIs adopt it close behind—it extends their computational reach the same way Claude Code did for non-engineers. The starter catalog skews to biology, but the core extends to chemistry, neuroscience, and ML research.

## How it works

Claude Science is a standalone application for macOS and Linux that runs a local daemon with its UI in the browser—the same model as a Jupyter notebook, but the agent is driving. The scientist installs it wherever the data lives: a laptop, a lab Linux box, an HPC login node, or a cloud VM. Data, compute environments, and agents stay on that machine, while the scientist connects from a laptop browser over an SSH tunnel when the daemon is running remotely. When a job needs bigger hardware, Claude Science dispatches it from the same session to the lab's own GPU box, SSH host, SLURM cluster (it auto-detects SLURM and writes the batch directives), or serverless GPU account.

Once installed, agents can be pointed at any local folder, including FASTQ files, AnnData objects, Seurat objects, and connect natively to S3, GCS, GitHub, and institutional literature access. Conda and pip environments are managed per specialist, and sessions, kernels, and artifacts persist across reboots.

## Domain expertise, ready on day one

Claude Science ships with configurable capabilities for common scientific workflows, backed by optional connections to more than sixty scientific databases and roughly 150 curated skills. When a project spans domains, it plans and routes across them automatically. Public databases and other third-party resources are governed by their own licenses and use terms; organizations are responsible for ensuring their use — including commercial use — complies with those terms and their own entitlements. Information about network domains, connectors, and skills can be found in Settings.

Claude Science ships a library of pre-built Python skills that, if enabled, allow Claude to access certain major open scientific databases, so a scientist can ask a question in plain language and Claude writes and executes the query against the source of record, returning results with provenance.

Because these skills run code rather than retrieve documents, Claude can chain them: pull a gene's variants from one database, cross-reference drug interactions in another, and check expression across cell types in a third, inside a single analysis. Each skill is open source, so computational teams can inspect the query logic, pin versions, or extend a skill with their organization's own filters and output formats.

The table below groups them by the kind of question they answer.

### Genes, variants, and annotation

Genes, variants, and annotation skills

| Skill | Source | Use when |
| --- | --- | --- |
| `gene-database` | NCBI Gene / Datasets | Looking up a gene by symbol or ID — RefSeqs, GO terms, genomic location, associated phenotypes, batch retrieval. |
| `biothings-database` | BioThings.io (MyGene, MyVariant, MyChem, MyDisease) | Resolving identifiers across databases or pulling aggregated annotation for a gene, variant, compound, or disease in one call. |
| `ena-database` | European Nucleotide Archive | Retrieving raw sequence data — FASTQ reads, assemblies, sample metadata — by accession. |
| `harmonizome-database` | Harmonizome | Asking what a gene is associated with across 170+ functional genomics resources at once. |

### Expression and single-cell

Expression and single-cell skills

| Skill | Source | Use when |
| --- | --- | --- |
| `cellxgene-census` | CZ CELLxGENE Census | Filtering 125M+ cells by type, tissue, or disease and pulling expression matrices straight into scanpy or PyTorch. |
| `immgen-database` | ImmGen | Checking expression of a gene across mouse immune cell populations. |
| `allen-brain-database` | Allen Brain Atlas | Querying gene expression, connectivity, or spatial transcriptomics across mouse and human brain regions. |

### Oncology

Oncology skills

| Skill | Source | Use when |
| --- | --- | --- |
| `cosmic-database` | COSMIC | Searching somatic mutations, the Cancer Gene Census, mutational signatures, or fusion events. Requires institutional authentication. |
| `tcia-database` | The Cancer Imaging Archive | Pulling DICOM imaging series from public cancer imaging collections for radiomics or model training. |

### Pharmacology and safety

Pharmacology and safety skills

| Skill | Source | Use when |
| --- | --- | --- |
| `clinpgx-database` | ClinPGx (PharmGKB) | Checking gene–drug interactions, CPIC dosing guidelines, or allele function for a pharmacogenomic question. |
| `fda-database` | openFDA | Searching adverse event reports, recalls, drug labels, device 510(k)/PMA records, or UNII identifiers. |

### Metabolomics

Metabolomics skills

| Skill | Source | Use when |
| --- | --- | --- |
| `hmdb-database` | Human Metabolome Database | Looking up any of 220K+ human metabolites — properties, biomarker associations, NMR/MS spectra, pathway membership. |
| `metabolomics-workbench-database` | Metabolomics Workbench | Searching 4,200+ public metabolomics studies, RefMet nomenclature, or running m/z lookups. |

### Neuroscience

Neuroscience skills

| Skill | Source | Use when |
| --- | --- | --- |
| `neuromorpho-database` | NeuroMorpho.Org | Retrieving neuron morphology reconstructions and morphometrics by species, brain region, or cell type. |
| `openneuro-database` | OpenNeuro | Finding and pulling BIDS-formatted MRI, fMRI, EEG, MEG, or PET datasets. |

### Multi-database toolkits

For exploratory work that crosses several sources, Claude can also load broader Python toolkits as skills:

Multi-database toolkit skills

| Skill | Coverage | Use when |
| --- | --- | --- |
| `bioservices` | 40+ services — UniProt, ChEMBL, PubChem, Reactome, QuickGO, KEGG, Ensembl, BioMart, and more | Running pathway analysis or ID mapping across many providers through one unified interface. |
| `gget` | 20+ databases — Ensembl, UniProt, NCBI, ARCHS4, Enrichr, OpenTargets, PDB, AlphaFold, BLAST | Quick one-liner lookups: gene info, enrichment, reference genome download, a fast BLAST. |
| `biopython` (Bio.Entrez) | All NCBI Entrez databases — PubMed, Gene, Nucleotide, Protein, SRA, Taxonomy, Assembly, BioProject | Anything that lives behind NCBI E-utilities and isn't covered by a more specific skill above. |
| `hmmer` | Pfam, UniProtKB, Reference Proteomes | Profile and sequence searches — phmmer, hmmscan, hmmsearch, jackhmmer — for domain identification and remote homology. |
| `foldseek` | AlphaFold DB, PDB100, ESMAtlas, CATH | Searching by 3D structure rather than sequence to find structural homologs the sequence would miss. |

The catalog is opinionated but open: a lab can save any working pipeline as a reusable skill, build a custom specialist for its own methods from inside any session, or wrap an internal API once so every future session inherits it.

## Analysis that holds up under review

Five design choices make Claude Science suitable for scientific work.

### Persistent kernels

Agents load a dataset into a persistent Python or R kernel once; from then on they're exploring it, not re-loading it. Variables, dataframes, and loaded models stay in memory across the whole analysis. Agents see their own plots—every figure generated is fed back into the agent's context, so it runs QC on its own output, spots the outlier cluster in its own UMAP, and filters it before moving on.

### Full provenance on every artifact

Figures, tables, reports, and notebooks are first-class objects, not files to dig up afterward. Each ships with four layers of history: a human-readable description of what was done, the exact reproducible code that produced it, the conversation itself and the reasoning that led there, and a snapshot of every package and version used.

### A background reviewer

A separate reviewer agent reads each session's transcript while the primary agent works and flags any claim it cannot trace to evidence. Findings surface inline at the suspect sentence and the agent fixes them before finishing. The reviewer runs every session by default and can be triggered manually at any point.

### Plans before actions, permissions you can see

Claude Science drafts each task as a step-by-step plan and waits for approval before executing; the plan stays visible as a checklist and can be edited or scoped down while work runs. Whenever an agent needs to reach a new website, open a folder, or run code, the same approval card appears—allow it once, for this project, or always—and every decision can be reviewed or revoked from a single permissions screen. An OS-level sandbox with deny-by-default network egress sits underneath, and a human-approval broker gates code execution, network grants, host file access, deletions, MCP tools, remote compute, and skill persistence.

### Built-in biosecurity safeguards

Biology is a dual-use domain, and Claude Science ships with safeguards specific to it: biosecurity rules are written unconditionally into every agent's system prompt, a per-turn bio trajectory classifier runs in the binary and cannot be disabled, and the product completed external red-teaming and Anthropic Safeguards review before public release. These sit on top of the runtime sandbox and approval broker as an additional layer for organizations whose risk and compliance teams will ask exactly this question.

## Working with results

Scientists iterate on outputs in plain language. Click directly on a figure to drop an annotation, or just ask: drop the gridlines, make the axis log scale, switch to a colorblind-safe palette, or run it again without the outliers. The agent reads the exact code that produced the artifact and edits surgically rather than regenerating something that looks roughly right. Every version is saved with its provenance intact. From any point a scientist can fork the session to explore two approaches in parallel without losing the original thread.

Built-in scientific renderers display protein structures, DNA sequences, multiple sequence alignments, genome tracks, and small molecules natively, alongside spreadsheets, interactive HTML, PDFs, notebooks, and live LaTeX and Markdown for manuscript editing.

## MCP connectors and extensions

Claude Science is MCP-native: any MCP server—data warehouses, ELNs, ticketing, and internal services—connects, and tools the rest of the organization already uses work here, too.

**Scientific databases:** Basecamp Research, Phylo, protocols.io, ToolUniverse, Open Targets, Wiley, Clarivate, Owkin

**Lab and partner tools:** Benchling, Modal, SandboxAQ, Revvity Signals, Boltz, Inductive Bio, Latch Bio, Synthesize Bio, Helix, 10x Genomics, Medidata, BioRender

### When to use a skill vs. a connector

Use a connector when the answer lives in the organization's own systems, such as an ELN, a CTMS, or a regulatory document repository, and entitlements matter. Use a scientific data skill when the answer lives in the public record and the value is in querying it precisely, reproducibly, and in combination with other sources. Most real questions use both: Claude pulls the internal context through a connector, grounds it against public reference data through a skill, and returns an analysis the scientist can verify line by line.
