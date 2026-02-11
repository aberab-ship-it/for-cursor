## **Pattern A Reviewers Guidelines**

### **1) Prompt Best Practices (Pattern A–aligned)**

## **Goal:** The prompt presents a scenario that requires the model to *determine which tool to call and with what parameters*, based on context rules.

* ## **Context-forcing**: The prompt must be unsolvable without Stage 2 rules (no "common sense" tool selection).

* ## **Single objective**: One clear deliverable (e.g., "output the correct tool call as JSON"), not multiple goals.

* ## **Scenario with concrete values**:

  * ## Include specific data: IDs, amounts, dates, flags, customer types, etc.

  * ## These values feed into parameter extraction rules.

* ## **No tool hints**: Prompt should NOT reveal which tool to select or hint at parameter values.

* ## **Determinism hooks**: If multiple tools could apply, rules in context must disambiguate.

* ## **No hidden assumptions**: Everything needed to determine the tool call must be in prompt + Stage 2.

* ## **Explicit output contract**: Define the tool call JSON structure expected.

## ---

### **2) Stage 1 (No Context) Best Practices (Pattern A–aligned)**

## **Goal:** With no Stage 2 rules, the model should *fail to select the correct tool or produce correct parameters*.

* ## **Truly empty**: "No additional information provided." That's it.

* ## **No hints**: Don't leak tool names, parameter schemas, routing rules, or examples here.

* ## **Should fail**: If Stage 1 can pass via general reasoning, the task isn't context-learning.

## ---

### **3) Stage 2 (Gold Context) Best Practices (Pattern A–aligned)**

## **Goal:** Define the **tool selection logic and parameter extraction rules** that determine exactly one correct tool call.

#### **3.1 Define all available tools completely**

* ## 4-8 fictional tools with unique purposes.

* ## Each tool has: name, description, parameter schema.

* ## Parameters: mark required vs optional, specify types, define allowed values (enums, ranges).

* ## Use fictional tool names (not real APIs like Stripe, Jira, Salesforce).

#### **3.2 Define routing/selection rules explicitly**

* ## Write rules as numbered IF-THEN statements (e.g., "IF VIP customer → use route_vip tool").

* ## Define priority/precedence when multiple rules could apply.

* ## Include 5-15 explicit rules covering all decision paths.

* ## Handle edge cases (what if multiple conditions match? what's the default?).

#### **3.3 Define parameter extraction rules**

* ## How to map scenario values to parameter values.

* ## Formulas for computed parameters (e.g., "priority = base + 2 if error_500").

* ## Enum mappings (e.g., "VIP → queue = 'VIP_dedicated'").

* ## Caps, limits, defaults for parameters.

#### **3.4 Guarantee "one correct tool call" from the rules (deterministic spec)**

* ## Complete tie-breakers for tool selection.

* ## Clear precedence when rules conflict.

* ## One deterministic path through the decision tree.

#### **3.5 Make it context-forcing**

* ## Use fictional systems + arbitrary thresholds that aren't guessable.

* ## Avoid rules that match common API patterns models might know.

#### **3.6 Specify output format precisely**

* ## Strict tool call schema: `{"tool": "...", "parameters": {...}}`

* ## Define required and optional parameters per tool.

* ## State what to omit: "No extra keys" or "Extra keys ignored".

#### **3.7 Examples should teach the procedure, not leak the answer**

* ## 2-3 worked examples showing: scenario → rule application → tool call.

* ## Use examples *different from the evaluation instance*.

#### **3.8 Align Stage 2 with what the validator checks**

* ## Every validated field must be stated in Stage 2.

* ## Every critical rule should be validated.

## ---

### **4) Stage 3 (Shuffled Context) Best Practices (Pattern A–aligned)**

## **Goal:** Same tool definitions + same routing rules, just harder to read.

* ## **Exact same content as Stage 2**: no edits, no paraphrase, no additions, no deletions.

* ## **Only reorder**: shuffle sections/paragraphs; keep every rule intact.

* ## **Preserve identifiers**: keep version labels, tool names, and rule IDs unchanged.

* ## **Avoid accidental clarifications**: don't add headings/summaries not present in Stage 2.

## ---

### **5) Stage 4 (Distractor Context) Best Practices (Pattern A–aligned)**

## **Goal:** Provide plausible wrong routing rules that lead to wrong tool selection or parameters.

* ## **Plausible but wrong**: add conflicting routing rules that sound legit but select different tools.

* ## **Clearly mark authority**: include an explicit “authoritative” ruleset marker (e.g., **ACTIVE vX.Y** / **OFFICIAL**), and include one or more alternative rulesets marked as **LEGACY / DRAFT / EXPERIMENTAL**.

  * ## Avoid labels like “correct/wrong”; use *document authority* markers instead.

* ## **Target common model mistakes**:

  * ## Wrong tool selection rules

  * ## Wrong parameter mappings

  * ## Wrong threshold boundaries (>, ≥)

  * ## Wrong priority calculations

  * ## Wrong enum values

* ## **Self-consistent distractor**: wrong rules should still "work" internally.

* ## **Mix correct and incorrect**: some rules should be right (makes it harder to detect wrong ones).

* ## **Don't overload**: 3-6 contradictions is usually enough.

## ---

### **6) Golden Answer Best Practices (Pattern A–aligned)**

## **Goal:** The golden answer is the *one correct tool call* from applying Stage 2 routing rules to the scenario.

* ## **Exactly one canonical tool call**:

  * ## One JSON blob with tool name + parameters.

  * ## No duplicates of the same payload elsewhere.

* ## **Strictly schema-compliant**:

  * ## Correct tool name (matches one defined in context).

  * ## All required parameters present.

  * ## Correct parameter values and types.

* ## **No prose if forbidden**:

  * ## If prompt says "JSON only", golden must be JSON only.

* ## **Stable formatting**:

  * ## Consistent indentation and key order.

* ## **Derivable from rules**:

  * ## Golden answer must be produced by applying the routing rules, not "chosen".

## ---

### **7) Validator Best Practices (Pattern A–aligned)**

## **Goal:** Score the *tool call correctness* (tool selection + parameters), with robust parsing and continuous scoring.

#### **7.1 Single source of truth**

* ## Keep exactly one canonical expected tool call (the golden answer).

* ## Derive expected tool name and parameters from `expected`, not duplicated constants.

#### **7.2 Check tool name first**

* ## Wrong tool name → score should be 0 or very low.

* ## Tool name is the most critical check.

#### **7.3 Check parameters systematically**

* ## All required parameters present.

* ## Each parameter value matches expected.

* ## Correct data types (string, int, array, etc.).

* ## Enum values within allowed set.

#### **7.4 Continuous scoring (prefer no hard gates)**

* ## Points for: correct tool name, each correct parameter, correct types.

* ## Score = passed checks / total checks.

* ## Avoid: "If tool wrong → return 0.0" (unless that's the design intent).

#### **7.5 Be robust to harmless formatting variation**

* ## Accept JSON via:

  * ## raw object

  * ## fenced code blocks

  * ## surrounding prose (if allowed by prompt)

* ## Normalize where reasonable: key order, whitespace.

#### **7.6 Make scoring granular and stable**

* ## Use boolean checks: tool_name_correct, param1_correct, param2_correct, etc.

* ## Return passed/total.

#### **7.7 Mandatory validator tests + recommended extras**

* ## **Required**

  * ## perfect answer ⇒ 1.0

  * ## empty/garbage ⇒ 0.0

  * ## wrong tool ⇒ 0.0 or low score

  * ## missing parameters ⇒ partial score

* ## **Recommended**

  * ## malformed JSON ⇒ 0.0 (no crash)

  * ## extra parameters ⇒ ignore or penalize (match Stage 2)

  * ## wrong parameter values ⇒ partial credit per field

#### **7.8 Determinism of validator (Pattern A note)**

* ## Validator must be deterministic (no randomness, time, external calls).

* ## Model variability is handled via parsing tolerance + continuous scoring.

## ---

## **Quick Author + Reviewer Checklist (Pattern A–aligned)**

### **Prompt**

* ## Scenario requires tool invocation

* ## Contains concrete values (IDs, amounts, dates)

* ## Does NOT hint at which tool to use

* ## Output format specified

### **Stage 2**

* ## 4-8 fictional tools with complete schemas

* ## 5-15 explicit routing rules (IF-THEN format)

* ## Parameter extraction rules defined

* ## Tie-breakers and precedence clear

* ## 2-3 worked examples included

* ## Every validated rule is stated

### **Validator**

* ## Checks tool name correctness

* ## Checks all required parameters

* ## Checks parameter values

* ## No crashes on malformed input

* ## Returns 0.0-1.0 continuous score

* ## Required tests included

## ---

## **Cross-cutting "do / don't" for Pattern A tasks**

### **Do**

* **Define all tool schemas completely** (name, params, types, required, enums).
* **Define routing rules as numbered IF-THEN statements**.
* **Define parameter extraction mappings explicitly**.
* **Use unique fictional tool names** (not real APIs).
* **Include 2-3 worked examples in Stage 2**.
* **Handle edge cases** (what if no rule matches? default behavior?).

### **Don't**

* **Don't use real API names** (Stripe, Jira, Salesforce, etc.).
* **Don't rely on common sense** ("call the obvious tool").
* **Don't allow multiple valid tool calls** (unless validator supports equivalence).
* **Don't leak tool names or routing logic in the prompt**.
* **Don't create "gotchas" that aren't encoded as rules**.

---

## **Quick reviewer checklist (copy/paste)**

* Prompt is context-forcing and doesn't hint at tool selection
* Prompt contains concrete scenario values (IDs, amounts, flags)
* Stage 1 contains no tools/rules/schema leaks
* Stage 2 has 4-8 fictional tools with complete schemas
* Stage 2 has 5-15 explicit routing rules
* Stage 3 is Stage 2 reordered only (no edits)
* Stage 4 has plausible contradictions, and authoritative rules are clearly marked
* Golden Answer is exactly one valid tool call JSON
* Golden Answer matches expected from applying rules
* Validator checks tool name + all parameters
* Validator returns continuous 0.0-1.0 score
* MBPI: No Context = 0%, Tencent Gold ≤ 35%, ≥25% improvement

