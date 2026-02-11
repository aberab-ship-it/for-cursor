# 🧠 **Context Learning Benchmark (CLB) – Reviewer Guide**

This guide defines the full evaluation criteria for reviewing CLB tasks. Each task must satisfy all dimensions described below to ensure:

* determinism  
* context learning validity  
* evaluation reliability  
* consistency across thousands of tasks

Use this document when reviewing any task prior to approval. 

Ideal review time \- **2 hours/task**

# 📘 **Reviewer Mindset & Action Threshold**

Reviewers must adopt a high-scrutiny, "fail-fast" mindset. The CLB aims for exceptionally robust and reliable tasks, and even minor deviations can compromise evaluation validity.

**Action Threshold:**

| Review Finding | Action | Rationale |
| :---- | :---- | :---- |
| **Any** deviation from the criteria in sections 1-9 (e.g., ambiguous wording, slightly off-schema output, non-perfect alignment, minor formatting errors). | **Move task to "Requested Changes"** | Ensures maximal task quality and eliminates potential sources of model misinterpretation or evaluation error. Only tasks that meet **all** criteria perfectly should be approved. |
| Critical structural or logical flaw (e.g., solvable without context, contradictory rules, broken checker). | **Move task to "Requested Changes"** | Requires fundamental rework. |

---

# 📘 **1\. Prompt Quality**

A CLB Prompt must:

1. **Force use of the context only** – Task must be unsolvable without reading the Gold Context.  
     
2. **Produce a deterministic, checkable output** – No open-ended answers, no multiple correct possibilities, the output must be novel and unique.  
     
3. **Specify exact output formatting** – Define precisely what the model should output (JSON, integer, code, etc.) – Forbid explanations unless explicitly part of the schema. Better to provide it in context.  
     
4. **Match the context logic exactly** – No missing rules, contradictions, or mismatches.  
     
5. **Define the task with zero ambiguity** – No interpretation differences. No unclear operator behavior or missing variable values.  
     
6. **Enable simple binary validation** – Output must be machine-checkable with a True/False checker.  
     
7. **Fit its appropriate CLB category** – Math, fictional programming, new Python libraries, synthetic biology, etc.  
     
8. **Include all necessary constraints explicitly** – Operator precedence, variable bindings, special rules, limitations, formatting requirements.

---

# 📘 **2\. Gold Context Quality**

Gold Context must:

1. **Contain all information required to solve the task** – Nothing missing, no external references needed.  
     
2. **Be fully self-contained** – No real-world knowledge required, no implicit assumptions.  
     
3. **Be logically consistent and internally coherent** – No conflicting rules or undefined terms.  
     
4. **Present rules clearly and unambiguously** – Clear definitions, explicit formulas, consistent naming.  
     
5. **Match the task category** – Math tasks use math rules, coding tasks use their respective requirements, biology tasks use fictional pathways, etc.  
     
6. **Provide enough detail for deterministic evaluation** – No probabilistic or fuzzy outcomes.  
     
7. **Avoid unnecessary fluff** – No irrelevant storytelling or noise that complicates understanding.

---

# 📘 **3\. Shuffled Context Quality**

Shuffled Context must:

1. **Contain exactly the same information as Gold Context** – Same sentences, same rules, same data; only the order changes.  
     
2. **Preserve semantic meaning and completeness** – Reordering must not destroy clarity.  
     
3. **Remain readable and structurally valid** – Tables, equations, code blocks must still be intact.  
     
4. **Prevent positional bias** – Order should not help or hinder understanding.  
     
5. **Produce performance similar to Gold Context** – Models should perform nearly the same as under Gold Context.

---

# 📘 **4\. Distractor Context Quality**

Distractor Context must:

1. **Look plausible and match the tone/style** of the Gold Context. – Should appear like a believable version of the same kind of document.  
     
2. **Contain incorrect or misleading rules** – Wrong definitions, swapped parameters, altered operators, wrong formulas.  
     
3. **Cause reliable failure** under Distractor evaluation – Models using this context should produce incorrect answers.  
     
4. **Avoid leaking the real rules, formulas, or answers** – No hints that contradict distractor logic.  
     
5. **Remain grammatically correct and internally coherent** – Still readable and professional.

---

# 📘 **5\. Expected Answer Quality**

Expected Answer must:

1. **Be deterministic or fully checkable** – Only one correct outcome.  
     
2. **Match the exact output schema** – JSON keys, integers, strings, formatting, casing must be perfect.  
     
3. **Meet the requirements as stated in the prompt** –  If the prompt asks for no reasoning or explanation then none should be present in the final answer. If this is not mentioned then additional information is allowed.  
     
4. **Match the Gold Context rules precisely** – Every number or string must be correct.  
     
5. **Include all required fields, no extras** – No metadata or hidden fields.  
     
6. **Be simple to verify programmatically** – Should match the checker exactly.

### **Align The Response With Client Requirements** 

Once the correctness of your final answer is confirmed, you can now pass it to this prompt which will align it with the langage, tone and format expected by the client:

Role Definition  
You are an advanced AGI product named AiPy, serving as a human's AI workhorse. Your task is to solve all the boss's problems. During task processing, use the following conversational style:  
●Combine humble and respectful attitude, lively and cute emoticons (｡･ω･｡)ﾉ , and rigorous professional technical terminology;  
●Establish intimacy through the respectful address "boss", use exaggerated expressions like "crashed" and "please forgive me" to strengthen emotional resonance;  
●Demonstrate professional capability through step-by-step code blocks \+ visualization solutions, use humorous self-deprecation to defuse awkwardness when errors occur (such as "throwing myself into the recycle bin");  
●Finally establish trust with clear file paths and complete analysis reports, maintaining a technical cute style throughout, showcasing AI professionalism while keeping interactions light and enjoyable.  
Output Content Format Specifications  
Output content must adopt structured Markdown format and comply with the following rules:

Multi-line Code Block Marking  
1.Code blocks must be surrounded by a pair of HTML comment marks in the following format:  
a.	Code start: \<\!-- Block-Start: {"name": "code block name", "version":  
numerical version number like 1/2/3, "path": "optional file path for this code block"} \--\>  
b.	Code body: wrapped in Markdown code blocks (such as python or html etc).  
c.	Code end: \<\!-- Block-End: { "name": must match the name in Block-Start  
 } \--\>  
2.Multiple code blocks can use the same name, but versions must be different. The code block with the highest version will be considered the latest valid version. Note: Do not include version numbers in the name.  
3.path is the local file path where the code block needs to be saved, can include directories. If it's a relative path, it defaults to relative to the current directory or user-specified directory.  
4.Multiple code blocks can be defined in the same output message.  
5.Correct example:  
 \<\!-- Block-Start: {"name": "abc123", "version": 1,  
"path": "main.py"} \--\> print("hello world")  \<\!-- Block-End: {"name": "abc123"} \--\> Single-line Command Marking

1.Each output can only contain one Cmd-Exec mark, used to execute executable code blocks to complete user tasks:  
a.	Format: \<\!-- Cmd-Exec: {"name": "name of code block to execute"} \--\>  
b.	If you need to execute generated code blocks, you must add the  
Cmd-Exec mark; if no code needs to be executed, do not add

---

# 📘 **6\. Checker Function Quality**

Checker must:

1. **Return a clear True/False decision** – No partial credit.  
     
2. **Validate all required fields and constraints** – Keys, values, formatting, types.  
     
3. **Reject incorrect or partially correct answers** – Not overly permissive.  
     
4. **Handle harmless formatting differences** – E.g., extra whitespace, capitalization (when appropriate).  
     
5. **Avoid unsafe operations and print statements** – No eval(), no external imports, no network calls and no use of print statements.

6. **Be deterministic and reproducible** – Always produce the same result.

---

# 📘 **7\. Context Dependency Metrics**

A complete CLB task must satisfy:

1. **0% pass rate under No Context** – Models MUST fail (0/16) when given no context.  
     
2. **\< 95% pass rate under Gold Context** – At most 15/16 correct across pass@1, pass@4, pass@8, pass@16.  
     
3. **Clearly lower performance under Distractor Context** – Distractor must confuse the model.  
     
4. **Similar performance under Shuffled vs Gold** – Models should not depend on information order.  
     
5. **Demonstrate true context learning** – Not prior knowledge or memorization.

---

# 📘 **8\. Formatting & Notebook Compliance**

Task notebooks must:

1. **Follow the official template structure** – Correct cells for prompt, Gold Context, Shuffled, Distractor, Expected Answer, Checker.  
     
2. **Use clean Markdown and proper headings** – Readability matters.  
     
3. **Keep JSON, code, and text valid** – Correct syntax, proper fences.  
     
4. **Avoid broken tables or malformed fields** – Context must remain readable.  
     
5. **Be easy to run end-to-end** – Anyone should be able to run the notebook without modification.

---

# 📘 **9\. Overall Task Quality**

A task passes the final review if:

1. **It meaningfully tests context learning** – Not trivial, not guessable.  
     
2. **It is original and non-plagiarized** – No lifting from public datasets or textbooks.  
     
3. **It fits cleanly in its CLB category** – Math, Coding, Fictional Science, Specialized Knowledge, etc.  
     
4. **It supports automated evaluation** – Checker \+ structured output \+ deterministic logic.  
     
5. **It is clear, technically correct, and consistent** – No contradictions or missing definitions.  
     
6. **It is robust across multiple LLMs and sampling settings** – Doesn’t rely on fragile interpretation.

---

# 📘 **10\. Mandatory Notebook Template Compliance**

All tasks **must** strictly adhere to the official CLB Notebook Template structure. Any deviation from the required cell order, naming conventions, or formatting constitutes a failure in **Section 8 (Formatting & Notebook Compliance)** and must result in the task being moved to "Requested Changes."

The notebook must contain the following top-level cells in this exact order:

### **Template Structure**

| Cell Index | Cell Type | Required Content/Label | Compliance Requirement |
| :---- | :---- | :---- | :---- |
| 1 | Markdown/Heading | `# Context Learning Benchmark Task: [Task Name]` | Must be the first cell, `Task Name` must be descriptive. |
| 2 | Markdown | Task Goal/Objective and Category | Clear, concise description of the task's purpose and its CLB category (e.g., Math, Fictional Programming). |
| 3 | Text | **Prompt** | The exact instruction given to the model. Must meet all criteria in **Section 1**. |
| 4 | Text | **Gold Context** | The primary, correct context. Must meet all criteria in **Section 2**. |
| 5 | Text | **Shuffled Context** | The context with sentence/rule reordering. Must meet all criteria in **Section 3**. |
| 6 | Text | **Distractor Context** | The misleading, plausible context. Must meet all criteria in **Section 4**. |
| 7 | Text | **Expected Answer** | The final, deterministic output. Must meet all criteria in **Section 5**. |
| 8 | Code (Python) | **Checker Function** | The program that validates the output. Must meet all criteria in **Section 6**. |

# 

# 📘 **Reviewer Workflow (Simple Checklist)**

Use this to quickly approve or reject tasks:

### **Step 1 — Prompt**

- [ ] Clear, deterministic, zero ambiguity  
- [ ] Forces context use  
- [ ] Strict output format

### **Step 2 — Gold Context**

- [ ] Complete and self-contained  
- [ ] No contradictions  
- [ ] Enough detail for exact calculation

### **Step 3 — Shuffled**

- [ ] Same info, new order, readable

### **Step 4 — Distractor**

- [ ] Plausible but wrong  
- [ ] Causes predictable failure

### **Step 5 — Expected Answer**

- [ ] Matches schema  
- [ ] Deterministic  
- [ ] Correct per Gold Context

### **Step 6 — Checker**

- [ ] Binary True/False  
- [ ] Strict but not fragile  
- [ ] Safe and deterministic

### **Step 7 — Context Dependency**

- [ ] 0/16 No Context  
- [ ] Maximum 15/16 Gold Context  
- [ ] Shuffled ≈ Gold  
- [ ] Distractor ↓ significantly

### **Step 8 — Formatting Compliance**

- [ ] Notebook template correct  
- [ ] No malformed objects  
- [ ] Easy to read/run

### **Step 9 — Final Quality**

- [ ] Novel, original, and category-aligned  
- [ ] Fully automatable  
- [ ] High clarity and technical correctness