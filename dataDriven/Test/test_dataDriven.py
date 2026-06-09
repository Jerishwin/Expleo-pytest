import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader

@pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles/data.xlsx","Sheet1"))
class TestLogin:
    def test_log(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")

        login_button = self.driver.find_element(By.ID,"login2")
        login_button.click()
        self.driver.implicitly_wait(3)

        user_name = self.driver.find_element(By.ID,"loginusername")
        passord = self.driver.find_element(By.ID,"loginpassword")

        user_name.send_keys(username)
        passord.send_keys(password)

        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        time.sleep(5)

        user = self.driver.find_element(By.ID,"nameofuser")
        assert user.text.__eq__("Welcome "+username)

        self.driver.quit()

