from typing import Any,Dict
import logging.config


print("Declarative configuration using dectionary config")
print("..................\n")

dict_config: Dict[str ,Any ] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s-8s  - %(message)s"}
    },

    "handlers":{
        "console":{
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }

    },
    "loggers": {
        "config.dict": {
            "level": "DEBUG",
            "handlers": ["console"] 
        }
    }
}

logging.config.dictConfig(dict_config)
config_logger= logging.getLogger("config.dict")
config_logger.debug("dictConfig Steup Successfully")
config_logger.info("config goes to console")



