from pytest_bdd import scenarios, given, when, then
from core.base.browser_manager import BrowserManager
from core.utils.config import Config
from pages.signup import SignupPage
from pages.login import LoginPage
from pages.account import AccountPage

# Link feature file
scenarios("../features/test_signup.feature")

@given("I navigate to the Parabank registration page")
def navigate_to_registration():
    global browser_manager, page
    browser_manager = BrowserManager()
    page = browser_manager.new_page()
    page.goto(Config.get_base_url())
    page.click("a[href*='register.htm']")

@when("I create a new user account")
def create_account():
    global signup_page
    signup_page = SignupPage(page)
    user_data = {
        "first": "John",
        "last": "Doe",
        "address": "123 Main St",
        "city": "Goa",
        "state": "GA",
        "zip_code": "403001",
        "phone": "9999999999",
        "ssn": "123-45-6789",
        "username": Config.get_username(),
        "password": Config.get_password()
    }
    signup_page.create_account(user_data)

@when("I log in with that account")
def login_account():
    global login_page
    login_page = LoginPage(page)
    username = Config.get_username()
    password = Config.get_password()
    login_page.login(username, password)

@then("I should see my account balance displayed")
def verify_balance():
    account_page = AccountPage(page)
    balance = account_page.get_balance()
    print(f"💰 Account Balance: {balance}")
    assert balance is not None and balance.strip() != ""
    # Close browser
    browser_manager.close()
