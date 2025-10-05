# core/base/browser_manager.py
from playwright.sync_api import sync_playwright, Error as PlaywrightError
from core.utils.config import Config

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        try:
            self.playwright = sync_playwright().start()
            headless = Config.is_headless()
            self.browser = self.playwright.chromium.launch(headless=headless)
        except PlaywrightError as e:
            self.stop_playwright()
            raise Exception(f"Failed with playwright error {e}")


    def new_page(self):
        """ Method to initialize a browser instance"""
        try:
            if not self.context and self.browser:
                self.context = self.browser.new_context()
            if not self.page and self.context:
                self.page = self.context.new_page()
            return self.page
        except PlaywrightError as e:
            return None

    def close(self):
        """ Method to close a browser instance"""
        try:
            if self.page:
                self.page.close()
            if self.context:
                self.context.close()
            if self.browser:
                self.browser.close()
        except PlaywrightError as e:
            raise Exception(f"Failed with playwright error {e}")
        finally:
            self.stop_playwright()

    def stop_playwright(self):
        """ Method to stop playwright from running """
        if self.playwright:
            try:
                self.playwright.stop()
            except Exception as e:
                raise Exception(f"Failed with playwright error {e}")

