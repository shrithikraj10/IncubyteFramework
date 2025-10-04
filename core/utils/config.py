import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    @staticmethod
    def get_base_url():
        return os.getenv("BASE_URL")

    @staticmethod
    def get_username():
        return os.getenv("USERNAME")

    @staticmethod
    def get_password():
        return os.getenv("PASSWORD")

    @staticmethod
    def is_headless() -> bool:
        headless_value = os.getenv("HEADLESS", "true").lower()
        return headless_value in ["true", "1", "yes"]
