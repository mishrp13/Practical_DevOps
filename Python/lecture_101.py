import logging
import os
import logging.handlers

def cleanup_log_files(base_name: str):
    for file_name in os.listdir("."):
        if file_name.startswith(base_name):
            os.remove(file_name)


timed_rotating_log_files= "timedrotatingfile.log"

cleanup_log_files(timed_rotating_log_files)

timed_rotating_logger= logging.getLogger("file.timed")
timed_rotating_logger.setLevel(logging.DEBUG)

timed_rotating_fh= logging.handlers.TimedRotatingFileHandler(
    timed_rotating_log_files,
    when="s",
    interval=3,
    backupCount=2,
    encoding="utf-8"
)

timed_rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

timed_rotating_logger.addHandler(timed_rotating_fh)

for i in range(30):
    timed_rotating_logger.info(f"Entry {i}: {'z' *50}")
    





