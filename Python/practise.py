import logging
import os
import logging.handlers
import time

def cleanup_log_files(base_name: str):
    for file_name in os.listdir("."):
        if file_name.startswith(base_name):
            os.remove(base_name)


rotating_logs_filename= "roatatingfile.log"

cleanup_log_files(rotating_logs_filename)

rotating_logger= logging.getLogger("file.rotating")
rotating_logger.setLevel(logging.DEBUG)

rotaing_fh= logging.handlers.RotatingFileHandler(
    rotating_logs_filename,
    maxBytes=500,
    backupCount=3,
    encoding="utf-8"
)

rotaing_fh.setFormatter(
    logging.Formatter("%(levelname)s - %(message)s")
)

rotating_logger.addHandler(rotaing_fh)


for i in range(30):
    rotating_logger.info(f"Entry: {i}: {'z'*50}")
    time.sleep(0.05)
    



