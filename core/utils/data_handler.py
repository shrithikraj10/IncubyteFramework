import csv
import os
from typing import List, Dict
import random


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
        Creates the file with headers if it doesn't exist.
        Handles newline and concurrency issues cleanly.
        """
        abs_path = DataHandler._resolve_path(file_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        try:
            # Always use newline='' to prevent merged lines
            with open(abs_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Write header only if file is empty
                if os.stat(abs_path).st_size == 0:
                    writer.writeheader()
                
                # Ensure all values are strings (avoids encoding edge cases)
                safe_row = {k: str(v) for k, v in row.items()}
                writer.writerow(safe_row)

        except Exception as e:
            print(f"Error writing to CSV file {file_path}: {e}")
            raise
        
    @staticmethod
    def randomize_test_string(max_digits: int = 6) -> str:
        """
        Generate a random string starting with 'test' followed by random digits.
        
        Args:
            max_digits (int): Maximum number of digits to append (default: 6)
        
        Returns:
            str: Random string like 'test123456'
        """
        number = random.randint(0, 10**max_digits - 1)
        return f"test{number}"


