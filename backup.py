#!/usr/bin/env python3

import os
import shutil
import datetime
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_backup(source_dir: str, backup_dir: str) -> None:
    """Creates a backup of the source directory.

    Args:
        source_dir: The directory to backup.
        backup_dir: The directory to store the backup.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        OSError: If there is an error during the backup process.
    """
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

        # Create backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)

        # Generate backup filename with timestamp
        now = datetime.datetime.now()
        backup_filename = f"backup_{now.strftime('%Y%m%d_%H%M%S')}.zip"
        backup_filepath = os.path.join(backup_dir, backup_filename)

        # Create the zip archive
        logging.info(f"Creating backup of '{source_dir}' to '{backup_filepath}'...")
        shutil.make_archive(os.path.splitext(backup_filepath)[0], 'zip', source_dir)

        logging.info(f"Backup created successfully at '{backup_filepath}'")

    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
        raise
    except OSError as e:
        logging.error(f"Error during backup: {e}")
        raise


def main():
    """Main function to parse arguments and initiate the backup process."""
    parser = argparse.ArgumentParser(description='Backup a directory.')
    parser.add_argument('source', type=str, help='Source directory to backup')
    parser.add_argument('destination', type=str, help='Destination directory for backups')

    args = parser.parse_args()

    try:
        create_backup(args.source, args.destination)
    except (FileNotFoundError, OSError) as e:
        print(f"Backup failed: {e}")
        exit(1)


if __name__ == "__main__":
    main()
