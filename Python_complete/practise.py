import subprocess
import logging
import sys
from pathlib import Path


CPU_THRESHOLD= 80
MEMORY_THRESHOLD= 80
DISK_THRESHOLD= 80

LOG_DIRECTORY= Path("logs")
LOG_FILE= LOG_DIRECTORY/"health.log"

LOG_DIRECTORY.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.info,
    format= "%(asctime)s -%(levelname)s -%(message)s"
)

def run_command(command):

    try:
        result= subprocess.run(
            command,
            capture_output=True,
            text= True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        logging.error(
            "command: %s",
            error
        )

        return None


def get_cpu_usage():

    output= run_command(
        [
            "bash",
            "-c",
            "top -bn1 | grep 'Cpu(s)'"
        ]
    )

    if not output:
        return None

    try:

        idle= float(
            output.split("id,")[0].split()[-1]
        )

        cpu_usage= 100- idle
        return round(cpu_usage,2)

    except (ValueError,IndexError):
        logging.error(
            "unable to parse cpu information"
        )

        return None


def get_memory_usage():

    output= run_command(
        ["free","-m"]
    )

    if not output:
        return None


    try:

        lines= output.splitlines()

        memory_lines= lines[1].split

        total_memory= int(memory_lines[1])
        used_memory= int(memory_lines[2])

        total_usage= (used_memory/total_memory)*100

        return round(total_usage,2)

    except ( ValueError,IndexError,ZeroDivisionError):

        logging.error(
            "Unable to parse memory information"
        )

        return None


def get_disk_usage():

    output= run_command(
        ["df", "-P", "/"]
    )

    if not output:
        return None


    try:

        lines= output.splitlines()

        disk_line= lines[1].split()

        usage= disk_line[4]

        usage= usage.replace("%","")

        return int(usage)

    except (ValueError,IndexError):
        logging.error("unable to parse usage information")

        return None


def get_uptime():

    output= run_command(
        ["uptime","-P"]
    )

    return output


def check_health(cpu,memory,disk):

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



def display_result(cpu,memory,disk,uptime,status):

    print()
    print("=" * 50)
    print(" server Health check")
    print("=" *50)


    print(f" cpu_usage  : {cpu}%")
    print(f"Memory usage: {memory}%")
    print(f"Disk usage: {disk}%")
    print(f"Server uptime: {uptime}")

    print("-" * 50)
    print(f"server status: {status}")
    print("="*50)
    print()


def main():

    logging.info(
        "starting server health check"
    )

    cpu=get_cpu_usage()
    memory= get_memory_usage()
    disk= get_disk_usage()

    uptime= get_uptime()

    status= check_health(
        cpu,memory,disk
    )

    display_result(
        cpu,
        memory,
        disk,
        uptime,
        status
    )


    if status == "UNHEALTHY":

        logging.warning(
            "server health status: unhealthy"
        )

        sys.exit(1)

    if status == "UNKNOWN":
        logging.error(
            "server health status unknown"
        )

        sys.exit(2)

    logging.info(
        "server health status: Healthy"
    )

    sys.exit(0)



if __name__=="__main__":
    main()

