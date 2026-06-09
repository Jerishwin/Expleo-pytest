import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles/data.xlsx","Sheet1"))
class TestLogin:
    logger = logCreator.log_generator()
    def test_log(self,username,password):
        self.logger.info("Test started")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")
        self.logger.info("Site Launched")

        login_button = self.driver.find_element(By.ID,"login2")
        login_button.click()
        self.logger.info("Login Button Clicked")
        self.driver.implicitly_wait(3)

        user_name = self.driver.find_element(By.ID,"loginusername")
        passord = self.driver.find_element(By.ID,"loginpassword")

        user_name.send_keys(username)
        self.logger.info("Username filled")
        passord.send_keys(password)
        self.logger.info("Passord Filled")

        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        self.logger.info("Submit button clicked")
        time.sleep(5)

        user = self.driver.find_element(By.ID,"nameofuser")
        self.logger.info("Asserted in Dashboard")

        self.driver.quit()

