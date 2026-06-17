# Three-Pack Method

## Shape Learned From The Reference Pack

The reference pack is a coordinated three-volume system:

- The knowledge guide begins with a course-level map, then moves through numbered blocks and subtopics.
- The practice booklet uses the same block/subtopic order and contains only classified past questions.
- The solutions booklet mirrors the practice booklet and teaches each item through method recognition, execution, and pitfalls.

The design goal is not "summarize everything" but "turn the course into an exam operating system."

## Master Map

Create one taxonomy and reuse it everywhere.

1. Course map: identify 1-3 main storylines that explain how the course fits together.
2. Blocks: 5-9 major units is usually readable for a final review pack.
3. Subtopics: name each subtopic by the exam action students must perform.
4. Bridge block: add a zero block for prerequisite tools when earlier material is repeatedly needed.
5. Final block: add a proof, synthesis, or last-check block when exams contain integrative or theoretical questions.

Each subtopic should carry:

- textbook source range;
- key definitions and theorems;
- formula/tool list;
- exam triggers;
- standard routine;
- common traps;
- representative past questions.

## Knowledge Guide Writing Pattern

For each subtopic, prefer this order:

1. `Core`: the minimum theory and formulas.
2. `Use When`: signals in the prompt that call this method.
3. `Routine`: numbered steps for solving.
4. `Exam Variants`: common twists, boundary cases, or proof versions.
5. `Pitfalls`: mistakes that cost points.
6. `Past Exam Links`: compact source labels.

Write densely. Avoid long textbook exposition unless the concept is a repeated bottleneck. If a theorem is used mainly as a tool, state the conditions and the executable form.

## Classified Exam Booklet Pattern

The question booklet is for practice, so it should not reveal the method too early.

- Group by block and subtopic.
- Keep original mathematical content faithful.
- Preserve source tags like `[2023-2024, Final, 7]` or `[21-22 H, 5]`.
- Keep diagrams or tables if needed; redraw them cleanly in LaTeX or include cropped images only when redrawing would risk distortion.
- Add answer blanks or vertical space only when it improves usability.
- If one original question spans multiple skills, place it under the primary skill and add secondary tags in a short note.

## Solutions Booklet Pattern

Each solution should make the reusable tactic visible.

Use a blue idea box for the method:

- what type of problem this is;
- why the chosen theorem/formula applies;
- the key substitution, transformation, invariant, or proof strategy.

Then give a clean solution:

- verify hypotheses before applying theorems;
- define auxiliary functions or variables explicitly;
- show important algebra and transformations;
- box final answers;
- cite earlier conclusions when a multi-part question depends on them.

Use a red pitfall box for:

- sign/orientation mistakes;
- boundary/domain/end-point omissions;
- false theorem conditions;
- common formula confusions;
- denominator-zero or degenerate cases;
- grading wording such as "must state continuity" or "must check point lies on surface."

## Coverage Audit

Before finalizing, make a small coverage table:

- rows: textbook chapters or syllabus items;
- columns: included in knowledge guide, has past-question coverage, appears in solutions, notes.

If a topic has no past exam question, still include it in the knowledge guide when it is in scope, and label it as "textbook/syllabus only" or add a clearly marked synthesized drill only if requested.

## Visual Style

Use an A4 article layout with:

- compact margins;
- table of contents;
- running header with course name and document type;
- page number footer;
- Chinese-friendly fonts when needed;
- restrained color: blue for method/idea boxes, red for pitfalls, black text for main content.

Avoid decorative covers. The first page should immediately show the document title and table of contents or course map.
