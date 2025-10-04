# pages/login.py
from core.base.base_ui import UIBase

class LoginPage(UIBase):
    # Locators
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "input[value='Log In']"

    def login(self, username: str, password: str):
        """
        Logs in a user with provided credentials.

        Args:
            username (str): Username of the account
            password (str): Password of the account
        """
        self.wait_for_element(self.USERNAME_INPUT)
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
