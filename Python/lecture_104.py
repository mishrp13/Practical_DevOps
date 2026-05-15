import logging.config
import json

# Declarative logging configuration -INI-files

print("Declarative config with INI files")
print(".........\n")

config_path="declarative-config.ini"
logging.config.fileConfig(
    fname=config_path,
)

app_logger= logging.getLogger("app")
app_logger.debug("INI-style fileconfig is working")
