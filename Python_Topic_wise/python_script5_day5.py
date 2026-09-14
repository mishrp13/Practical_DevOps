import os
import shutil
import logging
from datetime import datetime

SOURCE = "/data/application"
BACKUP_DIR = "/backup"

# Create backup directory if it doesn't exist
os.makedirs(BACKUP_DIR, exist_ok=True)

# Log file
logging.basicConfig(
    filename="/backup/backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_name = f"application_backup_{timestamp}"
        backup_path = os.path.join(BACKUP_DIR, backup_name)

        # Copy entire source directory
        shutil.copytree(SOURCE, backup_path)

        logging.info(f"Backup successful: {backup_path}")
        print(f"Backup completed: {backup_path}")

    except Exception as e:
        logging.error(f"Backup failed: {e}")
        print(f"Backup failed: {e}")


if __name__ == "__main__":
    create_backup()