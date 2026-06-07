#!/usr/bin/env python3
"""PreToolUse hook: intercept reads of common secret-bearing files.
Blocks the real read and returns a redacted version instead.
Example/sample config files are always allowed through unredacted.
"""

import json
import os
import re
import sys
from pathlib import Path

data = json.load(sys.stdin)
fp = data.get("tool_input", {}).get("file_path", "")
name = os.path.basename(fp)
path_lower = fp.lower()

allowed_examples = (
    name.endswith(".example")
    or name.endswith(".example.json")
    or name.endswith(".example.yml")
    or name.endswith(".example.yaml")
    or name.endswith(".sample")
    or name.endswith(".sample.json")
    or name.endswith(".sample.yml")
    or name.endswith(".sample.yaml")
)

sensitive_path_patterns = [
    r"^\.env(\..+)?$",
    r".*\.key$",
    r".*\.pem$",
    r".*\.p12$",
    r".*\.pfx$",
    r"^terraform\.tfvars$",
    r"^\.npmrc$",
    r"^\.pypirc$",
    r"^appsettings\..+\.json$",
    r"^secrets\.ya?ml$",
]

is_sensitive = any(
    re.match(pattern, name, re.IGNORECASE) for pattern in sensitive_path_patterns
)

if not is_sensitive or allowed_examples:
    sys.exit(0)

sensitive_key_pattern = re.compile(
    r"SECRET|TOKEN|PASS|KEY|REFRESH|CREDENTIAL|PRIVATE|CERT|PWD|CLIENT_SECRET|API_KEY|ACCESS_KEY|CONNECTIONSTRING",
    re.IGNORECASE,
)

redacted_lines = []
try:
    with open(fp, encoding="utf-8", errors="replace") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                redacted_lines.append(line)
                continue

            kv_match = re.match(r"^([A-Za-z_][A-Za-z0-9_.-]*)\s*[:=]\s*(.*)$", line)
            if kv_match and sensitive_key_pattern.search(kv_match.group(1)):
                value = kv_match.group(2)
                replacement = "[redacted]" if value else "(empty)"
                separator = (
                    ":"
                    if ":" in line
                    and ("=" not in line or line.index(":") < line.index("="))
                    else "="
                )
                redacted_lines.append(
                    f"{kv_match.group(1)}{separator} {replacement}"
                    if separator == ":"
                    else f"{kv_match.group(1)}={replacement}"
                )
            else:
                redacted_lines.append(line)
except Exception as e:
    redacted_lines = [f"(could not read file safely: {e})"]

redacted = "\n".join(redacted_lines)
out = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            f"Direct read blocked for sensitive file: {fp}.\n\n"
            f"Redacted version follows (sensitive values masked where detected):\n\n{redacted}\n\n"
            f"Use an example/sample config file where possible, or extend the redaction hook for project-specific patterns."
        ),
    }
}
print(json.dumps(out))
