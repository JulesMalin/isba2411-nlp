# ISBA 2411 — Natural Language Processing
**Santa Clara University · Leavey School of Business · Summer 2026**

Course companion repository. This repo links to the publishers' official, openly licensed
notebooks (it does **not** redistribute the textbooks), maps each notebook to the weekly
schedule, and houses the Final Team Project **milestone starter notebooks** your team will build on.

> **Texts.** Jurafsky & Martin, *Speech and Language Processing* (J&M, 3rd-ed. draft released Jan 6, 2026 — reading only, no code repo) ·
> Alammar & Grootendorst, *Hands-On Large Language Models* (HOLLM) ·
> Tunstall, von Werra & Wolf, *Natural Language Processing with Transformers* (Tunstall).

## How to use this repo
- **Publisher notebooks** are linked below — open any chapter directly in Google Colab with the **▶ Colab** link (nothing to install).
- **Milestone starters** live in [`/milestones`](./milestones). Each team copies these into their own project repo and fills in the `TODO` cells against *their* dataset.
- **Data**: see [`/data`](./data) for the shared corpora (e.g., FOMC transcripts) and where to place your team's dataset.
- Run everything on **Google Colab** (included in your SCU Google Suite) or the **SCU WAVE** cluster for heavier jobs.

## Weekly notebook map
J&M is reading-only (no companion code). HOLLM and Tunstall links open the exact chapter notebook.

| Wk | Theme | J&M (read) | HOLLM notebook | Tunstall notebook | Assignment |
|----|-------|-----------|----------------|-------------------|------------|
| 1 | NLP as a Socio-Technical System | J&M Ch. 2–3 | [Ch 1](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter01/Chapter%201%20-%20Introduction%20to%20Language%20Models.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter01/Chapter%201%20-%20Introduction%20to%20Language%20Models.ipynb) | [Ch 1](https://github.com/nlp-with-transformers/notebooks/blob/main/01_introduction.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/01_introduction.ipynb) | Assignment 1 · Milestone 1: Business Brief |
| 2 | Language as Structured Data | J&M Ch. 17–18 | [Ch 2](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter02/Chapter%202%20-%20Tokens%20and%20Token%20Embeddings.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter02/Chapter%202%20-%20Tokens%20and%20Token%20Embeddings.ipynb) | [Ch 4](https://github.com/nlp-with-transformers/notebooks/blob/main/04_multilingual-ner.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/04_multilingual-ner.ipynb) | Team Update |
| 3 | Supervised Learning for NLP | J&M Ch. 4 | [Ch 4](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter04/Chapter%204%20-%20Text%20Classification.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter04/Chapter%204%20-%20Text%20Classification.ipynb) | [Ch 2](https://github.com/nlp-with-transformers/notebooks/blob/main/02_classification.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/02_classification.ipynb) | Assignment 2 · Milestone 2: Baseline & Representation |
| 4 | Text Retrieval & Deep Learning Intro | J&M Ch. 6 | [Ch 8](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter08/Chapter%208%20-%20Semantic%20Search.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter08/Chapter%208%20-%20Semantic%20Search.ipynb) | [Ch 6](https://github.com/nlp-with-transformers/notebooks/blob/main/06_summarization.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/06_summarization.ipynb) | Team Update |
| 5 | Deep Learning & Topic Modeling | J&M Ch. 8 | [Ch 5](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter05/Chapter%205%20-%20Text%20Clustering%20and%20Topic%20Modeling.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter05/Chapter%205%20-%20Text%20Clustering%20and%20Topic%20Modeling.ipynb) | [Ch 3](https://github.com/nlp-with-transformers/notebooks/blob/main/03_transformer-anatomy.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/03_transformer-anatomy.ipynb) | Assignment 3 · Milestone 3: Model Adaptation |
| 6 | Embeddings & Midterm | J&M Ch. 5 | [Ch 10](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter10/Chapter%2010%20-%20Creating%20Text%20Embedding%20Models.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter10/Chapter%2010%20-%20Creating%20Text%20Embedding%20Models.ipynb) | — | Team Update (Jul 21) · Midterm (Jul 23) |
| 7 | Language Models & Transformers | J&M Ch. 7, 10 | [Ch 3](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter03/Chapter%203%20-%20Looking%20Inside%20LLMs.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter03/Chapter%203%20-%20Looking%20Inside%20LLMs.ipynb) | [Ch 10](https://github.com/nlp-with-transformers/notebooks/blob/main/10_transformers-from-scratch.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/10_transformers-from-scratch.ipynb) | Assignment 4 · Milestone 4: System Prototype |
| 8 | LMs, Generative AI & RAG | J&M Ch. 11 | [Ch 7](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter07/Chapter%207%20-%20Advanced%20Text%20Generation%20Techniques%20and%20Tools.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter07/Chapter%207%20-%20Advanced%20Text%20Generation%20Techniques%20and%20Tools.ipynb) · [Ch 9](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter09/Chapter%209%20-%20Multimodal%20Large%20Language%20Models.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter09/Chapter%209%20-%20Multimodal%20Large%20Language%20Models.ipynb) | [Ch 5](https://github.com/nlp-with-transformers/notebooks/blob/main/05_text-generation.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/05_text-generation.ipynb) · [Ch 7](https://github.com/nlp-with-transformers/notebooks/blob/main/07_question-answering.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/07_question-answering.ipynb) | Team Update |
| 9 | Evaluation, Ethics & Responsible AI | J&M Ch. 9 | — | [Ch 9](https://github.com/nlp-with-transformers/notebooks/blob/main/09_few-to-no-labels.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/09_few-to-no-labels.ipynb) | Assignment 5 · Milestone 5: Final System & Demo (due) |
| 10 | Final Presentations · Operationalizing | — | [Ch 11](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter11/Chapter%2011%20-%20Fine-Tuning%20BERT.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter11/Chapter%2011%20-%20Fine-Tuning%20BERT.ipynb) · [Ch 12](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter12/Chapter%2012%20-%20Fine-tuning%20Generation%20Models.ipynb) · [▶ Colab](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter12/Chapter%2012%20-%20Fine-tuning%20Generation%20Models.ipynb) | [Ch 8](https://github.com/nlp-with-transformers/notebooks/blob/main/08_model-compression.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/08_model-compression.ipynb) · [Ch 11](https://github.com/nlp-with-transformers/notebooks/blob/main/11_future-directions.ipynb) · [▶ Colab](https://colab.research.google.com/github/nlp-with-transformers/notebooks/blob/main/11_future-directions.ipynb) | Final Presentations (Aug 18 & 20) |

### Notebook alignment
Readings have been **aligned to the books' actual chapter content** (e.g., Week 3 → HOLLM Ch. 4 / Tunstall Ch. 2 for text classification; Week 6 → HOLLM Ch. 10 for embeddings; Week 7 → HOLLM Ch. 3 for transformer internals). J&M is reading-only (no companion code).

J&M readings are aligned to the **current Jan 6, 2026 draft** numbering (e.g., Embeddings = Ch. 5, Transformers = Ch. 8, LLMs = Ch. 7, IR & RAG = Ch. 11, alignment/RLHF = Ch. 9). Note that **J&M Ch. 1 (Introduction) is an unreleased placeholder** — it appears in the table of contents but has no PDF, so it is not assigned.

A couple of weeks intentionally show **"—"** for one publisher because that book has no matching chapter: Tunstall has no standalone embeddings chapter (Week 6), and neither book has a dedicated evaluation/ethics chapter (Week 9) — that material lives in **J&M Ch. 9 (Post-training: alignment)**.

## Final Team Project milestones
Five sequenced assignments, each applying that part of the course to your team's own project.
Topic is open — any task that fits a *baseline → measured improvement* frame.

| Assignment | Milestone | Week | Starter |
|---|---|---|---|
| 1 | Business Brief | 1 | [`milestones/Milestone1_Business_Brief.md`](./milestones/Milestone1_Business_Brief.md) |
| 2 | Project Baseline & Representation | 3 | [`Milestone2_Baseline_and_Representation.ipynb`](./milestones/Milestone2_Baseline_and_Representation.ipynb) · worked example: [`Milestone2_FOMC_representation_comparison.ipynb`](./milestones/Milestone2_FOMC_representation_comparison.ipynb) |
| 3 | Model Adaptation Experiment | 5 | [`milestones/Milestone3_Model_Adaptation.ipynb`](./milestones/Milestone3_Model_Adaptation.ipynb) |
| 4 | System Prototype | 7 | [`milestones/Milestone4_System_Prototype.ipynb`](./milestones/Milestone4_System_Prototype.ipynb) |
| 5 | Final System & Demo | 9 (present Aug 18 & 20) | [`milestones/Milestone5_Final_Deliverable.md`](./milestones/Milestone5_Final_Deliverable.md) |

## Course documents
Reference documents for the course live in [`/docs`](./docs):

- [Syllabus](./docs/ISBA2411_NLP_Syllabus_Summer2026.pdf) — course policies, schedule, grading
- [Assignment descriptions](./docs/ISBA2411_Assignment_Descriptions.pdf) — the five assignments in detail
- [Team Project Rubric](./docs/ISBA2411_Team_Project_Rubric.pdf) — how the Final Team Project milestones are graded
- [Weekly learning outcomes](./docs/ISBA2411_Weekly_Learning_Outcomes.pdf) — what you should be able to do each week

## Setup
```bash
pip install -r requirements.txt
```
On Colab, run the install cell at the top of each milestone notebook instead.

## Attribution & licensing
The linked publisher repositories are released under the **Apache License 2.0**:
- HOLLM — https://github.com/HandsOnLLM/Hands-On-Large-Language-Models
- Tunstall — https://github.com/nlp-with-transformers/notebooks

This repo links to (and may fork) those notebooks under that license; it does **not** contain
the textbooks themselves. Course materials authored here © Professor Malin, Santa Clara University.
