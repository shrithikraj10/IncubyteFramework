import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    @staticmethod
    def get_base_url() -> str:
        """ Method used to fetch base URL from .env file """

        url = os.getenv("BASE_URL")
        if not url:
            raise ValueError("BASE_URL not set in environment variables")
        return url

    @staticmethod
    def get_username() -> str:
        """ Method used to fetch username from .env file """

        username = os.getenv("USERNAME")
        if not username:
            raise ValueError("USERNAME not set in environment variables")
        return username

    @staticmethod
    def get_password() -> str:
        """ Method used to fetch password from .env file """

        password = os.getenv("PASSWORD")
        if not password:
            raise ValueError("PASSWORD not set in environment variables")
        return password

    @staticmethod
    def is_headless() -> bool:
        try:
            headless_value = os.getenv("HEADLESS", "true").lower()
            return headless_value in ["true", "1", "yes"]
        except Exception as e:
            print(f"Error reading HEADLESS variable: {e}")
            return True  # default to headless if error occurs
