import logging.config
import json
from typing import Any, Dict

print("Dynamically building config")
print(".......................\n")

base_config: Dict[str, Any] = {
    "version": 1,
    "disable_existing_logger": True,
    "handlers": {},
    "formatter": {},
    "loggers": {},
}

base_config["formatter"]["simple"]= {
    "format": "%(levelname)s -%(message)s"
}

base_config["handlers"]["console"] = {
    "class": "logging.StreamHandler",
    "level": "DEBUG",
    "formatters": "simple",
    "stream": "ext://sys.stdout",
}

base_config["loggers"]["config.dynamic"]= {
    "level": "WARNING",
    "handlers": ["console"],
}

def is_debug():
    return True

if is_debug():
    for logger, _config in base_config["loggers"].items():
        base_config["loggers"][logger]["level"]= "DEBUG"


logging.config.dictConfig(base_config)
config_logger= logging.getLogger("config.dynamic")
config_logger.debug("new")
config_logger.info("newest")