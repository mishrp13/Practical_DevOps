import os
import platform
import socket
import subprocess
import sys


def run_command(command):

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=0
        )

        if result.returncode !=0:
            return f"command Failed: {result.stderr.strip}"

        return result.stdout.strip()

    except  subprocess.TimeoutExpired:
        return "Command Timed output"

    except Exception as e:
        return f"ERROR: {e}"


def get_hostname():
    return socket.gethostname()

def get_os_information():
    return platform.system()

def get_os_version():
    return platform.release()

def get_architecture():
    return platform.machine()

def get_cpu_count():
    return os.cpu_count()


def get_memory():
    return run_command("free -h | awk '/Mem:/ {print $2}")

def get_disk_usage():
    return run_command("df -h / awk 'NR==2 {print $5}'")

def get_ip_address():
    return run_command("hostname -I | awk '{print $1}'")

def get_uptime():
    return run_command("uptime -p")

def get_python_version():
    return sys.version.split()[0]


def display_report():
    print("=" * 50)
    print("    SYSTEM INFORMATION REPORT")
    print("=" * 50)

    print(f" Hostname : {get_hostname()}")
    print(f" Operating System: {get_os_information()}")
    print(f" kernel version : {get_os_version()}")
    print(f"Architecture: {get_architecture()}")
    print(f"CPU cores : {get_cpu_count()}")
    print(f"Memory : {get_memory()}")
    print(f"Disk Usage: {get_disk_usage()}")
    print(f"Ip Address: {get_ip_address()}")
    print(f"Python version: {get_python_version()}")
    print(f" Uptime : {get_uptime()}")

    print("=" * 50)


if __name__=="__main__":
    display_report()

    




    