import subprocess
import logging
import sys
from pathlib import Path


DISK_THRESHOLD= 80

LOG_DIRECTORY= Path("logs")
LOG_FILE= LOG_DIRECTORY/"disk_usage.log"

LOG_DIRECTORY.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format= "-%(asctime)s -%(levelname)s -%(message)s"
)

def run_command(command):

    try:
        result= subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        logging.error(
            "command failed: %s",
            error
        )

        return None


def get_disk_usage():

    output = run_command(
        [
            "df",
            "-P",
            "/"
        ]
    )

    
    




