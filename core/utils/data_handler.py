import csv
import os
from typing import List, Dict


class DataHandler:
    @staticmethod
    def _resolve_path(file_path: str) -> str:
        """
        Resolves a file path relative to the project root, regardless of where tests are executed from.
        """
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # goes up from core/utils/
        abs_path = os.path.join(project_root, file_path)
        return abs_path

    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, str]]:
        """
        Reads a CSV file and returns a list of dictionaries.
        Each row becomes a dictionary with column headers as keys.
        """
        abs_path = DataHandler._resolve_path(file_path)

        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"CSV file not found: {abs_path}")

        with open(abs_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def write_csv(file_path: str, data: List[Dict[str, str]], fieldnames: List[str]):
        """
        Writes a list of dictionaries to a CSV file (overwrites existing content).
        """
        abs_path = DataHandler._resolve_path(file_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        with open(abs_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def append_csv(file_path: str, row: Dict[str, str], fieldnames: List[str]):
        """
        Appends a single row (dict) to an existing CSV file.
        If the file doesn't exist, it creates one with headers.
        """
        abs_path = DataHandler._resolve_path(file_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        try:
            with open(abs_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if file.tell() == 0:  # file is empty
                    writer.writeheader()
                writer.writerow(row)
        except FileNotFoundError:
            # Create file and write header + first row
            with open(abs_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(row)
