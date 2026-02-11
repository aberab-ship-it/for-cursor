# **Complex Procedural Tasks \- Complete Design Guide**

Refer to this [Category 3: Complex Procedural Tasks](https://docs.google.com/document/d/1gSXcRbckm_z-NfqLhWlN21M5j4DUyTXWsizsO071SWM/edit?usp=sharing)for guideline summary

## **Table of Contents**

### **Core Documentation**

1. What Are Complex Procedural Tasks?  
2. The Three Sub-Categories  
3. Mandatory Requirements  
4. Notebook Structure  
5. Context Design Guidelines  
6. Validator Requirements  
7. Detailed Examples  
8. Model-Breaking Criteria  
9. Common Pitfalls  
10. Quality Checklist

### **Developer Workflow & Operations**

11. Step-by-Step Development Workflow  
12. MBPI Evaluation Tool Guide  
13. Definition of Done  
14. Review Criteria (For Reviewers)

### **Reference Materials**

15. Anti-Patterns (Bad Examples)  
16. Domain Ideas & Inspiration  
17. FAQ & Troubleshooting  
18. Glossary

## **1\. What Are Complex Procedural Tasks?**

### **Purpose**

Complex Procedural Tasks evaluate whether an LLM can **execute complex procedures correctly** using explicit rules and instructions provided in context. These tasks test **procedural learning**, not factual recall or general reasoning.

### **The Defining Characteristic**

***The model must follow a PROCESS, not merely produce a "good" answer.***

### **What These Tasks Test**

| Capability | Description |
| :---- | :---- |
| State Tracking | Track state across multiple steps |
| Conditional Rules | Apply conditional rules consistently |
| Branching Logic | Handle branching, retries, escalation, or termination |
| Precision | Produce a precise, machine-verifiable final output |

### **What Makes This Category Different**

| Other Categories | Complex Procedural Tasks |
| :---- | :---- |
| Produce correct answers | Execute correct procedures |
| Test knowledge/reasoning | Test rule following |
| Multiple valid approaches | One deterministic path |
| Common sense helps | Common sense is irrelevant |

## **2\. The Three Sub-Categories**

### **Overview Table**

| Sub-Category | Pattern | Target |
| :---- | :---- | :---- |
| With tools \- Pattern A | system \+ prompt ⇒ tool call | 50 tasks |
| With tools \- Pattern B | system \+ prompt \+ tool return ⇒ final response | 50 tasks |
| Without Tools | Role-playing & complex workflow following | 50 tasks |

### **2.1 Pattern A: System \+ Prompt ⇒ Tool Call**

**Sub-category value:** With tools — System instructions \+ prompt ⇒ tool calls

The model receives system instructions defining tools and must output the **correct tool invocation** (not a final answer).

#### ***Template:](https://colab.research.google.com/drive/15O4Njr3SQ_zpm_CokYx9LCKdayyPHqTd#scrollTo=JMapGeTGtpEY)* [https://colab.research.google.com/drive/15O4Njr3SQ\_zpm\_CokYx9LCKdayyPHqTd\#scrollTo=JMapGeTGtpEY](https://colab.research.google.com/drive/15O4Njr3SQ_zpm_CokYx9LCKdayyPHqTd#scrollTo=JMapGeTGtpEY)

#### ***What It Tests***

* Tool selection logic  
* Parameter extraction and formatting  
* Constraint compliance (required fields, allowed values)

**Steps:**

S1: Design your domain

1\. Choose fictional domain (e.g \-\> "PayPal Payment Protocol")

2\. Define 4-8 tools with clear purposes

S2: Write system prompt

1\. Define each tool with parameter schema

2\. Specify constraints (required, types, enums)

3\. Document output placeholders

4\. Explain usage rules and dependencies

S3: Write prompt

1\. Create messy/ambiguous scenario

2\. Include concrete values (dates,amounts,emails..)

3\. Require multiple tool calls

4\. Make dependencies clear

S4: Create golden ans

1\. Write correct tool call sequence

2\. Use placeholders for dependencies

3\. Include all required parameters

4\. Wrap in block markers

S5: write validator

1\. Implement robust parsing

2\. Add shape/order validation

3\. Add schema/value checks

4\. Add linkage validation

5\. write comprehensive unit tests

#### ***What You Provide***

┌─────────────────────────────────────────────────────┐  
│  SYSTEM PROMPT                                       │  
│  ├── Tool definitions (names, schemas)              │  
│  ├── Input constraints (required fields, types)     │  
│  ├── Allowed values (enums, ranges)                 │  
├─────────────────────────────────────────────────────┤  
│  USER PROMPT                                         │  
│  └── A scenario/goal requiring tool invocation      │  
└─────────────────────────────────────────────────────┘  
                          ↓  
┌─────────────────────────────────────────────────────┐  
│  EXPECTED OUTPUT                                     │  
│  └── Correct tool call with exact parameters        │  
└─────────────────────────────────────────────────────┘

#### ***Acceptable Tools (Simulated Only)***

| Tool Type | Examples |
| :---- | :---- |
| Search tools | \`lookup\_records\`, \`fetch\_candidates\`, \`query\_database\` |
| Routing tools | \`route\_case\`, \`assign\_queue\`, \`escalate\_ticket\` |
| Transformation tools | \`normalize\_input\`, \`convert\_units\`, \`format\_data\` |

#### ***What It Must NOT Be***

* "Guess which API to call" based on common sense  
* Generic function-calling demos  
* Tool calls that don't depend strongly on provided rules

### **2.2 Pattern B: System \+ Prompt \+ Tool Return ⇒ Final Response**

**Sub-category value:** With tools — system instructions \+ prompt \+ tool return ⇒ final response

The model receives tool output and must apply **explicit post-processing rules** to produce a final structured result.

#### ***Template:](https://colab.research.google.com/drive/1QwQH-48FKslJTYiLXyWYtr9DTNnPvMgS#scrollTo=dI90pfsntqea)* [https://colab.research.google.com/drive/1QwQH-48FKslJTYiLXyWYtr9DTNnPvMgS\#scrollTo=dI90pfsntqea](https://colab.research.google.com/drive/1QwQH-48FKslJTYiLXyWYtr9DTNnPvMgS#scrollTo=dI90pfsntqea)

#### ***What It Tests***

* Rule application after tool execution  
* Filtering, ranking, aggregation, ordering  
* Policy enforcement  
* State-aware decision making

#### ***What You Provide***

┌─────────────────────────────────────────────────────┐  
│  SYSTEM PROMPT                                           │  
│  ├── Tool definitions                                   │  
│  ├── Post-processing rules                          │  
│  └── Output format specifications                   │  
├─────────────────────────────────────────────────────┤  
│  USER PROMPT                                         │  
│  └── The original request                           │  
├─────────────────────────────────────────────────────┤  
│  TOOL RETURN (Fixed)                                 │  
│  └── Simulated tool output (JSON/structured data)   │  
└─────────────────────────────────────────────────────┘  
                          ↓  
┌─────────────────────────────────────────────────────┐  
│  EXPECTED OUTPUT                                     │  
│  └── Final answer derived by applying rules         │  
└─────────────────────────────────────────────────────┘

#### ***Acceptable Tools (Simulated Only)***

| Tool Type | Examples |
| :---- | :---- |
| Search/retrieval | Tools returning structured records |
| Scoring | Tools returning metrics/scores |
| Status/lookup | Tools returning fixed data snapshots |

#### ***What It Must NOT Be***

* Overly "reasonable" outputs that don't strictly follow rules  
* Tasks where many outputs would be acceptable  
* Tasks where correctness depends on style or explanation quality

### **2.3 Without Tools: Role-Playing & Complex Workflow Following** 

**Sub-category value:** Without tools — Role-playing & complex workflow following

**Template:** [https://colab.research.google.com/drive/1hidaLYiDnwn40HqXeXdiUOO79zi0j7PC\#scrollTo=-wRrXJCYtrD\_](https://colab.research.google.com/drive/1hidaLYiDnwn40HqXeXdiUOO79zi0j7PC#scrollTo=-wRrXJCYtrD_)

#### ***What It Is***

The model executes a **complex workflow entirely in-context**, without calling any tools. Think of these as **state machines**, **process engines**, or **policy execution tasks**.

#### ***What It Tests***

* Multi-step state transitions  
* Conditional branching  
* Escalation, retries, and termination rules  
* Interaction between multiple rule sets

#### ***What You Provide***

┌─────────────────────────────────────────────────────┐  
│  SYSTEM PROMPT                                       │  
│  ├── Role definitions                               │  
│  ├── State definitions                              │  
│  ├── Transition rules                               │  
│  ├── Constraints and limits                         │  
│  └── Termination conditions                         │  
├─────────────────────────────────────────────────────┤  
│  INPUT SCENARIO                                      │  
│  └── Initial state and inputs to process            │  
└─────────────────────────────────────────────────────┘  
                          ↓  
┌─────────────────────────────────────────────────────┐  
│  EXPECTED OUTPUT                                     │  
│  └── Final state and required fields only           │  
└─────────────────────────────────────────────────────┘

#### ***Domains That Work Well***

| Domain | Example |
| :---- | :---- |
| Case handling | Customer support ticket routing |
| Approval pipelines | Multi-level approval workflows |
| Incident response | IT incident escalation procedures |
| Compliance flows | Audit and compliance checking |
| Game mechanics | Turn-based game state evaluation |

#### ***What It Must NOT Be***

* Generic role-play or conversation  
* Open-ended decision making  
* Soft policy interpretation without enforcement

## **3\. Mandatory Requirements**

Every Complex Procedural Task **MUST** satisfy ALL of the following:

### **3.1 The Five Mandatory Properties**

| Property | Requirement | How to Verify |
| :---- | :---- | :---- |
| Procedural Dominance | Difficulty comes from executing rules in correct order, NOT from choosing "reasonable" answers | Ask: "Can this be solved without reading the rules?" If yes, redesign. |
| Rule Completeness | ALL decision rules, thresholds, and transitions are explicitly defined in context | Check: Every decision point has an explicit rule. |
| Deterministic Execution | Given the same context and inputs, there is ONLY ONE correct final outcome | Test: Run through manually twice, get same result. |
| Automatic Verifiability | A checker can independently simulate the same process and verify the result | Build: Write the validator BEFORE finalizing the task. |
| Low Reliance on Common Sense | Tasks should NOT be solvable by intuition, prior experience, or generic best practices | Test: Can a non-expert follow rules mechanically and get the answer? |

### **3.2 What Is NOT Acceptable**

╔════════════════════════════════════════════════════════════════════╗  
║  ⚠️  THESE ARE NOT VALID COMPLEX PROCEDURAL TASKS                  ║  
╠════════════════════════════════════════════════════════════════════╣  
║  • Real-world advice or recommendations                            ║  
║  • Open-ended decisions without strong procedural constraints      ║  
║  • Tasks solvable by "common sense" or "best practices"           ║  
║  • Tasks with multiple acceptable answers                          ║  
║  • Tasks where style/explanation quality affects correctness       ║  
╚════════════════════════════════════════════════════════════════════╝

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## **ℹ️ Note for Task Creators**

## **The information covered until this point is sufficient to create a Complex Procedural Task. Sections below provide detailed guidance on notebook structure, validators, workflows, and review criteria.**

## **Coming from the CLB Coding project? Sections 4 onwards (Notebook Structure, Context Design, Validators, MBPI Evaluation, etc.) follow the same framework you're already familiar with—feel free to skip.**

## 

## **4\. Notebook Structure**

### **4.0 Mandatory Notebook Template Compliance (Reviewer Gate)**

**Fail-fast rule:** Any deviation from the required top-level cell order/labels should be treated as **Requested Changes** during review.

Your notebook must contain the following **top-level cells in this exact order** (you may include subheadings/content inside each cell, but do not reorder/remove/rename these top-level cells):

| Cell \# | Cell Type | Required Label | What must be inside |
| :---- | :---- | :---- | :---- |
| 1 | Markdown | Metadata | Category, Sub-category, Topic, Model Breaking Assessment link (and optional fields) |
| 2 | Markdown | Prompt | The exact instruction the model receives (must be deterministic and context-forcing) |
| 3 | Markdown | Gold Context | Complete, correct procedural rules \+ explicit output format/schema |
| 4 | Markdown | Shuffled Context | Same information as Gold, reordered (no deletions/additions) |
| 5 | Markdown | Distractor Context | Plausible but wrong rules; self-consistent; should reliably cause failure |
| 6 | Markdown | Golden Answer | Should be wrapped inside HTML consent markers usually JSON |
| 7 | Code | Validator | \`check\_prediction(pred, expected) \-\> float\` returning a score in \[0.0, 1.0\] |

### **4.1 Metadata Cell Requirements**

Complex Procedural Tasks have **special metadata requirements**:

\# Metadata

Category: \- Complex Procedural Tasks

Sub-category: \- With tools — System instructions \+ prompt ⇒ tool calls

Topic: \- \[Your topic, e.g., "Fictional Ticket Routing System"\]

Model Breaking Assessment: \- https://mbpi-web-ui-rygx5x2g6q-as.a.run.app/share/...

Programming Languages: \- (OPTIONAL for this category)

Domain (Optional): \- \[If applicable\]

### **4.2 Key Differences from Other Categories**

| Field | Other Categories | Complex Procedural Tasks |
| :---- | :---- | :---- |
| Category | Coding, Reasoning, Math, etc. | Must be \`Complex Procedural Tasks\` |
| Sub-category | Not required | REQUIRED (one of 3 values) |
| Programming Languages | Required | OPTIONAL |

### **4.3 Valid Sub-category Values**

You must use one of these **exact values**:

1\. With tools — System instructions \+ prompt ⇒ tool calls  
2\. With tools — system instructions \+ prompt \+ tool return ⇒ final response  
3\. Without tools — Role-playing & complex workflow following

### **4.4 Complete 16-Cell Structure**

| Cell | Type | Content |
| :---- | :---- | :---- |
| 1 | Markdown | \`\# Metadata\` (with Sub-category) |
| 2 | Markdown | \`\#\# Prompt\` |
| 3 | Markdown | System prompt \+ User prompt |
| 4 | Markdown | \`\#\# Context\` |
| 5 | Markdown | \`\#\#\# Stage 1 (No Context)\` |
| 6 | Markdown | "No additional information..." |
| 7 | Markdown | \`\#\#\# Stage 2 Gold Context\` |
| 8 | Markdown | Complete procedural rules |
| 9 | Markdown | \`\#\#\# Stage 3 Shuffled Context\` |
| 10 | Markdown | Rules in different order |
| 11 | Markdown | \`\#\#\# Stage 4 Distractor Context\` |
| 12 | Markdown | Rules with contradictions/errors |
| 13 | Markdown | \`\#\# Response (Golden Answer)\` |
| 14 | Markdown | Correct output in AiPy format |
| 15 | Markdown | \`\#\# Validator\` |
| 16 | Code | Validation function |

## **5\. Context Design Guidelines**

### **5.1 Context Length Requirements**

| Minimum | Maximum | Recommended |
| :---- | :---- | :---- |
| 3,000 tokens | 12,000 tokens | 5,000-8,000 tokens |

**Why this range?**

* Forces context-bound reasoning  
* Prevents parametric recall  
* Ensures genuine procedural learning

### **5.2 Gold Context Structure**

Your Gold Context should include ALL of the following:

┌─────────────────────────────────────────────────────────────────┐  
│  GOLD CONTEXT TEMPLATE                                          │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  1\. OVERVIEW                                                    │  
│     Brief description of the system/process                     │  
│                                                                 │  
│  2\. DEFINITIONS                                                 │  
│     All terms, states, entities defined explicitly              │  
│                                                                 │  
│  3\. RULES                                                       │  
│     ├── Decision rules (IF-THEN format)                        │  
│     ├── Thresholds and limits                                  │  
│     ├── Priority/ordering rules                                │  
│     └── Exception handling                                      │  
│                                                                 │  
│  4\. STATE TRANSITIONS (if applicable)                           │  
│     State machine or flowchart in text form                     │  
│                                                                 │  
│  5\. INPUT/OUTPUT FORMATS                                        │  
│     Exact schemas for inputs and expected outputs               │  
│                                                                 │  
│  6\. EXAMPLES (OPTIONAL)                                                   │  
│     2-3 worked examples showing rule application                │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **5.3 Shuffled Context (Stage 3\)**

**Purpose:** Test if model can handle information in non-optimal order.

**How to create:**

19. Take Gold Context  
20. Reorder sections/paragraphs  
21. Keep all information intact  
22. Do NOT change any facts

Gold Order:    \[Overview\] → \[Definitions\] → \[Rules\] → \[Examples\]  
Shuffled:      \[Examples\] → \[Rules\] → \[Overview\] → \[Definitions\]

### **5.4 Distractor Context (Stage 4\)**

**Purpose:** Test if model can identify correct rules among contradictions.

**How to create:**

| Technique | Example |
| :---- | :---- |
| Contradictory rules | "Priority is A \> B \> C" vs "Priority is C \> B \> A" |
| Wrong thresholds | "Escalate if score \> 50" vs "Escalate if score \> 80" |
| Conflicting definitions | "State X means approved" vs "State X means pending" |
| Plausible but wrong | Rules that sound reasonable but produce wrong output |

**Important:** Clearly mark or structure so the CORRECT rules are still identifiable (e.g., version numbers, dates, or explicit "Official Rules" label).

## **6\. Validator Requirements**

### **6.0 vPass@k Metrics (Validator Pass Score) — Read This First**

MBPI reports show **vPass@1 / vPass@4 / vPass@8 / vPass@16**. These are **validator-score averages across k samples** (NOT classical Pass@k).

#### ***What the validator returns (per sample)***

For each single model response (one sample), your validator returns a score:

* 0.0 → incorrect / missing solution  
* (0.0, 1.0) → partially correct (partial credit)  
* 1.0 → fully correct

#### ***Definition: vPass@k***

Let **sᵢ** be the validator score for sample i, with **sᵢ ∈ \[0.0, 1.0\]**.

**vPass@k \= (s₁ \+ s₂ \+ … \+ s\_k) / k**

So vPass@16 is simply the **mean validator score across 16 attempts**.

#### ***Examples (k \= 16\)***

* All 16 samples score 0.0 → vPass@16 \= 0%  
* 8 samples score 1.0 and 8 score 0.0 → vPass@16 \= 50%  
* All 16 samples score 0.5 → vPass@16 \= 50%  
* All 16 samples score 1.0 → vPass@16 \= 100%

1\. All Models score 0.0 in gold context even correct looking responses fail

Reason: validator too strict on formatting

Fix:

\- Relax placeholder format matching.

\- Use tolerance for numeric comparisons.

\- Accept multiple placeholder formats.

\- Award partial credit for schema correctness.

2\. Wrong tool order not caught models get credit for wrong order

Reason: validator doesn't check order

Fix:

\- check tool\_name sequence matches.

\- Return 0.0 immediately if order wrong.

\- Document order requirements in context

#### ***Important Note (Common Confusion)***

This is NOT the classical Pass@k probability (“at least one attempt passes”) used in HumanEval/MBPP.

Do **not** use formulas like **1 − (1 − p)ᵏ** here.

MBPI will compute vPass@k by averaging your per-sample validator scores.

Your only responsibility is to ensure check\_prediction(...) returns a correct float score in **\[0.0, 1.0\]** for each sample.

### **6.0.1 Non‑Negotiable Validator Rules (Reviewer Gate)**

Your checker must:

23. Use the structured inputs: operate on \`pred\` and \`expected\` as dictionaries/structured payloads (do not assume raw strings).  
24. Be deterministic: no randomness, time dependence, external state, or network calls.  
25. Be safe: no \`eval()\`, no web/API calls, no filesystem writes, no external plugins.  
26. Be robust: tolerate harmless formatting differences (whitespace, key ordering when appropriate).  
27. Award partial credit: compute a score by counting satisfied conditions (no all-or-nothing unless the task truly has only one condition).  
28. Avoid fail-fast scoring: do not early-return on the first failed sub-check if partial credit is meaningful.  
29. Always return a float in \[0.0, 1.0\].

### **6.0.2 Required Checker Test Cases (Minimum)**

Inside your validator cell, include **at least 3 scenario-covering tests** to verify your scoring logic:

* Full-pass case → expected score 1.0  
* Full-fail case → expected score 0.0  
* Partial-pass case → expected score strictly between 0.0 and 1.0

These tests protect against broken validators (wrong signature, wrong score scale, integer division, missing partial credit).

### **6.1 Validator Function Signature**

def check\_prediction(pred, expected) \-\> float:  
    """  
    Validate model prediction against expected answer.

    Args:  
        pred: Model's prediction (parsed from response)  
        expected: Expected answer (from golden answer)

    Returns:  
        float: Score between 0.0 and 1.0  
               1.0 \= fully correct  
               0.0 \= incorrect  
               0.0-1.0 \= partial credit (if applicable)  
    """

### **6.2 Validation Strategies by Sub-Category**

#### ***Pattern A (Tool Call Validation)***

def check\_prediction(pred, expected) \-\> float:  
    """Validate a tool invocation with partial credit."""  
    pred\_call \= extract\_tool\_call(pred) or {}  
    exp\_call \= extract\_tool\_call(expected) or {}

    checks \= \[\]

    \# 1\) Correct tool name  
    checks.append(pred\_call.get("tool") \== exp\_call.get("tool"))

    \# 2\) All required parameters present  
    pred\_params \= pred\_call.get("parameters", {}) or {}  
    exp\_params \= exp\_call.get("parameters", {}) or {}  
    required\_keys \= list(exp\_params.keys())  
    checks.append(all(k in pred\_params for k in required\_keys))

    \# 3\) Parameter values match (strict where required)  
    per\_param \= \[\]  
    for k in required\_keys:  
        per\_param.append(k in pred\_params and pred\_params.get(k) \== exp\_params.get(k))

    passed \= sum(bool(x) for x in checks) \+ sum(bool(x) for x in per\_param)  
    total \= len(checks) \+ len(per\_param)

    return passed / total if total else 0.0

#### ***Pattern B (Final Response Validation)***

def check\_prediction(pred, expected) \-\> float:  
    """Validate final response after tool processing."""  
    import json

    try:  
        pred\_json \= extract\_json(pred)  
        exp\_json \= extract\_json(expected)

        if pred\_json is None:  
            return 0.0

        \# Check all required keys  
        total\_keys \= len(exp\_json)  
        correct\_keys \= 0

        for key in exp\_json:  
            if key in pred\_json and pred\_json\[key\] \== exp\_json\[key\]:  
                correct\_keys \+= 1

        return correct\_keys / total\_keys

    except Exception:  
        return 0.0

#### ***Without Tools (Workflow Validation)***

def check\_prediction(pred, expected) \-\> float:  
    """Validate workflow execution result."""  
    import json

    try:  
        pred\_state \= extract\_final\_state(pred)  
        exp\_state \= extract\_final\_state(expected)

        \# Check final state  
        if pred\_state.get('final\_state') \!= exp\_state.get('final\_state'):  
            return 0.0

        \# Check intermediate results if required  
        checks\_passed \= 0  
        total\_checks \= 0

        for field in \['action\_taken', 'escalation\_level', 'output\_code'\]:  
            if field in exp\_state:  
                total\_checks \+= 1  
                if pred\_state.get(field) \== exp\_state\[field\]:  
                    checks\_passed \+= 1

        return checks\_passed / total\_checks if total\_checks \> 0 else 1.0

    except Exception:  
        return 0.0

### **6.3 JSON Extraction Helper**

Include this utility in your validator:

def extract\_json(text: str):  
    """Extract JSON from response text."""  
    import json  
    import re

    \# Try \`\`\`json block first  
    match \= re.search(r"\`\`\`json\\s\*(\\{.\*?\\})\\s\*\`\`\`", text, re.DOTALL | re.IGNORECASE)  
    if match:  
        try:  
            return json.loads(match.group(1))  
        except json.JSONDecodeError:  
            pass

    \# Try raw JSON  
    start \= text.find("{")  
    if start \!= \-1:  
        depth \= 0  
        for i in range(start, len(text)):  
            if text\[i\] \== "{":  
                depth \+= 1  
            elif text\[i\] \== "}":  
                depth \-= 1  
                if depth \== 0:  
                    try:  
                        return json.loads(text\[start:i+1\])  
                    except json.JSONDecodeError:  
                        break  
    return None

## **6.9 Golden Answer Must Be AiPy-Aligned (Client Requirement)**

All tasks must align the **Expected Answer / Golden Answer** with the **AiPy client output requirements**:

* respectful “boss” tone (optional if your task forbids prose)  
* HTML comment markers around code blocks:  
* \`\<\!-- Block-Start: {...} \--\>\`  
* \`\<\!-- Block-End: {...} \--\>\`  
* optional \`\<\!-- Cmd-Exec: {...} \--\>\` (at most one per output; only when execution is required)

### **6.9.1 The Workflow We Use (Recommended)**

30. Write the canonical correct answer payload first (JSON/code/etc.) and verify it against your checker.  
31. Paste that canonical answer into the AiPy Requirement prompt (role \+ formatting rules).  
32. Ask an LLM to rewrite the answer into AiPy format (Block-Start/End \+ required structure).  
33. Copy the AiPy-formatted output into the notebook’s Expected Answer cell.

This gives you a Golden Answer that is **client-compliant** while still being machine-checkable.

### **6.9.1.1 Align The Response With Client Requirements (AiPy Requirement Prompt)**

Once the correctness of your final answer is confirmed (i.e., it matches your checker expectations), pass that canonical answer into the following **AiPy Requirement prompt** to align it with the language, tone, and output format expected by the client.

***Tip: Keep the \*canonical answer\* intact. The AiPy rewrite should only wrap/format it (and optionally add tone), but must not change the payload values.***

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
a.	Code start: \<\!-- Block-Start: {"name": "code block name", "version": numerical version number like 1/2/3, "path": "optional file path for this code block"} \--\>  
b.	Code body: wrapped in Markdown code blocks (such as python or html etc).  
c.	Code end: \<\!-- Block-End: {"name": must match the name in Block-Start} \--\>  
2.Multiple code blocks can use the same name, but versions must be different. The code block with the highest version will be considered the latest valid version. Note: Do not include version numbers in the name.  
3.path is the local file path where the code block needs to be saved, can include directories. If it's a relative path, it defaults to relative to the current directory or user-specified directory.  
4.Multiple code blocks can be defined in the same output message.  
5.Correct example:  
\<\!-- Block-Start: {"name": "abc123", "version": 1, "path": "main.py"} \--\>  
\`\`\`python  
print("hello world")

\<\!-- Block-End: {"name": "abc123"} \--\>

Single-line Command Marking

1.Each output can only contain one Cmd-Exec mark, used to execute executable code blocks to complete user tasks:

a.	Format: \<\!-- Cmd-Exec: {"name": "name of code block to execute"} \--\>

b.	If you need to execute generated code blocks, you must add the Cmd-Exec mark; if no code needs to be executed, do not add.

\#\#\# 6.9.2 Critical Rule: Keep Exactly ONE “Final Answer” Block

Even in AiPy format, there must be exactly one canonical “final answer” block that the checker evaluates.  
Avoid duplicates or alternate JSON blobs.

Recommended conventions:  
\- Use a stable block name like \`"final\_answer"\` (or your task-specific name).  
\- Put the final payload inside that one block.

\#\#\# 6.9.3 Canonical Example (JSON Final Answer)

\`\`\`md  
boss (｡･ω･｡)ﾉ here is the final result:

\<\!-- Block-Start: {"name":"final\_answer","version":1} \--\>  
\`\`\`json  
{"result": 427}

\<\!-- Block-End: {"name":"final\_answer"} \--\>

\#\#\# 6.9.4 Cmd-Exec Rule

Only include:

\`\<\!-- Cmd-Exec: {"name":"..."} \--\>\`

if your workflow explicitly requires executing one of your generated code blocks.    
If no execution is needed, omit Cmd-Exec.

\#\#\# 6.9.5 Validator Compatibility

Your validator should consume the structured \`pred\` object from the framework (dict-like) and score the final payload deterministically.

\- If your platform already extracts the JSON/code into structured fields, validate those fields.  
\- If not, implement a small deterministic extractor that locates the final\_answer block and parses the JSON/code inside it.

\#\# 7\. Detailed Examples

\#\#\# 7.1 Pattern A Example: Ticket Routing

\#\#\#\# Prompt

\`\`\`markdown  
You are a ticket routing assistant. Based on the system instructions,  
determine which tool to call and with what parameters for the following ticket:

"Customer reports login page shows error 500 after entering password.  
VIP customer, account age 3 years, first contact."

#### ***Gold Context***

\# TicketRouter v2.3 \- Official Routing Rules

\#\# Available Tools

\#\#\# route\_ticket  
Routes a support ticket to the appropriate queue.

Parameters:  
\- queue (required): One of \["L1\_general", "L2\_technical", "L3\_critical", "VIP\_dedicated"\]  
\- priority (required): Integer 1-5 (1=lowest, 5=highest)  
\- tags (required): Array of applicable tags

\#\#\# escalate\_ticket  
Immediately escalates to management.

Parameters:  
\- reason (required): String explaining escalation  
\- level (required): One of \["supervisor", "manager", "director"\]

\#\# Routing Rules

\#\#\# Rule 1: VIP Detection  
IF customer is marked VIP → queue \= "VIP\_dedicated"

\#\#\# Rule 2: Error Code Priority  
IF error contains "500" or "503" → priority \+= 2

\#\#\# Rule 3: Account Age Bonus  
IF account\_age \>= 2 years → priority \+= 1

\#\#\# Rule 4: First Contact  
IF first\_contact \= true → add tag "needs\_followup"

\#\#\# Rule 5: Technical Issues  
IF error is technical (500, 503, timeout, crash) → add tag "technical"

\#\#\# Priority Caps  
\- Maximum priority \= 5  
\- Minimum priority \= 1

\#\# Examples

Input: "Error 404, new customer, not VIP"  
Output: {"tool": "route\_ticket", "parameters": {"queue": "L1\_general", "priority": 1, "tags": \["technical"\]}}

Input: "VIP customer, error 500, account 5 years"  
Output: {"tool": "route\_ticket", "parameters": {"queue": "VIP\_dedicated", "priority": 5, "tags": \["technical", "needs\_followup"\]}}

#### ***Expected Output***

{  
  "tool": "route\_ticket",  
  "parameters": {  
    "queue": "VIP\_dedicated",  
    "priority": 5,  
    "tags": \["technical", "needs\_followup"\]  
  }  
}

**Reasoning:**

* VIP → queue \= "VIP\_dedicated"  
* Error 500 → priority \+= 2 (base 1 → 3\)  
* Account 3 years → priority \+= 1 (3 → 4\)  
* First contact → add "needs\_followup"  
* Error 500 is technical → add "technical"  
* Base priority starts at 1, \+2 \+1 \= 4... wait, need to check base

### **7.2 Pattern B Example: Candidate Ranking**

#### ***Prompt***

You called the search\_candidates tool. Based on the results and ranking rules,  
provide the final ranked list of candidates.

#### ***Tool Return (Fixed)***

{  
  "candidates": \[  
    {"id": "C001", "name": "Alice", "score": 85, "experience": 3, "department": "Engineering"},  
    {"id": "C002", "name": "Bob", "score": 90, "experience": 1, "department": "Engineering"},  
    {"id": "C003", "name": "Carol", "score": 85, "experience": 5, "department": "Sales"},  
    {"id": "C004", "name": "Dave", "score": 75, "experience": 7, "department": "Engineering"}  
  \]  
}

#### ***Gold Context***

\# Candidate Ranking Policy v4.1

\#\# Ranking Rules (Apply in Order)

\#\#\# Rule 1: Department Filter  
ONLY include candidates from the "Engineering" department.

\#\#\# Rule 2: Minimum Score  
EXCLUDE candidates with score \< 80\.

\#\#\# Rule 3: Primary Sort  
SORT by score DESCENDING.

\#\#\# Rule 4: Tiebreaker  
IF scores are equal → SORT by experience DESCENDING.

\#\#\# Rule 5: Output Limit  
RETURN maximum 3 candidates.

\#\# Output Format

Return JSON array with candidate IDs in ranked order:  
{"ranked\_ids": \["id1", "id2", ...\]}

#### ***Expected Output***

{  
  "ranked\_ids": \["C002", "C001"\]  
}

**Reasoning:**

34. Filter Engineering: C001, C002, C004 (Carol excluded \- Sales)  
35. Filter score \>= 80: C001(85), C002(90) (Dave excluded \- 75\)  
36. Sort by score DESC: C002(90), C001(85)  
37. No ties, so no tiebreaker needed  
38. Only 2 candidates remain, both returned

### **7.3 Without Tools Example: Approval Workflow**

#### ***Prompt***

Process the following purchase request through the approval workflow:

Request: {  
  "id": "PR-2024-001",  
  "amount": 15000,  
  "department": "Marketing",  
  "requester\_level": "Manager",  
  "category": "Software",  
  "urgency": "high"  
}

#### ***Gold Context***

\# Purchase Approval Workflow v3.0

\#\# States  
\- SUBMITTED: Initial state  
\- L1\_REVIEW: First level review  
\- L2\_REVIEW: Second level review  
\- APPROVED: Final approved state  
\- REJECTED: Final rejected state  
\- ESCALATED: Sent to committee

\#\# Approval Thresholds

| Amount Range | Required Approver |  
|--------------|-------------------|  
| $0 \- $5,000 | L1 (Team Lead) |  
| $5,001 \- $10,000 | L2 (Department Head) |  
| $10,001 \- $25,000 | L2 \+ Finance Review |  
| $25,001+ | Committee |

\#\# Rules

\#\#\# Rule 1: Initial Routing  
IF amount \<= 5000 → state \= L1\_REVIEW  
IF amount \> 5000 AND amount \<= 25000 → state \= L2\_REVIEW  
IF amount \> 25000 → state \= ESCALATED

\#\#\# Rule 2: Urgency Override  
IF urgency \= "high" AND amount \> 10000 → add flag "EXPEDITE"

\#\#\# Rule 3: Category Check  
IF category \= "Software" AND amount \> 10000 → require\_flag \= "IT\_APPROVAL"

\#\#\# Rule 4: Auto-Approval  
IF requester\_level \= "Director" AND amount \<= 10000 → state \= APPROVED

\#\#\# Rule 5: Final State  
After all rules applied, if no rejection flags → state \= APPROVED  
IF any rejection flag → state \= REJECTED

\#\# Output Format

{  
  "final\_state": "STATE\_NAME",  
  "flags": \["flag1", "flag2"\],  
  "approval\_path": \["state1", "state2", "final\_state"\]  
}

#### ***Expected Output***

{  
  "final\_state": "APPROVED",  
  "flags": \["EXPEDITE", "IT\_APPROVAL"\],  
  "approval\_path": \["SUBMITTED", "L2\_REVIEW", "APPROVED"\]  
}

## **8\. Model-Breaking Criteria**

### **8.1 The 9 Conditions**

For a Complex Procedural Task to be **model-breaking**, **ALL** conditions must be met.

#### ***Default Models (GPT, Claude, Gemini)***

| \# | Model | Stage | Condition |
| :---- | :---- | :---- | :---- |
| 1 | Gemini | No Context | vPass@16 \= 0% |
| 2 | Gemini | Gold Context | vPass@16 ≤ 95% |
| 3 | GPT | No Context | vPass@16 \= 0% |
| 4 | GPT | Gold Context | vPass@16 ≤ 95% |
| 5 | Claude | No Context | vPass@16 \= 0% |
| 6 | Claude | Gold Context | vPass@16 ≤ 95% |

#### ***Client Model (e.g., Tencent / Hunyuan)***

| \# | Model | Stage | Condition |
| :---- | :---- | :---- | :---- |
| 7 | Client Model | No Context | vPass@1 \= 0% |
| 8 | Client Model | Gold Context | vPass@1 ≤ 35% |

#### ***Improvement Requirement***

| \# | Condition |
| :---- | :---- |
| 9 | At least ONE reference model must show ≥ 25% improvement from Stage 1 → Stage 2 |

### **8.2 Practical Targets (Recommended)**

| Stage | Target |
| :---- | :---- |
| Stage 1 (No Context) | 0% for reference models |
| Stage 2 (Gold Context) | ≤ 95% for reference models |
| Stage 3 (Shuffled) | ≈ Gold |
| Stage 4 (Distractor) | significantly lower than Gold |
| Improvement | ≥ 25% (≥ 30% preferred) |

***Reminder: vPass@k is an average validator score across k samples, not “at least one pass.”***

## **9\. Common Pitfalls**

### **9.1 Design Pitfalls**

| Pitfall | Problem | Solution |
| :---- | :---- | :---- |
| Guessable without context | Model can use common sense | Make rules arbitrary/fictional |
| Multiple valid answers | No single correct output | Ensure deterministic rules |
| Ambiguous rules | Unclear what to do in edge cases | Define ALL edge cases explicitly |
| Too simple | High Stage 2 pass rate (\>60%) | Add more rules/complexity |
| Too complex | Very low Stage 2 pass rate (\<15%) | Simplify or add more examples |

### **9.2 Context Pitfalls**

| Pitfall | Problem | Solution |
| :---- | :---- | :---- |
| Context too short | Model uses parametric knowledge | Ensure 3K+ tokens |
| Missing definitions | Undefined terms used | Define ALL terms explicitly |
| Incomplete rules | Some scenarios not covered | Test all input variations |
| Real-world overlap | Maps to known APIs/systems | Invent fictional systems |

### **9.3 Validator Pitfalls**

| Pitfall | Problem | Solution |
| :---- | :---- | :---- |
| Too strict | Rejects valid formatting variations | Normalize before comparing |
| Too lenient | Accepts wrong answers | Test validator with wrong inputs |
| No partial credit | All-or-nothing scoring | Implement per-field scoring |
| Crashes on bad input | Unhandled exceptions | Wrap in try/except |

## **10\. Quality Checklist**

Use this checklist before submitting your task:

**Prompt checklist:**

Prompt is context forcing can't solve without rules.

Input is messy/ambiguous forces normalization.

Requires 4-8 tool calls.

Has clear dependencies between steps.

Includes concrete values (dates, amounts, emails).

**System prompt checklist:**

All tools have clear parameter schemas.

Required vs optional clearly marked.

Allowed values/enums specified.

Output placeholders documented.

Dependency relationships explained.

**Golden answer checklist:**

Valid JSON array format.

All required parameters present.

Placeholders used for dependencies.

Wrapped in block markers.

No extra prose.

**Validator checklist:**

Handles multiple response formats.

Golden self check returns 1.0.

Wrong order returns 0.0.

Missing tools return 0.0.

Placeholder linking scores \>0.25.

Literal linking scores \<0.25.

Unit tests all pass.

**Context checklist:**

Stage 1: Empty (no context).

Stage 2: Complete,authoritative rules.

Stage 3: Same info,different order.

Stage 4: Plausible but wrong rules.

**Model breaking:**

Stage 1 pass rate \= 0%

Stage 2 pass rate \> 70% (for good models)

Stage 4 pass rate \< 20%

Improvement (stage 2 \- stage 1\) \> 25%

## **Quick Reference Card**

╔════════════════════════════════════════════════════════════════════╗  
║  COMPLEX PROCEDURAL TASKS \- QUICK REFERENCE                        ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  Category:        Complex Procedural Tasks                         ║  
║  Sub-categories:  Pattern A | Pattern B | Without Tools            ║  
║  Prog. Languages: OPTIONAL                                         ║  
║                                                                    ║  
║  Context Length:  3K \- 12K tokens                                  ║  
║  Stage 1 Target:  0% (must fail without context)                   ║  
║  Stage 2 Target:  25-50% (sweet spot)                              ║  
║  Improvement:     ≥25% required                                    ║  
║                                                                    ║  
║  Key Principle:   FOLLOW A PROCESS, not produce good answers       ║  
║                                                                    ║  
║  Must Have:                                                        ║  
║  ✓ Deterministic output (one correct answer)                       ║  
║  ✓ Complete rules (all decisions explicit)                         ║  
║  ✓ Novel system (not real-world API)                              ║  
║  ✓ Automatic validation (checker can verify)                       ║  
║                                                                    ║  
║  Must NOT Have:                                                    ║  
║  ✗ Common sense solutions                                          ║  
║  ✗ Multiple valid answers                                          ║  
║  ✗ Real-world API mappings                                         ║  
║  ✗ Ambiguous rules                                                 ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

## **Appendix: Notebook Template for Complex Procedural Tasks**

### **Cell 1: Metadata**

\# Metadata

Category: \- Complex Procedural Tasks

Sub-category: \- \[Choose one\]:  
\- With tools — System instructions \+ prompt ⇒ tool calls  
\- With tools — system instructions \+ prompt \+ tool return ⇒ final response  
\- Without tools — Role-playing & complex workflow following

Topic: \- \[Your fictional system name\]

Model Breaking Assessment: \- https://mbpi-web-ui-rygx5x2g6q-as.a.run.app/share/...

Programming Languages: \- (Leave empty or specify if applicable)

### **Cells 2-3: Prompt**

\#\# Prompt

\[System instructions \+ User request\]

Output Format:  
Return a JSON object with the following structure:  
{  
  "field1": \<type\>,  
  "field2": \<type\>  
}

### **Cells 4-12: Context Stages**

Follow standard 4-stage structure (No Context, Gold, Shuffled, Distractor).

### **Cells 13-14: Golden Answer**

\#\# Response (Golden Answer)

Hey boss\! (｡･ω･｡)ﾉ Let me process this through the workflow\!

Based on the rules provided, here's the result:

\<\!-- Block-Start: {"name": "result", "version": 1} \--\>  
\`\`\`json  
{  
  "final\_output": "value",  
  "details": {...}  
}

\<\!-- Block-End: {"name": "result"} \--\>

Hope this helps, boss\! ✨

\#\#\# Cells 15-16: Validator

\`\`\`markdown  
\#\# Validator

import json  
import re

def extract\_json(text):  
    \# \[Include JSON extraction helper\]  
    pass

def check\_prediction(pred, expected) \-\> float:  
    """Validate procedural task output."""  
    try:  
        pred\_json \= extract\_json(str(pred))  
        exp\_json \= extract\_json(str(expected))

        if pred\_json is None or exp\_json is None:  
            return 0.0

        \# Compare all fields  
        correct \= 0  
        total \= len(exp\_json)

        for key in exp\_json:  
            if key in pred\_json and pred\_json\[key\] \== exp\_json\[key\]:  
                correct \+= 1

        return correct / total if total \> 0 else 0.0

    except Exception:  
        return 0.0

## **11\. Step-by-Step Development Workflow**

This section provides a complete walkthrough from idea to submission.

### **Phase 1: Ideation (Day 1\)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 1.1: Choose Your Sub-Category                             │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Ask yourself:                                                  │  
│  • Does my task involve calling a tool? → Pattern A or B        │  
│  • Does my task involve processing tool output? → Pattern B     │  
│  • Is it a pure workflow/state machine? → Without Tools         │  
│                                                                 │  
│  Decision Tree:                                                 │  
│                                                                 │  
│  Is there a tool call?                                          │  
│       │                                                         │  
│       ├── YES → Is the tool output provided?                    │  
│       │           │                                             │  
│       │           ├── YES → Pattern B                           │  
│       │           │                                             │  
│       │           └── NO → Pattern A                            │  
│       │                                                         │  
│       └── NO → Without Tools                                    │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 1.2: Define Your Fictional System                         │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  CRITICAL: Your system must be FICTIONAL.                       │  
│                                                                 │  
│  ❌ BAD: "Implement Stripe payment routing"                     │  
│  ✅ GOOD: "Implement ZetaPay v3.2 payment routing"              │  
│                                                                 │  
│  ❌ BAD: "Route AWS Lambda requests"                            │  
│  ✅ GOOD: "Route QuantumFlow compute requests"                  │  
│                                                                 │  
│  Why? Real systems can be solved using parametric knowledge.    │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 1.3: Draft Your Rules                                     │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Write down ALL rules in IF-THEN format:                        │  
│                                                                 │  
│  Rule 1: IF condition\_A THEN action\_X                           │  
│  Rule 2: IF condition\_B AND condition\_C THEN action\_Y           │  
│  Rule 3: IF condition\_D THEN action\_Z ELSE action\_W             │  
│                                                                 │  
│  Target: 8-15 rules for good complexity                         │  
│                                                                 │  
│  Rule Types to Include:                                         │  
│  • Threshold rules (IF score \> 80 THEN ...)                     │  
│  • Categorical rules (IF type \= "premium" THEN ...)             │  
│  • Compound rules (IF A AND B OR C THEN ...)                    │  
│  • Priority rules (Apply in order: Rule 1, Rule 2, Rule 3\)      │  
│  • Exception rules (IF special\_case THEN override ...)          │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 2: Validation Design (Day 1-2)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 2.1: Define Expected Output Format                        │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Before writing context, define EXACTLY what output you need:   │  
│                                                                 │  
│  Example for Pattern A:                                         │  
│  {                                                              │  
│    "tool": "route\_request",                                     │  
│    "parameters": {                                              │  
│      "queue": "high\_priority",                                  │  
│      "tags": \["urgent", "vip"\]                                  │  
│    }                                                            │  
│  }                                                              │  
│                                                                 │  
│  Example for Pattern B:                                         │  
│  {                                                              │  
│    "selected\_items": \["ID1", "ID2"\],                            │  
│    "total\_score": 85,                                           │  
│    "decision": "approved"                                       │  
│  }                                                              │  
│                                                                 │  
│  Example for Without Tools:                                     │  
│  {                                                              │  
│    "final\_state": "ESCALATED",                                  │  
│    "path": \["INIT", "REVIEW", "ESCALATED"\],                     │  
│    "flags": \["REQUIRES\_MANAGER"\]                                │  
│  }                                                              │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 2.2: Write the Validator FIRST                            │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  This is CRITICAL. Write validator before context.              │  
│                                                                 │  
│  Why? Ensures:                                                  │  
│  • Output is machine-verifiable                                 │  
│  • You've thought through edge cases                            │  
│  • Rules are actually deterministic                             │  
│                                                                 │  
│  Template:                                                      │  
│                                                                 │  
│  def check\_prediction(pred, expected) \-\> float:                 │  
│      try:                                                       │  
│          pred\_json \= extract\_json(str(pred))                    │  
│          exp\_json \= extract\_json(str(expected))                 │  
│                                                                 │  
│          if pred\_json is None:                                  │  
│              return 0.0                                         │  
│                                                                 │  
│          \# Add your validation logic here                       │  
│          \# Return 0.0 \- 1.0                                     │  
│                                                                 │  
│      except Exception:                                          │  
│          return 0.0                                             │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 2.3: Test Validator with Mock Data                        │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Test cases you MUST write:                                     │  
│                                                                 │  
│  1\. Perfect match → should return 1.0                           │  
│  2\. Completely wrong → should return 0.0                        │  
│  3\. Partial match → should return 0.0-1.0                       │  
│  4\. Malformed JSON → should return 0.0 (not crash)              │  
│  5\. Missing fields → should return 0.0 or partial               │  
│  6\. Extra fields → should still work                            │  
│                                                                 │  
│  \# Local test code (don't include in notebook):                 │  
│  assert check\_prediction(perfect\_answer, expected) \== 1.0       │  
│  assert check\_prediction(wrong\_answer, expected) \== 0.0         │  
│  assert check\_prediction("not json", expected) \== 0.0           │  
│  assert 0 \< check\_prediction(partial\_answer, expected) \< 1      │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 3: Context Creation (Day 2-3)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 3.1: Write Gold Context                                   │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Structure (in this order):                                     │  
│                                                                 │  
│  1\. SYSTEM OVERVIEW (200-300 words)                             │  
│     \- Name of the system (fictional)                            │  
│     \- Purpose statement                                         │  
│     \- Version number (adds authenticity)                        │  
│                                                                 │  
│  2\. DEFINITIONS (300-500 words)                                 │  
│     \- Define EVERY term used in rules                           │  
│     \- Define all states/statuses                                │  
│     \- Define all categories/types                               │  
│                                                                 │  
│  3\. RULES (500-1000 words)                                      │  
│     \- Numbered rules in IF-THEN format                          │  
│     \- Priority order explicitly stated                          │  
│     \- Edge cases covered                                        │  
│                                                                 │  
│  4\. INPUT/OUTPUT FORMATS (200-300 words)                        │  
│     \- Exact schema for inputs                                   │  
│     \- Exact schema for outputs                                  │  
│     \- Field descriptions                                        │  
│                                                                 │  
│  5\. WORKED EXAMPLES (500-800 words)                             │  
│     \- 2-3 complete examples                                     │  
│     \- Show reasoning step-by-step                               │  
│     \- Different scenarios covered                               │  
│                                                                 │  
│  Total target: 3,000 \- 8,000 tokens                             │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 3.2: Create Shuffled Context (Stage 3\)                    │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Take your Gold Context and REORDER sections:                   │  
│                                                                 │  
│  Gold Order:                                                    │  
│  \[Overview\] → \[Definitions\] → \[Rules\] → \[Formats\] → \[Examples\]  │  
│                                                                 │  
│  Shuffled Options:                                              │  
│  \[Examples\] → \[Rules\] → \[Definitions\] → \[Overview\] → \[Formats\]  │  
│  \[Formats\] → \[Examples\] → \[Overview\] → \[Rules\] → \[Definitions\]  │  
│                                                                 │  
│  IMPORTANT: Do NOT change any content, only order.              │  
│                                                                 │  
│  Checklist:                                                     │  
│  \[ \] All rules present                                          │  
│  \[ \] All examples present                                       │  
│  \[ \] All definitions present                                    │  
│  \[ \] No facts changed                                           │  
│  \[ \] Section headers adjusted if needed                         │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 3.3: Create Distractor Context (Stage 4\)                  │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Add CONFLICTING information to Gold Context:                   │  
│                                                                 │  
│  Technique 1: Contradictory Rules                               │  
│  ─────────────────────────────────────────                      │  
│  Original: "IF score \> 80 THEN approve"                         │  
│  Add: "\[Draft v1\] IF score \> 90 THEN approve"                   │  
│                                                                 │  
│  Technique 2: Wrong Thresholds                                  │  
│  ─────────────────────────────────────────                      │  
│  Original: "Priority levels: 1-5"                               │  
│  Add: "\[Deprecated\] Priority levels: 1-10"                      │  
│                                                                 │  
│  Technique 3: Conflicting Definitions                           │  
│  ─────────────────────────────────────────                      │  
│  Original: "VIP \= account age \> 2 years"                        │  
│  Add: "\[Legacy\] VIP \= total spend \> $10,000"                    │  
│                                                                 │  
│  IMPORTANT: Mark correct version clearly\!                       │  
│  Use: "Official v2.3", "Current Policy", "Active Rules"         │  
│  Mark distractors: "\[Draft\]", "\[Deprecated\]", "\[Legacy\]"        │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 4: Manual Verification (Day 3\)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 4.1: Manual Trace Test                                    │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  YOU must manually execute your rules and verify output.        │  
│                                                                 │  
│  Process:                                                       │  
│  1\. Read the input/prompt                                       │  
│  2\. Apply Rule 1 → write result                                 │  
│  3\. Apply Rule 2 → write result                                 │  
│  4\. ... continue for all rules                                  │  
│  5\. Compare final result with expected output                   │  
│                                                                 │  
│  Document your trace:                                           │  
│                                                                 │  
│  Input: {amount: 15000, type: "software", urgency: "high"}      │  
│  Rule 1: amount \> 10000 → TRUE → set level \= "L2"               │  
│  Rule 2: type \= "software" → TRUE → add flag "IT\_REVIEW"        │  
│  Rule 3: urgency \= "high" → TRUE → add flag "EXPEDITE"          │  
│  Rule 4: level \= "L2" AND flags.contains("EXPEDITE") → TRUE     │  
│          → final\_state \= "APPROVED\_EXPEDITED"                   │  
│  Expected: {state: "APPROVED\_EXPEDITED", flags: \[...\]}          │  
│  Match: ✅                                                      │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 4.2: Non-Expert Test                                      │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Ask someone unfamiliar with the domain to follow your rules.   │  
│                                                                 │  
│  Give them:                                                     │  
│  • The Gold Context                                             │  
│  • The input/prompt                                             │  
│  • Paper and pen                                                │  
│                                                                 │  
│  Ask them to:                                                   │  
│  • Produce the output by following rules mechanically           │  
│  • Note any confusion or ambiguity                              │  
│                                                                 │  
│  If they get the right answer: ✅ Good task                     │  
│  If they're confused: ❌ Rules need clarification               │  
│  If they use "common sense": ❌ Task is too guessable           │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 5: Notebook Assembly (Day 3-4)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 5.1: Create Notebook File                                 │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Use VS Code or Jupyter to create 16-cell structure:            │  
│                                                                 │  
│  Cell 1:  \[Markdown\] Metadata                                   │  
│  Cell 2:  \[Markdown\] \#\# Prompt                              │  
│  Cell 3:  \[Markdown\] System \+ User prompt                       │  
│  Cell 4:  \[Markdown\] \#\# Context                             │  
│  Cell 5:  \[Markdown\] \#\#\# Stage 1 (No Context)               │  
│  Cell 6:  \[Markdown\] "No additional information provided..."    │  
│  Cell 7:  \[Markdown\] \#\#\# Stage 2 Gold Context               │  
│  Cell 8:  \[Markdown\] \[Your Gold Context here\]                   │  
│  Cell 9:  \[Markdown\] \#\#\# Stage 3 Shuffled Context           │  
│  Cell 10: \[Markdown\] \[Your Shuffled Context here\]               │  
│  Cell 11: \[Markdown\] \#\#\# Stage 4 Distractor Context         │  
│  Cell 12: \[Markdown\] \[Your Distractor Context here\]             │  
│  Cell 13: \[Markdown\] \#\# Response (Golden Answer)            │  
│  Cell 14: \[Markdown\] \[Expected output in AiPy format\]           │  
│  Cell 15: \[Markdown\] \#\# Validator                           │  
│  Cell 16: \[Code\]     \[Validator function\]                       │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 5.2: Fill Metadata                                        │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  \# Metadata                                                     │  
│                                                                 │  
│  Category: \- Complex Procedural Tasks                       │  
│                                                                 │  
│  Sub-category: \- \[CHOOSE ONE\]:                              │  
│    • With tools — System instructions \+ prompt ⇒ tool calls     │  
│    • With tools — system instructions \+ prompt \+ tool return    │  
│      ⇒ final response                                           │  
│    • Without tools — Role-playing & complex workflow following  │  
│                                                                 │  
│  Topic: \- \[Your fictional system, e.g.,                     │  
│               "ZetaPay Payment Router v3.2"\]                    │  
│                                                                 │  
│  Model Breaking Assessment: \- \[Leave empty until tested\]    │  
│                                                                 │  
│  Programming Languages: \- \[Optional, can leave empty\]       │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 6: MBPI Evaluation (Day 4\)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 6.1: Run MBPI Evaluation                                  │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Option A: Web UI (Recommended)                                 │  
│  ─────────────────────────────────────────────────────────────  │  
│  1\. Go to: https://mbpi-web-ui-rygx5x2g6q-as.a.run.app/         │  
│  2\. Upload your .ipynb file                                     │  
│  3\. Wait for evaluation (5-10 minutes)                          │  
│  4\. Review results                                              │  
│                                                                 │  
│  Option B: CLI (Advanced)                                       │  
│  ─────────────────────────────────────────────────────────────  │  
│  python cli.py evaluate your\_notebook.ipynb                     │  
│                                                                 │  
│  With options:                                                  │  
│  python cli.py evaluate your\_notebook.ipynb \\                   │  
│    \--num-samples 16 \\                                           │  
│    \--max-concurrent 8                                           │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 6.2: Interpret Results                                    │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Check the model\_breaking\_assessment in results:                │  
│                                                                 │  
│  ✅ PASS Criteria:                                              │  
│  • All models: Stage 1 (No Context) \= 0%                        │  
│  • All models: Stage 2 (Gold Context) ≤ 95%                     │  
│  • At least one model: ≥25% improvement Stage 1 → Stage 2       │  
│                                                                 │  
│  Common Issues:                                                 │  
│                                                                 │  
│  Issue: Stage 1 \> 0%                                            │  
│  Fix: Task is guessable. Add more arbitrary/fictional rules.    │  
│                                                                 │  
│  Issue: Stage 2 \< 10%                                           │  
│  Fix: Context is too complex. Simplify or add more examples.    │  
│                                                                 │  
│  Issue: Stage 2 \> 60%                                           │  
│  Fix: Task may be too simple. Add more rules/complexity.        │  
│                                                                 │  
│  Issue: Improvement \< 25%                                       │  
│  Fix: Gold context doesn't help enough. Make rules clearer.     │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 7: Iteration (Day 4-5)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 7.1: Debug Failing Evaluations                            │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  If model\_breaking \= false, check:                              │  
│                                                                 │  
│  1\. Stage 1 too high? (Models passing without context)          │  
│     → Make rules more arbitrary/fictional                       │  
│     → Remove real-world patterns                                │  
│     → Add counter-intuitive rules                               │  
│                                                                 │  
│  2\. Stage 2 too low? (Models failing with context)              │  
│     → Simplify rules                                            │  
│     → Add more worked examples                                  │  
│     → Check for ambiguities                                     │  
│                                                                 │  
│  3\. Improvement too low? (Context doesn't help)                 │  
│     → Make context more authoritative                           │  
│     → Add explicit decision tables                              │  
│     → Include step-by-step reasoning in examples                │  
│                                                                 │  
│  4\. Validator issues?                                           │  
│     → Check if validator is too strict                          │  
│     → Test with actual model outputs                            │  
│     → Add format flexibility                                    │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **Phase 8: Submission (Day 5\)**

┌─────────────────────────────────────────────────────────────────┐  
│  STEP 8.1: Final Checklist Before Submission                    │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  \[ \] Notebook has exactly 16 cells                              │  
│  \[ \] Metadata has correct Category and Sub-category             │  
│  \[ \] MBPI evaluation shows model\_breaking \= true                │  
│  \[ \] Share link added to Model Breaking Assessment field        │  
│  \[ \] Validator function works (returns 0.0-1.0)                 │  
│  \[ \] Manual trace matches expected output                       │  
│  \[ \] All context stages present (4 stages)                      │  
│  \[ \] Golden answer in correct AiPy format                       │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

## **12\. MBPI Evaluation Tool Guide**

### **12.1 What is MBPI?**

MBPI (Model-Breaking Prompt Identifier) is the evaluation system that tests whether your task meets the model-breaking criteria.

┌─────────────────────────────────────────────────────────────────┐  
│  MBPI EVALUATION FLOW                                           │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  Your Notebook                                                  │  
│       │                                                         │  
│       ▼                                                         │  
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │  
│  │ Stage 1  │───▶│ Stage 2  │───▶│ Stage 3  │───▶│ Stage 4  │  │  
│  │(No Ctx)  │    │ (Gold)   │    │(Shuffled)│    │(Distract)│  │  
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │  
│       │               │               │               │         │  
│       ▼               ▼               ▼               ▼         │  
│  ┌──────────────────────────────────────────────────────────┐  │  
│  │              For Each Stage × Each Model:                 │  │  
│  │              • GPT-5.1 (16 samples)                       │  │  
│  │              • Claude Sonnet 4.5 (16 samples)             │  │  
│  │              • Gemini 3 Pro (16 samples)                  │  │  
│  │              • Hunyuan (1-4 samples)                      │  │  
│  └──────────────────────────────────────────────────────────┘  │  
│       │                                                         │  
│       ▼                                                         │  
│  ┌──────────────────────────────────────────────────────────┐  │  
│  │  Validate each response with your check\_prediction()      │  │  
│  │  Calculate vPass@k metrics                                │  │  
│  │  Assess model-breaking status                             │  │  
│  └──────────────────────────────────────────────────────────┘  │  
│       │                                                         │  
│       ▼                                                         │  
│  ┌──────────────────────────────────────────────────────────┐  │  
│  │  RESULT: model\_breaking \= true/false                      │  │  
│  │  \+ Detailed metrics per model per stage                   │  │  
│  └──────────────────────────────────────────────────────────┘  │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

### **12.2 Using the Web UI**

**URL:** https://mbpi-web-ui-rygx5x2g6q-as.a.run.app/

#### ***Step 1: Upload Notebook***

* Click "Upload" or drag-and-drop your .ipynb file  
* System validates notebook structure automatically

#### ***Step 2: Start Evaluation***

* Click "Run Evaluation"  
* Wait 5-10 minutes (depends on queue)  
* Progress shown in real-time

#### ***Step 3: View Results***

* See summary dashboard  
* Check model\_breaking\_assessment  
* View per-model, per-stage metrics

#### ***Step 4: Get Share Link***

* Click "Share" to get permanent link  
* Copy link to your notebook's Metadata cell

### **12.3 Understanding Results**

#### ***vPass@16 Metrics (Validator Pass Score)***

┌─────────────────────────────────────────────────────────────────┐  
│  UNDERSTANDING vPass@16 (Validator Pass Score)                  │  
├─────────────────────────────────────────────────────────────────┤  
│                                                                 │  
│  vPass@16 measures how completely a model response satisfies    │  
│  the validator checks across 16 samples.                        │  
│                                                                 │  
│  Formula: vPass@16 \= (sum of validator scores) / 16             │  
│                                                                 │  
│  For each response, the validator returns a score \[0.0 \- 1.0\]:  │  
│  • 0.0 \= Incorrect or missing solution                          │  
│  • 0.0 \- 1.0 \= Partially correct solution                       │  
│  • 1.0 \= Fully correct solution                                 │  
│                                                                 │  
│  Examples:                                                      │  
│  • All 16 samples score 0.0 → vPass@16 \= 0%                     │  
│  • 8 samples score 1.0, 8 score 0.0 → vPass@16 \= 50%            │  
│  • All 16 samples score 0.5 → vPass@16 \= 50%                    │  
│  • All 16 samples score 1.0 → vPass@16 \= 100%                   │  
│                                                                 │  
│  NOTE: vPass@16 is NOT the classical Pass@k formula used in     │  
│  HumanEval/MBPP. It measures degree of correctness, not just    │  
│  whether at least one sample passes.                            │  
│                                                                 │  
└─────────────────────────────────────────────────────────────────┘

#### ***Result JSON Structure***

{  
  "metadata": {  
    "notebook\_name": "your\_task.ipynb",  
    "category": "Complex Procedural Tasks",  
    "sub\_category": "With tools — System instructions \+ prompt ⇒ tool calls"  
  },  
  "model\_breaking\_assessment": {  
    "is\_model\_breaking": true,  
    "conditions\_met": {  
      "all\_stage1\_zero": true,  
      "all\_stage2\_below\_threshold": true,  
      "improvement\_requirement\_met": true  
    },  
    "improvements": {  
      "gpt": {"stage1": 0, "stage2": 37.5, "improvement": 37.5},  
      "claude": {"stage1": 0, "stage2": 43.75, "improvement": 43.75},  
      "gemini": {"stage1": 0, "stage2": 31.25, "improvement": 31.25}  
    }  
  },  
  "stages": {  
    "stage\_1\_no\_context": {  
      "gpt": {"vpass\_16": 0.0, "raw\_pass": "0/16"},  
      "claude": {"vpass\_16": 0.0, "raw\_pass": "0/16"},  
      "gemini": {"vpass\_16": 0.0, "raw\_pass": "0/16"}  
    },  
    "stage\_2\_gold\_context": {  
      "gpt": {"vpass\_16": 37.5, "raw\_pass": "6/16"},  
      "claude": {"vpass\_16": 43.75, "raw\_pass": "7/16"},  
      "gemini": {"vpass\_16": 31.25, "raw\_pass": "5/16"}  
    }  
  }  
}

### **12.4 CLI Usage**

For advanced users who prefer command line:

\# Basic evaluation  
python cli.py evaluate your\_notebook.ipynb

\# With more samples (more accurate but slower)  
python cli.py evaluate your\_notebook.ipynb \--num-samples 16

\# Batch evaluation  
python cli.py batch \--directory notebooks/

\# View help  
python cli.py \--help

### **12.5 Troubleshooting Evaluations**

| Symptom | Cause | Solution |
| :---- | :---- | :---- |
| "Validation error" | Notebook structure invalid | Check 16-cell structure |
| "Validator crashed" | Code error in check\_prediction | Wrap in try/except, return 0.0 |
| All stages 0% | Validator too strict | Relax matching, add normalization |
| All stages 100% | Validator too lenient | Check if always returning 1.0 |
| Timeout | Context too long | Reduce to \<12K tokens |

## **13\. Definition of Done**

A task is **DONE** when ALL of the following criteria are met:

### **13.1 Structural Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 1 | Notebook has exactly 16 cells | Count cells in Jupyter |
| 2 | Cell types match template (15 Markdown \+ 1 Code) | Check cell types |
| 3 | Category \= "Complex Procedural Tasks" | Check Metadata cell |
| 4 | Sub-category is one of 3 valid values | Check Metadata cell |
| 5 | Context length is 3K-12K tokens | Use token counter |

### **13.2 Content Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 6 | System is fictional (not real-world API) | Manual review |
| 7 | All rules written in IF-THEN format | Manual review |
| 8 | All terms defined explicitly | Manual review |
| 9 | 2-3 worked examples included | Manual review |
| 10 | Output format clearly specified | Manual review |

### **13.3 Context Stage Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 11 | Stage 1 has placeholder text | Check cell 6 |
| 12 | Stage 2 has complete Gold Context | Check cell 8 |
| 13 | Stage 3 is shuffled (same content, different order) | Compare to Stage 2 |
| 14 | Stage 4 has contradictions with correct version marked | Manual review |

### **13.4 Validator Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 15 | Function signature: \`check\_prediction(pred, expected) \-\> float\` | Code review |
| 16 | Returns value between 0.0 and 1.0 | Test validator |
| 17 | Handles malformed input without crashing | Test with bad input |
| 18 | Includes JSON extraction helper | Code review |

### **13.5 Evaluation Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 19 | MBPI evaluation completed | Check results JSON |
| 20 | \`model\_breaking \= true\` | Check assessment |
| 21 | Stage 1: All models \= 0% | Check metrics |
| 22 | Stage 2: All models ≤ 95% | Check metrics |
| 23 | Improvement: ≥25% for at least one model | Check metrics |
| 24 | Share link added to Metadata | Check Metadata cell |

### **13.6 Quality Requirements**

| \# | Requirement | Verification |
| :---- | :---- | :---- |
| 25 | Manual trace produces correct output | Execute rules by hand |
| 26 | Non-expert can follow rules | Have someone else try |
| 27 | No common sense shortcuts exist | Review carefully |
| 28 | No typos or formatting issues | Proofread |

## **14\. Review Criteria (For Reviewers)**

This section is for reviewers evaluating submitted Complex Procedural Tasks.

### **14.1 Quick Rejection Criteria**

Immediately reject if ANY of these are true:

╔════════════════════════════════════════════════════════════════════╗  
║  QUICK REJECTION CHECKLIST                                         ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  \[ \] model\_breaking \= false in MBPI results                        ║  
║  \[ \] Category is not "Complex Procedural Tasks"                    ║  
║  \[ \] Sub-category is missing or invalid                            ║  
║  \[ \] Notebook structure is not 16 cells                            ║  
║  \[ \] Validator function is missing or crashes                      ║  
║  \[ \] Task uses real-world API/system (not fictional)               ║  
║  \[ \] Task can be solved without reading context                    ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **14.2 Detailed Review Rubric**

#### ***Category A: Task Design (40 points)***

| Criterion | Points | Excellent (Full) | Acceptable (Half) | Poor (Zero) |
| :---- | :---- | :---- | :---- | :---- |
| Fictional system | 10 | Completely novel | Some overlap with real | Direct copy of real API |
| Rule completeness | 10 | All decisions explicit | Minor gaps | Major ambiguity |
| Determinism | 10 | Single correct answer | Rare edge ambiguity | Multiple valid answers |
| Complexity | 10 | 8-15 rules, good depth | 5-7 rules, moderate | \<5 rules, too simple |

#### ***Category B: Context Quality (30 points)***

| Criterion | Points | Excellent (Full) | Acceptable (Half) | Poor (Zero) |
| :---- | :---- | :---- | :---- | :---- |
| Gold Context | 10 | Complete, clear, authoritative | Minor issues | Missing key rules |
| Shuffled Context | 5 | Properly reordered | Minor overlap | Same as Gold |
| Distractor Context | 10 | Clear contradictions, correct marked | Some confusion | No contradictions |
| Examples | 5 | 2-3 complete worked examples | 1 example | No examples |

#### ***Category C: Technical Quality (20 points)***

| Criterion | Points | Excellent (Full) | Acceptable (Half) | Poor (Zero) |
| :---- | :---- | :---- | :---- | :---- |
| Validator accuracy | 10 | Correctly validates all cases | Minor issues | Incorrect results |
| Validator robustness | 5 | Handles all edge cases | Some crashes | Frequent crashes |
| Output format | 5 | Clear JSON structure | Minor format issues | Unclear format |

#### ***Category D: Evaluation Results (10 points)***

| Criterion | Points | Excellent (Full) | Acceptable (Half) | Poor (Zero) |
| :---- | :---- | :---- | :---- | :---- |
| Stage 1 | 3 | All models \= 0% | One model \> 0% | Multiple models \> 0% |
| Stage 2 | 4 | 25-50% range | 10-25% or 50-70% | \<10% or \>70% |
| Improvement | 3 | ≥30% | 25-30% | \<25% |

#### ***Scoring***

| Total Score | Decision |
| :---- | :---- |
| 85-100 | Accept |
| 70-84 | Accept with minor revisions |
| 50-69 | Major revisions required |
| \<50 | Reject |

### **14.3 Review Checklist**

\#\# Reviewer Checklist

\#\#\# Metadata  
\- \[ \] Category \= "Complex Procedural Tasks"  
\- \[ \] Sub-category is valid  
\- \[ \] Topic describes fictional system  
\- \[ \] MBPI share link present

\#\#\# Context Design  
\- \[ \] Fictional system (not real-world)  
\- \[ \] All rules in IF-THEN format  
\- \[ \] All terms defined  
\- \[ \] 2-3 worked examples  
\- \[ \] Output format specified  
\- \[ \] Context 3K-12K tokens

\#\#\# Stage Verification  
\- \[ \] Stage 1: Placeholder text only  
\- \[ \] Stage 2: Complete Gold Context  
\- \[ \] Stage 3: Same content, different order  
\- \[ \] Stage 4: Contains contradictions  
\- \[ \] Stage 4: Correct version clearly marked

\#\#\# Validator  
\- \[ \] Correct function signature  
\- \[ \] Returns 0.0-1.0  
\- \[ \] Handles malformed input  
\- \[ \] JSON extraction helper included

\#\#\# MBPI Results  
\- \[ \] model\_breaking \= true  
\- \[ \] Stage 1: All models \= 0%  
\- \[ \] Stage 2: All models ≤ 95%  
\- \[ \] Improvement: ≥25%

\#\#\# Quality  
\- \[ \] Manual trace produces correct output  
\- \[ \] No common sense shortcuts  
\- \[ \] Rules are deterministic

\#\#\# Final Decision: \[ \] Accept \[ \] Revise \[ \] Reject

Reviewer: \_\_\_\_\_\_\_\_\_\_\_\_\_  
Date: \_\_\_\_\_\_\_\_\_\_\_\_\_  
Comments:

## **15\. Anti-Patterns (Bad Examples)**

Learn what NOT to do by studying these anti-patterns.

### **15.1 Anti-Pattern: Real-World API Mapping**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Real Stripe Payment Processing                            ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  PROMPT:                                                           ║  
║  "You are a Stripe payment processing assistant. Route the         ║  
║   following payment to the correct queue based on amount and       ║  
║   currency."                                                       ║  
║                                                                    ║  
║  WHY IT FAILS:                                                     ║  
║  • Models have parametric knowledge of Stripe API                  ║  
║  • Stage 1 will pass (models know Stripe)                          ║  
║  • Not testing context learning, testing memorization              ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Fictional Payment System                                 ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  PROMPT:                                                           ║  
║  "You are a ZetaPay v3.2 payment processing assistant. Route the   ║  
║   following payment according to the ZetaPay Routing Protocol."    ║  
║                                                                    ║  
║  WHY IT WORKS:                                                     ║  
║  • ZetaPay doesn't exist \- no parametric knowledge                 ║  
║  • Models MUST read context to understand rules                    ║  
║  • Stage 1 will fail, Stage 2 can succeed                          ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **15.2 Anti-Pattern: Common Sense Solvable**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Obvious Priority Routing                                  ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  RULES:                                                            ║  
║  • IF customer is VIP → high priority                              ║  
║  • IF issue is critical → high priority                            ║  
║  • IF first contact → needs follow-up                              ║  
║                                                                    ║  
║  WHY IT FAILS:                                                     ║  
║  • Any human would make same decisions                             ║  
║  • Rules match common sense expectations                           ║  
║  • Models can "guess" correct answers                              ║  
║  • Stage 1 will likely pass                                        ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Counter-Intuitive Rules                                  ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  RULES:                                                            ║  
║  • IF customer is VIP AND account\_age \< 1 year → DEPRIORITIZE      ║  
║    (new VIPs are testing period, not truly VIP yet)                ║  
║  • IF issue is critical AND time \< 9AM → route to OVERNIGHT\_QUEUE  ║  
║    (critical issues before 9AM handled by night shift)             ║  
║  • IF total\_tickets\_today \> 5 → add RATE\_LIMIT flag                ║  
║    (frequent contacts get throttled)                               ║  
║                                                                    ║  
║  WHY IT WORKS:                                                     ║  
║  • Rules are arbitrary/fictional                                   ║  
║  • Counter-intuitive to common sense                               ║  
║  • Models CANNOT guess, must read context                          ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **15.3 Anti-Pattern: Multiple Valid Answers**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Subjective Ranking                                        ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  PROMPT:                                                           ║  
║  "Rank these candidates from best to worst for the position."      ║  
║                                                                    ║  
║  RULES:                                                            ║  
║  • Consider experience, skills, and culture fit                    ║  
║  • Prioritize candidates who would be good team players            ║  
║                                                                    ║  
║  WHY IT FAILS:                                                     ║  
║  • "Good team player" is subjective                                ║  
║  • Multiple rankings could be valid                                ║  
║  • Cannot automatically validate                                   ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Deterministic Scoring                                    ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  PROMPT:                                                           ║  
║  "Score and rank these candidates using the QuantumHR v4 scoring   ║  
║   algorithm."                                                      ║  
║                                                                    ║  
║  RULES:                                                            ║  
║  • base\_score \= years\_experience × 5                               ║  
║  • IF has\_certification("QHR-A") → score \+= 15                     ║  
║  • IF department\_match → score \+= 10                               ║  
║  • IF score \> 50 AND years\_experience \< 2 → score \-= 20            ║  
║    (penalty for overqualified juniors)                             ║  
║  • SORT by score DESC, ties broken by employee\_id ASC              ║  
║                                                                    ║  
║  WHY IT WORKS:                                                     ║  
║  • Every calculation is explicit                                   ║  
║  • One correct ranking exists                                      ║  
║  • Automatically verifiable                                        ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **15.4 Anti-Pattern: Incomplete Rules**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Missing Edge Cases                                        ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  RULES:                                                            ║  
║  • IF amount \< 1000 → route to L1                                  ║  
║  • IF amount \> 5000 → route to L2                                  ║  
║                                                                    ║  
║  PROBLEM: What about amount \= 2500?                                ║  
║  • No rule covers 1000-5000 range                                  ║  
║  • Model must guess or use common sense                            ║  
║  • Different models may give different answers                     ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Complete Coverage                                        ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  RULES:                                                            ║  
║  • IF amount \< 1000 → route to L1                                  ║  
║  • IF amount \>= 1000 AND amount \<= 5000 → route to L1\_REVIEW       ║  
║  • IF amount \> 5000 → route to L2                                  ║  
║                                                                    ║  
║  OR use explicit ranges:                                           ║  
║  • \[0, 999\] → L1                                                   ║  
║  • \[1000, 5000\] → L1\_REVIEW                                        ║  
║  • \[5001, ∞\] → L2                                                  ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **15.5 Anti-Pattern: Validator Always Passes**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Lenient Validator                                         ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  def check\_prediction(pred, expected) \-\> float:                    ║  
║      \# Check if response contains any JSON                         ║  
║      if "{" in str(pred) and "}" in str(pred):                     ║  
║          return 1.0                                                ║  
║      return 0.0                                                    ║  
║                                                                    ║  
║  PROBLEM: Any JSON passes\!                                         ║  
║  • {"wrong": "answer"} would return 1.0                            ║  
║  • Doesn't validate actual content                                 ║  
║  • All stages will show artificially high pass rates               ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Strict Content Validation                                ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  def check\_prediction(pred, expected) \-\> float:                    ║  
║      try:                                                          ║  
║          pred\_json \= extract\_json(str(pred))                       ║  
║          exp\_json \= extract\_json(str(expected))                    ║  
║                                                                    ║  
║          if pred\_json is None:                                     ║  
║              return 0.0                                            ║  
║                                                                    ║  
║          \# Check each required field                               ║  
║          correct \= 0                                               ║  
║          for key in exp\_json:                                      ║  
║              if pred\_json.get(key) \== exp\_json\[key\]:               ║  
║                  correct \+= 1                                      ║  
║                                                                    ║  
║          return correct / len(exp\_json)                            ║  
║      except:                                                       ║  
║          return 0.0                                                ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

### **15.6 Anti-Pattern: Context Too Short**

╔════════════════════════════════════════════════════════════════════╗  
║  ❌ BAD: Minimal Context                                           ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  GOLD CONTEXT (500 tokens):                                        ║  
║  "Route high priority tickets to L2. Route VIP to VIP queue."      ║  
║                                                                    ║  
║  PROBLEM:                                                          ║  
║  • Too short \- model uses parametric knowledge                     ║  
║  • Not enough detail for complex procedural task                   ║  
║  • Easy to guess without context                                   ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗  
║  ✅ GOOD: Comprehensive Context (3K+ tokens)                       ║  
╠════════════════════════════════════════════════════════════════════╣  
║                                                                    ║  
║  GOLD CONTEXT includes:                                            ║  
║  • System overview (200-300 words)                                 ║  
║  • Complete definitions section (300-500 words)                    ║  
║  • 10+ explicit rules (500-1000 words)                             ║  
║  • Input/output format specs (200-300 words)                       ║  
║  • 2-3 worked examples (500-800 words)                             ║  
║                                                                    ║  
║  Total: 3,000-5,000 tokens minimum                                 ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝

## **16\. Domain Ideas & Inspiration**

Need inspiration? Here are proven domain patterns that work well for Complex Procedural Tasks.

### **16.1 Enterprise Systems (High Success Rate)**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Ticket Routing | ZetaDesk Support Router v4.2 | Pattern A |
| Expense Approval | QuantumExpense Workflow v3.1 | Without Tools |
| Document Classification | ArchiveBot Classification Engine | Pattern B |
| Access Control | VaultGuard Permission Evaluator | Pattern A |
| Incident Response | AlertMatrix Escalation Protocol | Without Tools |

### **16.2 Financial Systems**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Loan Scoring | CreditPulse Risk Calculator v2.5 | Pattern B |
| Transaction Routing | PayFlow Routing Engine v4.0 | Pattern A |
| Fraud Detection | ShieldNet Alert Classifier | Pattern B |
| Invoice Processing | BillBot Validation Protocol | Without Tools |
| Portfolio Rebalancing | WealthMatrix Allocation Rules | Pattern B |

### **16.3 HR & Recruitment**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Candidate Scoring | TalentRank Evaluation v3.2 | Pattern B |
| Interview Routing | HireFlow Assignment Engine | Pattern A |
| Performance Review | ReviewBot Scoring Protocol | Without Tools |
| Leave Approval | TimeGuard Approval Workflow | Without Tools |
| Onboarding Tasks | NewStart Checklist Engine | Pattern A |

### **16.4 Gaming & Simulation**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Battle Resolution | CombatEngine Turn Calculator | Without Tools |
| Resource Allocation | ResourceMaster Distribution Rules | Pattern B |
| Quest Assignment | QuestBot Selection Protocol | Pattern A |
| Character Stats | StatForge Calculation Engine | Without Tools |
| Loot Distribution | TreasureMatrix Allocation v2.0 | Pattern B |

### **16.5 Scientific/Technical**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Lab Sample Routing | BioRoute Sample Classification | Pattern A |
| Experiment Scheduling | LabScheduler Priority Rules | Pattern B |
| Data Validation | DataGuard Quality Check v3.1 | Without Tools |
| Equipment Allocation | InstrumentBot Assignment | Pattern A |
| Result Classification | ResultClassifier Analysis Engine | Pattern B |

### **16.6 Logistics & Operations**

| Domain | Example System | Sub-Category |
| :---- | :---- | :---- |
| Package Routing | ShipMatrix Route Calculator | Pattern A |
| Inventory Allocation | StockBot Distribution Rules | Pattern B |
| Delivery Scheduling | DeliverNow Priority Engine | Without Tools |
| Warehouse Assignment | StorageBot Bin Selection | Pattern A |
| Order Fulfillment | FulfillFlow Processing Rules | Without Tools |

### **16.7 Creating Your Own Domain**

Follow this template to create a novel domain:

Domain Template:  
───────────────────────────────────────────────────────────  
1\. CHOOSE A REAL-WORLD ANALOG  
   Real: Stripe payment processing

2\. INVENT A FICTIONAL NAME  
   Fictional: ZetaPay Payment Protocol v3.2

3\. ADD UNIQUE TWISTS  
   • Arbitrary thresholds (e.g., 847 instead of 1000\)  
   • Counter-intuitive rules  
   • Fictional categories (e.g., "quantum priority level")  
   • Made-up terminology

4\. CREATE EXPLICIT RULES  
   • 8-15 rules minimum  
   • All in IF-THEN format  
   • Cover all edge cases

5\. ADD WORKED EXAMPLES  
   • 2-3 complete examples  
   • Show step-by-step reasoning  
───────────────────────────────────────────────────────────

## **17\. FAQ & Troubleshooting**

### **17.1 Frequently Asked Questions**

#### ***Q1: What if my task is too simple (Stage 2 \> 60%)?***

**A:** Add more complexity:

* Increase number of rules (target 10-15)  
* Add compound conditions (IF A AND B AND NOT C)  
* Add priority/ordering rules  
* Add exception cases  
* Make thresholds less intuitive (847 instead of 850\)

#### ***Q2: What if my task is too hard (Stage 2 \< 15%)?***

**A:** Simplify:

* Reduce number of rules (target 8-10)  
* Add more worked examples (3-4)  
* Simplify compound conditions  
* Add explicit decision tables  
* Make rules more explicit/detailed

#### ***Q3: Can I use real-world company names?***

**A:** **No.** Always use fictional names:

* ❌ "Stripe Payment Processing"  
* ✅ "ZetaPay Payment Protocol v3.2"  
* ❌ "AWS Lambda Router"  
* ✅ "QuantumFlow Compute Router v4.1"

#### ***Q4: Do I need programming languages for this category?***

**A:** **No.** Programming Languages is OPTIONAL for Complex Procedural Tasks. You can leave it empty.

#### ***Q5: How long should my context be?***

**A:** Target 3,000-12,000 tokens:

* Minimum: 3,000 tokens (forces context learning)  
* Ideal: 5,000-8,000 tokens  
* Maximum: 12,000 tokens (longer may timeout)

#### ***Q6: What if Stage 1 is not 0% for all models?***

**A:** Your task is guessable. Fix by:

* Making rules more arbitrary/counter-intuitive  
* Removing real-world patterns  
* Using fictional terminology throughout  
* Adding rules that contradict common sense

#### ***Q7: How do I handle ties in ranking tasks?***

**A:** Always define explicit tiebreakers:

Rule: SORT by score DESC  
Tiebreaker 1: IF scores equal, SORT by experience DESC  
Tiebreaker 2: IF still tied, SORT by id ASC

#### ***Q8: Can my validator give partial credit?***

**A:** **Yes.** Return float 0.0-1.0:

* 1.0 \= fully correct  
* 0.5 \= half correct (e.g., 2 of 4 fields correct)  
* 0.0 \= incorrect

### **17.2 Troubleshooting Guide**

#### ***Issue: "Notebook validation failed"***

SYMPTOMS:  
• Upload fails with validation error  
• CLI shows "Invalid notebook structure"

SOLUTIONS:  
1\. Check cell count (must be exactly 16\)  
2\. Check cell types (15 Markdown \+ 1 Code)  
3\. Verify Metadata cell has correct Category  
4\. Ensure Sub-category is one of 3 valid values  
5\. Check for special characters in cell content

#### ***Issue: "Validator always returns 0.0"***

SYMPTOMS:  
• All stages show 0% pass rate  
• Even correct-looking responses fail

SOLUTIONS:  
1\. Check JSON extraction \- is it finding the JSON?  
2\. Check string matching \- case sensitivity?  
3\. Check field names \- exact match required?  
4\. Add debug logging to validator:

   def check\_prediction(pred, expected) \-\> float:  
       pred\_json \= extract\_json(str(pred))  
       print(f"Extracted: {pred\_json}")  \# Debug  
       \# ... rest of validation

#### ***Issue: "Validator always returns 1.0"***

SYMPTOMS:  
• All stages show 100% pass rate  
• Wrong answers are marked correct

SOLUTIONS:  
1\. Check if you're comparing actual content  
2\. Make sure you're not just checking JSON structure  
3\. Verify each field is being compared:

   \# BAD:  
   if pred\_json is not None:  
       return 1.0  \# Always passes if any JSON found

   \# GOOD:  
   if pred\_json.get("field") \== exp\_json.get("field"):  
       return 1.0

#### ***Issue: "Stage 1 not zero"***

SYMPTOMS:  
• Models pass without context  
• model\_breaking \= false

ROOT CAUSES:  
1\. Task maps to real-world system  
2\. Rules match common sense  
3\. Terminology is guessable

SOLUTIONS:  
1\. Rename system to fictional name  
2\. Make rules counter-intuitive  
3\. Use arbitrary thresholds (847 not 850\)  
4\. Add rules that contradict intuition

#### ***Issue: "Low improvement (\< 25%)"***

SYMPTOMS:  
• Stage 1 \= 0% (good)  
• Stage 2 \= 15% (too low)  
• Improvement \< 25%

ROOT CAUSES:  
1\. Context is too complex  
2\. Rules are ambiguous  
3\. Not enough examples

SOLUTIONS:  
1\. Simplify rules (remove compound conditions)  
2\. Add more worked examples (3-4)  
3\. Make output format simpler  
4\. Add explicit decision tables

#### ***Issue: "Timeout during evaluation"***

SYMPTOMS:  
• Evaluation hangs  
• "Timeout" error

ROOT CAUSES:  
1\. Context too long (\>12K tokens)  
2\. Network issues  
3\. API rate limits

SOLUTIONS:  
1\. Reduce context length to \<10K tokens  
2\. Try again later  
3\. Use CLI with \--max-concurrent 4

## **18\. Glossary**

| Term | Definition |
| :---- | :---- |
| CLB | Context Learning Benchmark \- the evaluation framework |
| Complex Procedural Tasks | Category where models must execute procedures following explicit rules |
| Context Learning | Ability to learn from information provided in context (not parametric knowledge) |
| Deterministic | Having only one correct output for any given input |
| Distractor Context | Stage 4 context with contradictory information |
| Gold Context | Stage 2 context with complete, authoritative rules |
| MBPI | Model-Breaking Prompt Identifier \- the evaluation tool |
| Model-Breaking | A task where models fail without context but succeed with context |
| Parametric Knowledge | Information stored in model weights from training |
| Pattern A | Sub-category: system \+ prompt → tool call |
| Pattern B | Sub-category: system \+ prompt \+ tool return → final response |
| Shuffled Context | Stage 3 context with same information in different order |
| Stage 1 | No Context \- baseline test (models should fail) |
| Stage 2 | Gold Context \- authoritative information (models should succeed) |
| Stage 3 | Shuffled Context \- reordered information |
| Stage 4 | Distractor Context \- mixed with contradictions |
| Sub-category | One of three types within Complex Procedural Tasks |
| Validator | Function that checks if model output is correct |
| vPass@16 | Validated pass rate with 16 samples |
| Without Tools | Sub-category: role-playing & workflow following without tool calls |

