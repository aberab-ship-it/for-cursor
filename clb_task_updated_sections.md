# Updated CLB Tool-Call Task Sections

This document applies the review feedback and provides updated content for each section.

---

## 1) Prompt (Updated)

No changes required.  
The prompt remains exactly as provided because it was already scored 5/5.

---

## 2) Gold Context (Updated)

Apply the following correction in **Section 2 → Tool Definitions → `create_new_audit_trail`**:

```text
6. `create_new_audit_trail` - Add an audit trail record to track changes made to database records. (This tool can be called multiple times; each call uses the same schema.)  
   - Parameters:
     - `reference_id` (required): string - ID of the entity being audited
     - `reference_type` (required): enum - `user`, `fund`, `investor`, `subscription`, `commitment`, `redemption`, `trade`, `portfolio`, `holding`, `instrument`, `invoice`, `payment`, `document`, `report`, `nav`, `notification`
     - `action` (required): enum - `create`, `update`, `delete`, `approve`, `cancel`, `process`
     - `field_name` (required): string - Field that changed
     - `old_value` (required): text - Previous value
     - `new_value` (required): text - New value
```

All other Gold Context content remains unchanged.

---

## 3) Shuffled Context (Updated)

Apply the same correction in the shuffled version under **Tool Definitions → `create_new_audit_trail`**:

```text
6. `create_new_audit_trail` - Add an audit trail record to track changes made to database records. (This tool can be called multiple times; each call uses the same schema.)  
   - Parameters:
     - `reference_id` (required): string - ID of the entity being audited
     - `reference_type` (required): enum - `user`, `fund`, `investor`, `subscription`, `commitment`, `redemption`, `trade`, `portfolio`, `holding`, `instrument`, `invoice`, `payment`, `document`, `report`, `nav`, `notification`
     - `action` (required): enum - `create`, `update`, `delete`, `approve`, `cancel`, `process`
     - `field_name` (required): string - Field that changed
     - `old_value` (required): text - Previous value
     - `new_value` (required): text - New value
```

All other Shuffled Context content remains unchanged.

---

## 4) Distractor Context (Updated)

Apply the same correction in the distractor version under **Tool Definitions → `create_new_audit_trail`**:

```text
6. `create_new_audit_trail` - Add an audit trail record to track changes made to database records. (This tool can be called multiple times; each call uses the same schema.)  
   - Parameters:
     - `reference_id` (required): string - ID of the entity being audited
     - `reference_type` (required): enum - `user`, `fund`, `investor`, `subscription`, `commitment`, `redemption`, `trade`, `portfolio`, `holding`, `instrument`, `invoice`, `payment`, `document`, `report`, `nav`, `notification`
     - `action` (required): enum - `create`, `update`, `delete`, `approve`, `cancel`, `process`
     - `field_name` (required): string - Field that changed
     - `old_value` (required): text - Previous value
     - `new_value` (required): text - New value
```

All other Distractor Context content remains unchanged.

---

## 5) Expected Answer (Updated)

```json
{
  "tools": [
    {
      "name": "approval_lookup",
      "arguments": {
        "action": "investor_onboarding",
        "requester_email": "danielle.johnson@investment.com"
      }
    },
    {
      "name": "create_investor",
      "arguments": {
        "legal_name": "India Limited",
        "registration_number": 72212345,
        "source_of_funds": "dividend_income",
        "contact_email": "india@limited.in",
        "accreditation_status": "accredited",
        "compliance_officer_approval": true
      }
    },
    {
      "name": "create_new_audit_trail",
      "arguments": {
        "reference_id": "176",
        "reference_type": "investor",
        "action": "create",
        "field_name": "event",
        "old_value": "",
        "new_value": "INVESTOR_ONBOARDED"
      }
    },
    {
      "name": "approval_lookup",
      "arguments": {
        "action": "portfolio_creation",
        "requester_email": "danielle.johnson@investment.com"
      }
    },
    {
      "name": "transfer_to_human",
      "arguments": {
        "summary": "ERROR_MISSING_REQUIRED_APPROVAL: automatic portfolio creation requires Fund Manager or Finance Officer approval; requester danielle.johnson@investment.com is compliance_officer. Commitment processing halted for human intervention."
      }
    }
  ]
}
```

Why this fix is compliant:
- Removes fabricated `fund_manager_approval`.
- Follows mandatory halt on missing approval.
- Uses full audit trail schema (`field_name`, `old_value`, `new_value`) per standardized rules.

---

## 6) Checker Function (Updated)

Use the updated checker from:

`/workspace/validator_fixed.py`

It fixes the review issues by:
- validating tool calls as a list (not name-keyed dict),
- correctly handling repeated tool names,
- using clear score math (`matched_tool_calls + passed_order_edges` over total checks),
- including improved unit tests (full pass, full fail, realistic partial pass).

