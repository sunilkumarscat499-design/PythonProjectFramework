
from playwright.sync_api import Page

class Login:
    def __init__(self,page:Page):
        self.page = page
        self.login_link = self.page.locator("#login2")

    def click_on_login_link(self):
        self.login_link.click()

