import subprocess
import logging
import sys
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

DISK_THRESHOLD = 80

LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "disk_usage.log"


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
# DISK USAGE CHECK
# ============================================================

def get_disk_usage():
    """
    Get root filesystem disk utilization percentage.
    """

    output = run_command(
        [
            "df",
            "-P",
            "/"
        ]
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
            "Unable to parse disk usage information"
        )

        return None


# ============================================================
# DISK SPACE INFORMATION
# ============================================================

def get_disk_space():
    """
    Get total, used and available disk space.
    """

    output = run_command(
        [
            "df",
            "-h",
            "/"
        ]
    )

    if not output:
        return None

    try:
        lines = output.splitlines()

        disk_line = lines[1].split()

        total = disk_line[1]
        used = disk_line[2]
        available = disk_line[3]

        return {
            "total": total,
            "used": used,
            "available": available
        }

    except IndexError:
        logging.error(
            "Unable to parse disk space information"
        )

        return None


# ============================================================
# DISK HEALTH CHECK
# ============================================================

def check_disk_health(disk):
    """
    Determine disk health based on configured threshold.
    """

    if disk is None:
        return "UNKNOWN"

    if disk > DISK_THRESHOLD:
        return "UNHEALTHY"

    return "HEALTHY"


# ============================================================
# DISPLAY RESULTS
# ============================================================

def display_results(
    disk,
    space,
    status
):
    print()

    print("=" * 50)
    print("             DISK USAGE MONITOR")
    print("=" * 50)

    print(f"Disk Usage      : {disk}%")

    if space:
        print(f"Total Space     : {space['total']}")
        print(f"Used Space      : {space['used']}")
        print(f"Available Space : {space['available']}")

    print("-" * 50)

    print(f"Threshold       : {DISK_THRESHOLD}%")
    print(f"Disk Status     : {status}")

    print("=" * 50)

    print()


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    logging.info(
        "Starting disk usage monitor"
    )

    # --------------------------------------------------------
    # GET DISK USAGE
    # --------------------------------------------------------

    disk = get_disk_usage()

    # --------------------------------------------------------
    # GET DISK SPACE
    # --------------------------------------------------------

    space = get_disk_space()

    # --------------------------------------------------------
    # CHECK DISK HEALTH
    # --------------------------------------------------------

    status = check_disk_health(disk)

    # --------------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------------

    display_results(
        disk,
        space,
        status
    )

    # --------------------------------------------------------
    # LOG RESULTS
    # --------------------------------------------------------

    if status == "UNHEALTHY":

        logging.warning(
            "Disk usage is above threshold: %s%%",
            disk
        )

    elif status == "UNKNOWN":

        logging.error(
            "Unable to determine disk usage"
        )

    else:

        logging.info(
            "Disk usage is healthy: %s%%",
            disk
        )

    # --------------------------------------------------------
    # EXIT CODES
    # --------------------------------------------------------

    if status == "UNHEALTHY":
        sys.exit(1)

    if status == "UNKNOWN":
        sys.exit(2)

    sys.exit(0)


# ============================================================
# PYTHON ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()