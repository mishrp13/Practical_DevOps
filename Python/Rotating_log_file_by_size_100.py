import logging
import os
import logging.handlers

print("Size-based log rotation with File Handler")

rotating_logs_filename= "rotatingfile.log"

for file_name in os.listdir("."):
    if file_name.startswith(rotating_logs_filename):
        os.remove(file_name)

rotating_logger= logging.getLogger("file.rotating")
rotating_logger.setLevel(logging.DEBUG)

rotating_fh = logging.handlers.RotatingFileHandler(
    rotating_logs_filename,
    maxBytes=500,
    backupCount=2,
    encoding="utf-8"
)

rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

rotating_logger.addHandler(rotating_fh)

for i in range(30):
    rotating_logger.info(f"Entry: {i}: {'z'*50}")
