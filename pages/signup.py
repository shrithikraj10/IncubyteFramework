# pages/signup.py
from core.base.base_ui import UIBase

class SignupPage(UIBase):
    FIRST_NAME = "#customer\\.firstName"
    LAST_NAME = "#customer\\.lastName"
    ADDRESS = "#customer\\.address\\.street"
    CITY = "#customer\\.address\\.city"
    STATE = "#customer\\.address\\.state"
    ZIP = "#customer\\.address\\.zipCode"
    PHONE = "#customer\\.phoneNumber"
    SSN = "#customer\\.ssn"
    USERNAME = "#customer\\.username"
    PASSWORD = "#customer\\.password"
    REPEAT_PASSWORD = "#repeatedPassword"
    REGISTER_BUTTON = "input[value='Register']"
    SIGNUP_BUTTON = "a[href*='register.htm']"

    def create_account(self, user_data: dict):
        self.click(self.SIGNUP_BUTTON)
        self.type(self.FIRST_NAME, user_data["first"])
        self.type(self.LAST_NAME, user_data["last"])
        self.type(self.ADDRESS, user_data["address"])
        self.type(self.CITY, user_data["city"])
        self.type(self.STATE, user_data["state"])
        self.type(self.ZIP, user_data["zip_code"])
        self.type(self.PHONE, user_data["phone"])
        self.type(self.SSN, user_data["ssn"])
        self.type(self.USERNAME, user_data["username"])
        self.type(self.PASSWORD, user_data["password"])
        self.type(self.REPEAT_PASSWORD, user_data["password"])
        self.click(self.REGISTER_BUTTON)
