import subprocess
import logging
import sys
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "health.log"


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

LOG_DIRECTORY.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# RUN LINUX COMMAND
# ============================================================

def run_command(command):
    """
    Execute a Linux command and return its output.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as error:

        logging.error(
            "Command failed: %s",
            error
        )

        return None


# ============================================================
# CPU CHECK
# ============================================================

def get_cpu_usage():
    """
    Get CPU utilization percentage.
    """

    output = run_command(
        [
            "bash",
            "-c",
            "top -bn1 | grep 'Cpu(s)'"
        ]
    )

    if not output:
        return None

    try:

        idle = float(
            output.split("id,")[0].split()[-1]
        )

        cpu_usage = 100 - idle

        return round(cpu_usage, 2)

    except (ValueError, IndexError):

        logging.error(
            "Unable to parse CPU information"
        )

        return None


# ============================================================
# MEMORY CHECK
# ============================================================

def get_memory_usage():
    """
    Get memory utilization percentage.
    """

    output = run_command(
        ["free", "-m"]
    )

    if not output:
        return None

    try:

        lines = output.splitlines()

        memory_line = lines[1].split()

        total_memory = int(memory_line[1])
        used_memory = int(memory_line[2])

        memory_usage = (
            used_memory / total_memory
        ) * 100

        return round(memory_usage, 2)

    except (
        ValueError,
        IndexError,
        ZeroDivisionError
    ):

        logging.error(
            "Unable to parse memory information"
        )

        return None


# ============================================================
# DISK CHECK
# ============================================================

def get_disk_usage():
    """
    Get root filesystem utilization percentage.
    """

    output = run_command(
        ["df", "-P", "/"]
    )

    if not output:
        return None

    try:

        lines = output.splitlines()

        disk_line = lines[1].split()

        usage = disk_line[4]

        usage = usage.replace("%", "")

        return int(usage)

    except (
        ValueError,
        IndexError
    ):

        logging.error(
            "Unable to parse disk information"
        )

        return None


# ============================================================
# UPTIME CHECK
# ============================================================

def get_uptime():
    """
    Get server uptime.
    """

    output = run_command(
        ["uptime", "-p"]
    )

    return output


# ============================================================
# HEALTH CHECK
# ============================================================

def check_health(cpu, memory, disk):
    """
    Determine overall server health.
    """

    if cpu is None:
        return "UNKNOWN"

    if memory is None:
        return "UNKNOWN"

    if disk is None:
        return "UNKNOWN"

    if cpu > CPU_THRESHOLD:
        return "UNHEALTHY"

    if memory > MEMORY_THRESHOLD:
        return "UNHEALTHY"

    if disk > DISK_THRESHOLD:
        return "UNHEALTHY"

    return "HEALTHY"


# ============================================================
# DISPLAY RESULTS
# ============================================================

def display_results(cpu, memory, disk, uptime, status):

    print()
    print("=" * 50)
    print("             SERVER HEALTH CHECK")
    print("=" * 50)

    print(f"CPU Usage       : {cpu}%")
    print(f"Memory Usage    : {memory}%")
    print(f"Disk Usage      : {disk}%")
    print(f"Server Uptime   : {uptime}")

    print("-" * 50)

    print(f"Server Status   : {status}")

    print("=" * 50)
    print()


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    logging.info(
        "Starting server health check"
    )

    cpu = get_cpu_usage()

    memory = get_memory_usage()

    disk = get_disk_usage()

    uptime = get_uptime()

    status = check_health(
        cpu,
        memory,
        disk
    )

    display_results(
        cpu,
        memory,
        disk,
        uptime,
        status
    )

    # --------------------------------------------------------
    # EXIT CODES
    # --------------------------------------------------------

    if status == "UNHEALTHY":

        logging.warning(
            "Server health status: UNHEALTHY"
        )

        sys.exit(1)

    if status == "UNKNOWN":

        logging.error(
            "Server health status: UNKNOWN"
        )

        sys.exit(2)

    logging.info(
        "Server health status: HEALTHY"
    )

    sys.exit(0)


# ============================================================
# PYTHON ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()