
from playwright.sync_api import Page

class LoginLandingPage:
    def __init__(self,page:Page):
        self.page = page
        self.username = self.page.locator("#loginusername")
        self.password = self.page.locator("#loginpassword")
        self.login_button_full = self.page.locator(".modal-footer button[onclick = 'logIn()']")

    def enter_username(self,name):
        self.username.clear()
        self.username.fill(name)

    def enter_password(self,password):
        self.password.clear()
        self.password.fill(password)

    def login(self):
        self.login_button_full.click()

    def perform_login(self,username,password):
        self.username.clear()
        self.username.fill(username)
        self.password.clear()
        self.password.fill(password)
        self.login_button_full.click()