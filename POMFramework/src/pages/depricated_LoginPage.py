


from playwright.sync_api import Page


## you always intiate elements inside constructor
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.login = page.locator("#login2")
        self.userName = page.locator("#loginusername")
        self.password = page.locator("#loginpassword")
        self.login_button = page.get_by_role("button",name="Log in")

    ##Action methods

    def click_login_link(self):
        self.login.click()
    def enter_username(self,username):
        self.userName.clear()
        self.userName.fill(username)
    def enter_password(self,password):
        self.password.clear()
        self.password.fill(password)
    def click_on_login_button(self):
        self.login_button.click()
