# pages/account_page.py
from core.base.base_ui import UIBase

class AccountPage(UIBase):
    # Locator
    BALANCE_TEXT = "xpath=//b[contains(text(),'Balance')]/following-sibling::span"

    def get_balance(self) -> str:
        """ Fetch the user account balance"""
        return self.get_text(self.BALANCE_TEXT)
