import subprocess
import logging
import sys
from pathlib import Path

CPU_THRESHOLD= 80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=80

LOG_DIRECTORY= Path("logs")
LOG_FILE=LOG_DIRECTORY/"health.log"

LOG_DIRECTORY.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format= "%(asctime)s -%(levelname)s -%(message)s"
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
            " command Failed: %s",
            error
        )


def get_cpu_usage():

    output= run_command(
        [
            "bash",
            "-c",
            "top bn1 | grep 'Cpu(s)' "
        ]

    )

    if not output:
        return None

    try:
        
    

