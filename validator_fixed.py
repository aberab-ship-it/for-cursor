import copy
import json
from typing import Any, Dict, List, Optional


expected = {
    "tools": [
        {
            "name": "approval_lookup",
            "arguments": {
                "action": "investor_onboarding",
                "requester_email": "danielle.johnson@investment.com",
            },
        },
        {
            "name": "create_investor",
            "arguments": {
                "legal_name": "India Limited",
                "registration_number": 72212345,
                "source_of_funds": "dividend_income",
                "contact_email": "india@limited.in",
                "accreditation_status": "accredited",
                "compliance_officer_approval": True,
            },
        },
        {
            "name": "create_new_audit_trail",
            "arguments": {
                "reference_id": "176",
                "reference_type": "investor",
                "action": "create",
                "field_name": "event",
                "old_value": "",
                "new_value": "INVESTOR_ONBOARDED",
            },
        },
        {
            "name": "approval_lookup",
            "arguments": {
                "action": "portfolio_creation",
                "requester_email": "danielle.johnson@investment.com",
            },
        },
        {
            "name": "transfer_to_human",
            "arguments": {
                "summary": "ERROR_MISSING_REQUIRED_APPROVAL: automatic portfolio creation requires Fund Manager or Finance Officer approval; requester danielle.johnson@investment.com is compliance_officer. Commitment processing halted for human intervention."
            },
        },
    ]
}


def _as_dict(obj: Any) -> Dict[str, Any]:
    return obj if isinstance(obj, dict) else {}


def _as_tool_list(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    tools = payload.get("tools", [])
    if not isinstance(tools, list):
        return []

    normalized: List[Dict[str, Any]] = []
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        name = tool.get("name")
        arguments = tool.get("arguments")
        if isinstance(name, str) and isinstance(arguments, dict):
            normalized.append({"name": name, "arguments": arguments})
    return normalized


def extract_json_answer(pred: Any) -> Dict[str, Any]:
    return _as_dict(pred)


def extract_code_answer(pred: Any) -> str:
    pred_dict = _as_dict(pred)

    code = pred_dict.get("code")
    if isinstance(code, str):
        return code

    program = pred_dict.get("program")
    if isinstance(program, str):
        return program

    return ""


def extract_freeform_answer(pred: Any) -> str:
    pred_dict = _as_dict(pred)

    text = pred_dict.get("model_output")
    if isinstance(text, str):
        return text

    answer = pred_dict.get("answer")
    if isinstance(answer, str):
        return answer

    return ""


def extract_tool_payload(obj: Any) -> Dict[str, Any]:
    d = _as_dict(obj)
    if not d:
        return {}

    if isinstance(d.get("tools"), list):
        return d

    for k in ("answer", "output", "result", "parsed"):
        inner = d.get(k)
        if isinstance(inner, dict) and isinstance(inner.get("tools"), list):
            return inner

    if extract_code_answer(d):
        return {}

    if extract_freeform_answer(d):
        return {}

    resp = d.get("response")
    if isinstance(resp, str):
        s = resp.strip()
        if s.startswith("{") and s.endswith("}"):
            try:
                parsed = json.loads(s)
                if isinstance(parsed, dict):
                    return parsed
            except json.JSONDecodeError:
                return {}

    return {}


def _first_index(
    tools: List[Dict[str, Any]],
    name: str,
    arg_pred=None,
) -> Optional[int]:
    for i, tool in enumerate(tools):
        if tool.get("name") != name:
            continue
        args = tool.get("arguments", {})
        if arg_pred is None or arg_pred(args):
            return i
    return None


def _count_matching_tool_calls(
    pred_tools: List[Dict[str, Any]],
    exp_tools: List[Dict[str, Any]],
) -> int:
    remaining = copy.deepcopy(pred_tools)
    matched = 0

    for exp_tool in exp_tools:
        match_idx = None
        for i, pred_tool in enumerate(remaining):
            if (
                pred_tool.get("name") == exp_tool.get("name")
                and pred_tool.get("arguments") == exp_tool.get("arguments")
            ):
                match_idx = i
                break
        if match_idx is not None:
            matched += 1
            remaining.pop(match_idx)

    return matched


def check_prediction(pred: dict, expected: dict) -> float:
    try:
        pred_json = extract_tool_payload(pred)
        exp_json = extract_tool_payload(expected)

        if not pred_json or not exp_json:
            return 0.0

        pred_tools = _as_tool_list(pred_json)
        exp_tools = _as_tool_list(exp_json)

        if not exp_tools:
            return 1.0

        if not pred_tools:
            return 0.0

        passed = _count_matching_tool_calls(pred_tools, exp_tools)
        total_tests = len(exp_tools)

        edge_rules = [
            # approval_lookup(investor_onboarding) -> create_investor
            (
                "approval_lookup",
                lambda a: a.get("action") == "investor_onboarding",
                "create_investor",
                None,
            ),
            # create_investor -> create_new_audit_trail(investor)
            (
                "create_investor",
                None,
                "create_new_audit_trail",
                lambda a: a.get("reference_type") == "investor",
            ),
            # create_new_audit_trail(investor) -> approval_lookup(portfolio_creation)
            (
                "create_new_audit_trail",
                lambda a: a.get("reference_type") == "investor",
                "approval_lookup",
                lambda a: a.get("action") == "portfolio_creation",
            ),
            # approval_lookup(portfolio_creation) -> transfer_to_human
            (
                "approval_lookup",
                lambda a: a.get("action") == "portfolio_creation",
                "transfer_to_human",
                None,
            ),
        ]

        total_tests += len(edge_rules)

        for from_name, from_pred, to_name, to_pred in edge_rules:
            from_i = _first_index(pred_tools, from_name, from_pred)
            to_i = _first_index(pred_tools, to_name, to_pred)
            if from_i is not None and to_i is not None and from_i < to_i:
                passed += 1

        return passed / total_tests

    except (TypeError, KeyError, ValueError) as e:
        print(f"[validator error] {e}")
        return 0.0


def __run_unittests():
    eps = 1e-6

    # Test 1: full-pass
    pred_full_pass = copy.deepcopy(expected)
    score = check_prediction(pred_full_pass, expected)
    assert abs(score - 1.0) <= eps

    # Test 2: full-fail
    pred_full_fail = {
        "tools": [
            {
                "name": "list_users",
                "arguments": {"username": "WRONG_USERNAME"},
            }
        ]
    }
    score = check_prediction(pred_full_fail, expected)
    assert score == 0.0

    # Test 3: partial-pass (missing required investor audit call)
    pred_partial = {
        "tools": [
            {
                "name": "approval_lookup",
                "arguments": {
                    "action": "investor_onboarding",
                    "requester_email": "danielle.johnson@investment.com",
                },
            },
            {
                "name": "create_investor",
                "arguments": {
                    "legal_name": "India Limited",
                    "registration_number": 72212345,
                    "source_of_funds": "dividend_income",
                    "contact_email": "india@limited.in",
                    "accreditation_status": "accredited",
                    "compliance_officer_approval": True,
                },
            },
            {
                "name": "approval_lookup",
                "arguments": {
                    "action": "portfolio_creation",
                    "requester_email": "danielle.johnson@investment.com",
                },
            },
            {
                "name": "transfer_to_human",
                "arguments": {
                    "summary": "ERROR_MISSING_REQUIRED_APPROVAL: automatic portfolio creation requires Fund Manager or Finance Officer approval; requester danielle.johnson@investment.com is compliance_officer. Commitment processing halted for human intervention."
                },
            },
        ]
    }
    score = check_prediction(pred_partial, expected)
    assert 0.0 < score < 1.0


if __name__ == "__main__":
    __run_unittests()
