#Write a Python script to check if a file exists.

#!/usr/bin/env python3

from pathlib import Path
import logging
import sys


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_file_exists(file_path: str) -> bool:
    """
    Check if a file exists and is a regular file.

    Args:
        file_path (str): Path to the file

    Returns:
        bool: True if file exists, False otherwise
    """
    try:
        path = Path(file_path)

        if path.exists() and path.is_file():
            logging.info("File exists: %s", path.resolve())
            return True

        logging.warning("File not found: %s", file_path)
        return False

    except PermissionError:
        logging.error("Permission denied while accessing: %s", file_path)

    except Exception as err:
        logging.exception("Unexpected error: %s", err)

    return False


def main():
    if len(sys.argv) != 2:
        logging.error("Usage: python check_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    exists = check_file_exists(file_path)


    sys.exit(0 if exists else 2)


if __name__ == "__main__":
    main()