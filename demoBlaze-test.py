import pytest
import PomDemo.utilities.read_config as read_config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
def test_login(self):

    login_button = self.driver.find_element(By.ID,"login2")
    login_button.click()
    self.driver.implicitly_wait(3)

    user_name = self.driver.find_element(By.ID,"loginusername")
    passord = self.driver.find_element(By.ID,"loginpassword")

    user_name.send_keys(read_config.get_config("login","name"))
    passord.send_keys(read_config.get_config("login","pass"))

    self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
    time.sleep(5)

    user = self.driver.find_element(By.ID,"nameofuser")
    assert user.text.__eq__("Welcome "+read_config.get_config("login","name"))
