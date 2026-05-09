print("configuring python-json-logger")
print("------\n")

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
    rename_fields={"asctime":"timestamp", "levelname":"level"},
)

handler.setFormatter(json_formatter)

json_logger.addHandler(handler)

json_logger.info("structed logging Initialized")