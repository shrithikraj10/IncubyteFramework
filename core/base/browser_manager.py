# core/base/browser_manager.py
from playwright.sync_api import sync_playwright
from core.utils.config import Config

class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()
        headless = Config.is_headless()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = None
        self.page = None

    def new_page(self):
        # Create context only once per BrowserManager instance
        if not self.context:
            self.context = self.browser.new_context()
        if not self.page:
            self.page = self.context.new_page()
        return self.page

    def close(self):
        # Close page and context safely
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        self.browser.close()
        self.playwright.stop()
