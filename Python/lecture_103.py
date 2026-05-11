print("configuring python-json_logger")
print("------------------\n")

import logging
import sys
from pythonjsonlogger.json import JsonFormatter

json_logger= logging.getLogger("demo.json")
json_logger.setLevel(logging.INFO)


handler= logging.StreamHandler(sys.stdout)

json_formatter= JsonFormatter(
    "{asctime}{levelname}{message}",
    style="{",
    json_indent=4,
    rename_fields={"asctime": "timestamps","levelname":"level"}
)

handler.setFormatter(json_formatter)

json_logger.addHandler(handler)

json_logger.info("structured Logging")

# printing logging with extra content

print("Logging with extra content")
print(".....................\n")

extra_content= {
    "user_id":"devops1",
    "request_id":"request-12345abc",
    "source_ip":"10.0.0.5"
}

json_logger.warning(
    "Request took longer than 5 second",
    extra=extra_content
)

print("Logging exception as json")
print("...............\n")

try:
    result = 1/0
except ZeroDivisionError:
    json_logger.exception(
        "unexpected calcultaion Error",
        extra={"operation": "division"}
    )

