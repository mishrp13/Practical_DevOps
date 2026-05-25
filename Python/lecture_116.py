import re

def has_critical_error(log_line: str) -> bool:

    pattern = re.compile(r'(ERROR|FAIL):', re.IGNORECASE)

    match= pattern.search(log_line)

    return bool(match)


