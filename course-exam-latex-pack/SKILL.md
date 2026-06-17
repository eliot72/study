---
name: course-exam-latex-pack
description: "Create high-density course exam preparation packs from a textbook, syllabus, notes, and past exam PDFs. Use when Codex must study course materials and generate three aligned LaTeX-compiled PDF handouts: a knowledge-point and problem-solving guide, a classified past-exam practice booklet, and a matching solutions booklet with tactics, full derivations, and pitfalls."
---

# Course Exam LaTeX Pack

## Overview

Build a three-document exam-prep pack from course source materials. The output must feel like a course-specific teaching system, not a generic summary: one shared knowledge map drives the knowledge guide, classified question booklet, and matching solutions booklet.

## Required Outputs

Create a LaTeX project that compiles to three PDFs:

1. `knowledge-guide.pdf`: high-density knowledge points, formulas, method triggers, problem-solving routines, and final exam tactics.
2. `classified-exams.pdf`: past exam questions reorganized by knowledge block and subtopic, preserving year/paper/question provenance.
3. `solutions.pdf`: matching answer booklet with complete solutions, "breakthrough idea" boxes, and "pitfall" boxes.

Use `assets/latex-pack-template/` as the starter project when creating a pack.

## Workflow

1. Inventory the inputs.
   - Identify textbook chapters, syllabus scope, exam papers, answer keys, lecture notes, and any course-specific exam variants.
   - Extract text with PDF tooling, but render sample pages when layout, formulas, tables, or diagrams matter.
   - If formulas extract poorly, use visual inspection and manual reconstruction rather than trusting garbled text.

2. Build the master knowledge map before writing.
   - Read `references/pack-method.md` when deciding the structure.
   - Make a block/subtopic outline that covers nearly all textbook concepts and observed exam points.
   - Add prerequisite or bridge blocks when the course depends on earlier material.
   - Name each block by exam use, not just textbook chapter title.

3. Classify exams into the shared map.
   - Split each exam into atomic questions or subquestions.
   - Assign each item to exactly one primary subtopic and optional secondary tags.
   - Preserve provenance as `[year, paper/variant, question]`.
   - Detect high-frequency templates, rare but high-risk topics, proof styles, and traps.

4. Write the knowledge guide.
   - Start with a whole-course map: the main story, major toolchains, and recurring exam mother-questions.
   - For each subtopic, include: core conclusion, when to use it, standard steps, common transformations, exam signals, traps, and 1-3 representative question links.
   - Keep density high. Prefer compact formulas, bullets, and short tactical paragraphs.

5. Write the classified exam booklet.
   - Follow the exact block/subtopic order of the knowledge guide.
   - Include questions only, with space when useful for practice.
   - Do not solve inside this booklet.
   - Keep numbering local to each subtopic; preserve source labels.

6. Write the solutions booklet.
   - Follow the same block/subtopic order and question numbering as the classified booklet.
   - For each substantial question, use:
     - problem source and prompt;
     - a blue `idea` box for the breakthrough route;
     - clean derivation or proof;
     - boxed final answer when appropriate;
     - a red `pitfall` box for common mistakes, sign/orientation/domain issues, missing hypotheses, or exam-writing advice.
   - For routine items, keep the solution compact but still state the key method.

7. Compile and visually verify.
   - Prefer the LaTeX compile skill or the local project `Makefile`.
   - Use XeLaTeX for Chinese/CJK packs unless the course material is entirely Latin-script.
   - Render representative pages of all three PDFs and check headings, page breaks, formula legibility, source labels, boxes, and page numbers.

## LaTeX Project

To scaffold a new pack, run:

```bash
python path/to/skill/scripts/create_latex_pack.py --output /path/to/output --course "Course Name"
```

Then edit:

- `content/metadata.tex` for course title and author mark.
- `content/knowledge.tex` for the knowledge guide body.
- `content/questions.tex` for the classified exam booklet body.
- `content/solutions.tex` for the solution booklet body.

Compile with:

```bash
make all
```

If `make` is unavailable, compile each root file with XeLaTeX:

```bash
xelatex knowledge-guide.tex
xelatex classified-exams.tex
xelatex solutions.tex
```

## Quality Bar

- The three documents must share one taxonomy and cross-reference each other mentally even when not using LaTeX hyperlinks.
- Coverage should be broad enough that a student can use the pack as the main final-review artifact for the provided scope.
- Do not invent exam questions and present them as real. Mark synthesized drills clearly if the user asks for extras.
- Do not omit low-frequency textbook points without noting why they are out of exam scope.
- Preserve source provenance for every real exam question.
- Keep final PDFs clean: no placeholder text, broken references, clipped formulas, unreadable extracted glyphs, or orphaned section headings.
