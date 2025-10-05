from playwright.sync_api import Page, TimeoutError, expect

class UIBase:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        try:
            self.page.click(locator)
            print(f"Clicked: {locator}")
        except TimeoutError:
            raise Exception(f"Failed to click element: {locator}")

    def type(self, locator: str, text: str):
        try:
            self.page.fill(locator, text)
            print(f"Typed '{text}' into: {locator}")
        except TimeoutError:
            raise Exception(f"Failed to type into: {locator}")

    def get_text(self, locator: str):
        try:
            text = self.page.inner_text(locator)
            print(f"Text from {locator}: {text}")
            return text
        except TimeoutError:
            raise Exception(f"Failed to get text from: {locator}")

    def wait_for_element(self, locator: str, timeout: int = 5000):
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
        except TimeoutError:
            raise Exception(f"Element not found: {locator}")

    def navigate_to(self, url: str):
        try:
            self.page.goto(url)
            print(f"Navigated to: {url}")
        except Exception as e:
            raise Exception(f"Failed to navigate to page: {url} with Error: {e}")
    
    def expect_text(self, locator: str, expected_text: str):
        """
        Assert that an element contains the expected text.
        """
        try:
            element = self.page.locator(locator)
            expect(element).to_contain_text(expected_text)
            print(f"[Assertion Passed] '{locator}' contains text: '{expected_text}'")
        except Exception as e:
            raise Exception(f"[Assertion Failed] '{locator}' does not contain text '{expected_text}'. Error: {e}")
