import re
from typing import Optional

def parse_login_event(log_line: str) -> Optional[dict[str,str]]:

    if not isinstance(log_line,str):
        raise TypeError("Input log_line must be a string")
    
    pattern = re.compile(
        r"LOGIN_EVENT: User '(?P<username>\w+)' login attempt was (?P<status>\w+)\."
    )

    match= pattern.search(log_line)

    if match:
        return match.groupdict()
    
    return None


