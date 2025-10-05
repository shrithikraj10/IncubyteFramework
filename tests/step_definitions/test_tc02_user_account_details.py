import pytest
from pytest_bdd import scenarios, given, when, then
from core.base.browser_manager import BrowserManager
from core.utils.config import Config
from pages.login import LoginPage
from pages.account import AccountPage
from core.utils.data_handler import DataHandler

# Link feature file
scenarios("../features/test_tc02_user_account_details.feature")

test_data_path = 'test_data/test_user_onboarding.csv'

# A pytest fixture to consilidate and provide the objects needed to be used in subsequent step methods
@pytest.fixture
def manager():
    browser_manager = BrowserManager()
    page = browser_manager.new_page()
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    user_data = DataHandler.read_csv(test_data_path)[0]

    yield {"page": page, 
           "user_data": user_data,
           "account": account_page,
           "login_page": login_page}
    browser_manager.close()


@given("I navigate to the Para bank home page")
def navigate_to_home_page(manager):
    manager["page"].goto(Config.get_base_url())
    
@when("I am able to successfully login to my account")
def login_account(manager):
    user_data = manager["user_data"]
    manager["login_page"].login(user_data["username"], user_data["password"])

@then("I am able to view my account balance")
def validate_user_account_balance(manager):
    account = manager["account"]
    balance = account.get_balance()
    print("The Account balance is: " + balance)

  

