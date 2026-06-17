# Course Exam LaTeX Pack Skill

> English version follows the Chinese version.

## 中文说明

### 项目简介

`course-exam-latex-pack` 是一个 Codex skill，用来把某门课程的课本、讲义、考纲、历年真题和答案整理成一套高密度期末复习资料。它的目标不是生成普通摘要，而是学习课程材料和真题风格后，建立一套统一的“课程知识图谱”，并据此生成三份互相对齐的 LaTeX/PDF 讲义：

1. `knowledge-guide.pdf`：知识点讲解汇编，包含高频考点、公式、定理条件、做题技巧、题型触发信号、常见陷阱。
2. `classified-exams.pdf`：真题分类汇编，把历年真题按知识板块和考点重新组织，保留年份、试卷、题号来源。
3. `solutions.pdf`：配套答案整理，按真题汇编的顺序逐题讲解，突出破题思路、规范步骤和避坑指南。

这个 skill 特别适合用于大学课程期末复习资料制作，例如数学、物理、计算机、经济学、工程类课程等，只要用户能提供教材范围和真题资料，就可以按统一流程生成三件套。

### 核心理念

本 skill 的核心逻辑来自一套高质量课程复习资料的制作方法：

- 先建立“全册地图”，用 1 到 3 条主线解释课程结构。
- 再按考试动作划分板块和子考点，而不是机械照搬课本目录。
- 三份资料共享同一套板块顺序和考点分类。
- 真题本只放题目，不提前泄露解法。
- 解析本逐题呈现“破题思路 - 完整步骤 - 避坑指南”。
- 所有真实真题必须保留来源标签，例如 `[2023-2024, Final, 7]`。
- 对课本中有范围但真题中较少出现的知识点，也应在知识讲义中说明其地位。

### 目录结构

```text
course-exam-latex-pack/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   └── pack-method.md
├── scripts/
│   └── create_latex_pack.py
└── assets/
    └── latex-pack-template/
        ├── Makefile
        ├── knowledge-guide.tex
        ├── classified-exams.tex
        ├── solutions.tex
        └── content/
            ├── metadata.tex
            ├── common.tex
            ├── knowledge.tex
            ├── questions.tex
            └── solutions.tex
```

### 文件说明

- `SKILL.md`：Codex skill 的主说明文件，定义触发场景、工作流程、质量标准和输出要求。
- `references/pack-method.md`：详细制作方法，包括如何构建课程知识图谱、如何分类真题、如何写知识讲义和答案解析。
- `scripts/create_latex_pack.py`：用于快速生成三份 PDF 项目的脚手架脚本。
- `assets/latex-pack-template/`：LaTeX 模板，内置三份文档入口、公共样式、蓝色“破题思路”框和红色“避坑指南”框。
- `agents/openai.yaml`：Codex UI metadata。

### 安装到 Codex

如果要让 Codex 自动发现这个 skill，可以把整个文件夹复制到本机 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force .\course-exam-latex-pack "$env:USERPROFILE\.codex\skills\course-exam-latex-pack"
```

复制后，在 Codex 中可以通过下面这类提示触发：

```text
Use $course-exam-latex-pack to turn this textbook and these past exam papers into three LaTeX-compiled PDF handouts.
```

也可以直接用中文：

```text
使用 $course-exam-latex-pack，读取我提供的课本和真题，生成知识点讲解汇编、真题分类汇编和配套答案解析三份 PDF。
```

### 快速生成 LaTeX 项目

进入本文件夹后运行：

```powershell
python .\scripts\create_latex_pack.py --output .\demo-pack --course "课程名称" --author "署名"
```

生成的项目包含：

```text
demo-pack/
├── knowledge-guide.tex
├── classified-exams.tex
├── solutions.tex
├── Makefile
└── content/
    ├── metadata.tex
    ├── common.tex
    ├── knowledge.tex
    ├── questions.tex
    └── solutions.tex
```

其中：

- `content/knowledge.tex`：写知识点讲解汇编正文。
- `content/questions.tex`：写真题分类汇编正文。
- `content/solutions.tex`：写答案解析正文。
- `content/common.tex`：公共 LaTeX 样式与自定义命令。
- `content/metadata.tex`：课程名与页眉署名。

### 编译 PDF

推荐使用 XeLaTeX，尤其是中文课程材料：

```powershell
cd .\demo-pack
latexmk -xelatex knowledge-guide.tex classified-exams.tex solutions.tex
```

如果没有 `latexmk`，也可以分别编译：

```powershell
xelatex knowledge-guide.tex
xelatex classified-exams.tex
xelatex solutions.tex
```

生成结果：

```text
knowledge-guide.pdf
classified-exams.pdf
solutions.pdf
```

### 推荐工作流

1. 收集输入材料：课本 PDF、讲义、考纲、历年真题、答案或评分标准。
2. 先抽取课程知识范围，建立“全册地图”。
3. 将课程拆成若干板块，例如“基础工具”“核心理论”“计算题”“证明题”“综合题”等。
4. 把每道真题切分为原子问题，标注年份、卷别、题号和知识点。
5. 写 `knowledge-guide.pdf`：先主线，后板块；每个考点写核心结论、使用信号、标准套路、陷阱和代表真题。
6. 写 `classified-exams.pdf`：按同样板块顺序放题，不写解答。
7. 写 `solutions.pdf`：与真题本完全对齐，逐题写破题思路、完整推导、最终答案和避坑提醒。
8. 编译三份 PDF，渲染抽查页面，确认公式、中文、页眉页脚、题号和盒子样式正常。

### 质量标准

- 三份 PDF 必须共享同一套板块和考点顺序。
- 知识点覆盖应尽量接近用户提供材料的全部范围。
- 真实真题不得编造来源；额外自拟题必须明确标注。
- 答案解析不能只给答案，要体现可复用的解题策略。
- LaTeX 输出不能包含占位符、乱码、残缺公式或断裂标题。
- 对于图形、表格、复杂公式，文本抽取不可靠时应进行视觉核对或手动重构。

### 维护建议

- 如果某门课有固定模板，可以在 `assets/latex-pack-template/` 的基础上扩展。
- 如果某类课程有特定整理方法，可以新增 `references/` 文档，例如 `references/math-proof-courses.md` 或 `references/programming-courses.md`。
- 修改 `SKILL.md` 后建议运行 Codex skill validator 检查 frontmatter 和命名规范。

---

## English Documentation

### Overview

`course-exam-latex-pack` is a Codex skill for turning a course textbook, lecture notes, syllabus, past exams, and answer keys into a dense final-review package. Instead of producing a generic summary, it learns the course structure and exam patterns, builds a shared knowledge taxonomy, and generates three aligned LaTeX/PDF handouts:

1. `knowledge-guide.pdf`: a knowledge-point and problem-solving guide with high-frequency topics, formulas, theorem conditions, method triggers, routines, and pitfalls.
2. `classified-exams.pdf`: a classified past-exam practice booklet, reorganized by knowledge block and subtopic while preserving source provenance.
3. `solutions.pdf`: a matching solution booklet with full reasoning, breakthrough ideas, clean derivations, final answers, and pitfall notes.

This skill is useful for university final-exam preparation packs across subjects such as mathematics, physics, computer science, economics, engineering, and other courses with textbooks and past papers.

### Core Idea

The skill follows a three-volume study-pack method:

- Build a whole-course map first, using 1 to 3 main storylines.
- Organize knowledge by exam actions and problem types, not merely by textbook chapters.
- Reuse the same block/subtopic taxonomy across all three documents.
- Keep the practice booklet question-only.
- Make the solutions booklet teach method recognition through "breakthrough idea" and "pitfall" boxes.
- Preserve source labels for every real exam question, such as `[2023-2024, Final, 7]`.
- Include in-scope textbook concepts even if they are low-frequency in past exams, while noting their exam status.

### Directory Structure

```text
course-exam-latex-pack/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   └── pack-method.md
├── scripts/
│   └── create_latex_pack.py
└── assets/
    └── latex-pack-template/
        ├── Makefile
        ├── knowledge-guide.tex
        ├── classified-exams.tex
        ├── solutions.tex
        └── content/
            ├── metadata.tex
            ├── common.tex
            ├── knowledge.tex
            ├── questions.tex
            └── solutions.tex
```

### File Guide

- `SKILL.md`: the main Codex skill instructions, including trigger conditions, workflow, output requirements, and quality bar.
- `references/pack-method.md`: the detailed production method for knowledge maps, classified exam booklets, and solutions.
- `scripts/create_latex_pack.py`: a scaffolding script for creating a new three-PDF LaTeX project.
- `assets/latex-pack-template/`: a reusable LaTeX template with three document roots, shared styling, blue idea boxes, and red pitfall boxes.
- `agents/openai.yaml`: Codex UI metadata.

### Install Into Codex

To make Codex discover this skill automatically, copy this folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\course-exam-latex-pack "$env:USERPROFILE\.codex\skills\course-exam-latex-pack"
```

Then invoke it with prompts such as:

```text
Use $course-exam-latex-pack to turn this textbook and these past exam papers into three LaTeX-compiled PDF handouts.
```

### Scaffold A LaTeX Pack

From this folder, run:

```powershell
python .\scripts\create_latex_pack.py --output .\demo-pack --course "Course Name" --author "Author Mark"
```

The generated project contains:

```text
demo-pack/
├── knowledge-guide.tex
├── classified-exams.tex
├── solutions.tex
├── Makefile
└── content/
    ├── metadata.tex
    ├── common.tex
    ├── knowledge.tex
    ├── questions.tex
    └── solutions.tex
```

Edit:

- `content/knowledge.tex` for the knowledge guide.
- `content/questions.tex` for the classified exam booklet.
- `content/solutions.tex` for the solution booklet.
- `content/common.tex` for shared LaTeX styles and commands.
- `content/metadata.tex` for course title and header author mark.

### Compile PDFs

XeLaTeX is recommended, especially for Chinese/CJK course materials:

```powershell
cd .\demo-pack
latexmk -xelatex knowledge-guide.tex classified-exams.tex solutions.tex
```

If `latexmk` is unavailable, compile each root file directly:

```powershell
xelatex knowledge-guide.tex
xelatex classified-exams.tex
xelatex solutions.tex
```

Expected outputs:

```text
knowledge-guide.pdf
classified-exams.pdf
solutions.pdf
```

### Recommended Workflow

1. Collect inputs: textbook PDFs, lecture notes, syllabus, past exams, answer keys, and grading rubrics.
2. Extract the course scope and build a whole-course map.
3. Divide the course into blocks such as prerequisites, core theory, calculation methods, proof questions, and synthesis.
4. Split every exam into atomic questions and label each item with year, paper variant, question number, and knowledge tags.
5. Write `knowledge-guide.pdf`: start with the course story, then cover each block with core facts, triggers, routines, pitfalls, and representative exam links.
6. Write `classified-exams.pdf`: place questions in the same block order, without solutions.
7. Write `solutions.pdf`: align exactly with the practice booklet and include idea boxes, derivations, final answers, and pitfall notes.
8. Compile all three PDFs and visually inspect representative pages for formulas, CJK text, headers, footers, numbering, and box styling.

### Quality Bar

- All three PDFs must share the same taxonomy and subtopic order.
- Coverage should approach the full scope of the provided materials.
- Never fabricate real exam provenance. Clearly label synthesized drills if added.
- Solutions should teach reusable strategy, not merely provide final answers.
- LaTeX output must not contain placeholders, garbled text, broken formulas, or orphaned headings.
- Use visual inspection when text extraction is unreliable for diagrams, tables, or formulas.

### Maintenance Notes

- Extend `assets/latex-pack-template/` if a course family needs a stable custom layout.
- Add specialized references under `references/` for course-specific production rules.
- After editing `SKILL.md`, run a Codex skill validator to check frontmatter and naming conventions.
