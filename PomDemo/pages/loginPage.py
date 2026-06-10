from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):

    loginButton = (By.ID, "login2")
    userName = (By.ID, "loginusername")
    password = (By.ID, "loginpassword")
    submitButton = (By.XPATH, "//button[text()='Log in']")
    userNameVie = (By.ID, "nameofuser")