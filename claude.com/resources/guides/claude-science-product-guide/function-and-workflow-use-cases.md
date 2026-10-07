<!-- source: https://claude.com/resources/guides/claude-science-product-guide/function-and-workflow-use-cases -->

Chapter 064 min read

# Function and workflow use cases

4 min read

13 min remaining

Claude Science was built to handle a scientist's most analysis-heavy work and repetitive workstreams. Claude Science handles the pipeline assembly, the database wrangling, and the figure iteration so your time goes to the design decisions and results interpretation. The sections below show what that looks like across the research lifecycle, with the adjacent Claude surfaces noted where the work crosses into document and submission territory.

## Discover and plan

Early-stage work is reading, reconciling, and designing—across literature, public databases, and the lab's prior results. Claude Science compresses that cycle with:

* Literature review and synthesis across primary sources, with citation verification by the background reviewer
* Target and indication assessment from PubMed, ChEMBL, ClinicalTrials.gov, Open Targets, and internal program files
* Experiment and protocol design, construct design, and assembly strategy for ordering
* Competitive trial scans cross-referenced with preclinical model availability
* Hypothesis generation against pathway and ontology references

## Analyze

Analysis is where most of the toil lives. Claude Science runs end-to-end pipelines with kernels that persist, agents that QC their own outputs, and branching for alternative approaches:

* Single-cell RNA-seq clustering, marker identification, and treatment-response analysis
* Genomics from FASTQ through alignment, QC, and variant calling
* CRISPR screen design and analysis
* Proteomics quantitation and interpretation, protein structure prediction, and homolog search
* Cheminformatics: ADMET prediction, similarity search, structural alert flagging
* Phylogenetic and evolutionary analysis
* Parameter sweeps and ML modeling dispatched to SLURM or remote GPU

## Polish and publish

Results become defensible outputs: figures with provenance, methods sections that match the code, and manuscripts edited in place. Claude Science covers:

* Surgical figure iteration in plain language with every version saved
* Methods-section drafting from the artifact's provenance bundle
* Manuscript drafting and editing with live LaTeX and Markdown rendering
* Progress reports and PI briefings synthesized from session history and lab notes

## Adjacent document and regulatory work *(Cowork, Microsoft 365)*

Once results leave the lab, the surrounding Claude surfaces pick up the document load with qualified human review before anything enters a regulated record:

* Protocol and synopsis drafting against the sponsor shell, CSR section drafting from TLFs
* CTD module authoring and gap analysis against current guidance
* SAE narrative drafting and QC, medical information response drafting
* SOP drafting, deviation write-ups, and inspection-readiness summaries
