# pages/account_page.py
from core.base.base_ui import UIBase

class AccountPage(UIBase):
    # Locator
    BALANCE_AMOUNT = "//*[@id='accountTable']/tbody/tr[2]/td[2]/b"

    def get_balance(self) -> str:
        """ Fetch the user account balance"""
        return self.get_text(self.BALANCE_AMOUNT)
