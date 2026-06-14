# Assignment 1 · Milestone 1 — Business Brief
**ISBA 2411 · Due Sunday, June 21, 2026 (11:59 PM PT) · Week 1 · Individual (used to form teams) · 400–600 words**

Frame your proposed final team project as a short **business brief**. This is the seed of your
team's whole project — the problem you define here is the one you carry through Milestones 2–5.
Submit as **PDF** via Camino.

> **Why this matters.** A good NLP project starts from a real problem and a clear notion of value,
> *not* from a model. We use these briefs to form teams around the strongest, most feasible
> problems, so write to convince a skeptical reader that yours is worth three months of work.

---

## How to use this template
Write ~400–600 words across the five sections below. Keep each section tight — a paragraph or two.
Replace the *italic prompts* with your own content; they are questions to answer, not text to keep.
A short worked example follows the template so you can see the bar.

---

## 1. Problem  *(≈100 words)*
*What real-world problem are you addressing? Who has it, and how do they handle it today? Why is it
hard or costly without NLP?* Be concrete: name the decision or task that gets better if you succeed.

## 2. Target user / organization  *(≈75 words)*
*Who is the specific user or stakeholder, and in what context do they act? What does a typical day /
workflow look like for them? Avoid "everyone" — name one primary user.*

## 3. Value proposition  *(≈100 words)*
*Why does solving this matter? Quantify the value if you can (time saved, errors avoided, revenue,
risk reduced, people helped). What does "good enough to be useful" look like?*

## 4. NLP hypothesis  *(≈125 words)*
*Which NLP capability could address it — classification, retrieval/RAG, summarization, extraction,
or clustering — and why that one? What data would you need, and is it plausibly obtainable? State an
initial, testable hypothesis (e.g., "A retrieval-augmented assistant over our policy docs can answer
≥70% of tier-1 support questions correctly").* This becomes your Milestone 2 baseline target.

## 5. Risks & governance  *(≈100 words)*
*What could go wrong — bias, privacy, hallucination, misuse, automation harm? Who is affected if the
system is wrong? Name your top two risks and one concrete first step to mitigate each.*

---

## Submission checklist
- [ ] 400–600 words, five sections, exported to **PDF**
- [ ] Names one **specific** user/stakeholder (not "everyone")
- [ ] States a **testable** NLP hypothesis with a rough success target
- [ ] Identifies a **plausible data source** for the proposed capability
- [ ] Names **two concrete risks** and a first mitigation for each

## How this is graded
This brief is scored on the shared milestone rubric — see
[`docs/ISBA2411_Assignment_Rubric.pdf`](../docs/ISBA2411_Assignment_Rubric.pdf). For Milestone 1,
the criteria map roughly to:

| Rubric criterion | In this brief |
|---|---|
| **Execution** | A compelling, *feasible* problem framing with a realistic data plan |
| **Analysis & Insight** | A specific user, quantified value, and a testable hypothesis |
| **Communication** | Clear, well-organized writing with explicit risk/governance reasoning |

---

## Worked example (abridged — yours should be fuller)
> **1. Problem.** Community-clinic intake staff spend ~15 min per patient manually routing free-text
> symptom descriptions to the right department; misroutes delay care and frustrate patients.
>
> **2. Target user.** A front-desk intake coordinator at a 4-clinic nonprofit who processes ~80
> walk-ins/day and is not a clinician.
>
> **3. Value proposition.** Cutting routing time to <2 min and misroutes by half would free ~15
> staff-hours/day across clinics and get patients to the right provider faster.
>
> **4. NLP hypothesis.** A **text classifier** over historical intake notes (we have ~12k labeled by
> final department) can predict department. Hypothesis: a fine-tuned model reaches ≥85% top-1
> accuracy — high enough to suggest a route the coordinator confirms.
>
> **5. Risks & governance.** (a) *Bias* — accuracy may be lower for non-native-English notes;
> mitigation: report per-language accuracy and keep a human in the loop. (b) *Privacy* — notes are
> PHI; mitigation: de-identify before training and keep data on-prem.

---
*The problem you define here is the one your team carries through every later milestone.*
