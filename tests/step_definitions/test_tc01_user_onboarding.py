import pytest
from pytest_bdd import scenarios, given, when, then
from core.base.browser_manager import BrowserManager
from core.utils.config import Config
from pages.signup import SignupPage
from pages.login import LoginPage
from pages.account import AccountPage
from core.utils.data_handler import DataHandler

# Link feature file
scenarios("../features/test_tc01_user_onboarding.feature")

test_data_path = 'test_data/test_user_onboarding.csv'

# A pytest fixture to consilidate and provide the objects needed to be used in subsequent step methods
@pytest.fixture
def manager():
    browser_manager = BrowserManager()
    page = browser_manager.new_page()
    signup_page = SignupPage(page)
    login_page = LoginPage(page)

    user_data = DataHandler.read_csv(test_data_path)[0]

    yield {"page": page, 
           "signup_page": signup_page, 
           "user_data": user_data,
           "login_page": login_page}
    browser_manager.close()


@given("I navigate to the Para bank home page")
def navigate_to_home_page(manager):
    manager["page"].goto(Config.get_base_url())
    
@then("I am able to successfully register a new user account")
def create_account(manager):
    user_data = manager["user_data"]
    user_data["username"] = DataHandler.randomize_test_string()
    user_data["password"] = DataHandler.randomize_test_string()
    DataHandler.append_csv(test_data_path, user_data, user_data.keys())
    manager["signup_page"].create_account(user_data)

@then("I am able to successfully login to the new user account")
def login_account(manager):
    user_data = manager["user_data"]
    manager["login_page"].login(user_data["username"], user_data["password"])
