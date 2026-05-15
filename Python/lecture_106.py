import json
import logging.config

print("Declarative configuration using json configuration")
print("..........\n")

config_path= "declarative-config.json"

with open(config_path, "r") as config_file:
    json_config= json.load(config_path)


logging.config.dictConfig(json_config)
config_logger= logging.getLogger("config.json")
logging.info("Json config setup successfully")
logging.debug("ops console")


