from Actions.baseActions import BaseActions
from pages.loginPage import LoginPage
class LoginActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):

        self.click(LoginPage.loginButton)

        self.enter_text(LoginPage.userName,username)

        self.enter_text(LoginPage.password,password)

        self.click(LoginPage.submitButton)

    def get_userName(self):
        return self.get_text(LoginPage.userNameVie)