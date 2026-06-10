import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.excel_reader import get_data
from Utilities.logger import get_logger

@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("email,password",get_data("login_data.xlsx", "ValidLoginData"))
    def test_valid_login(self, email, password):
        logger = get_logger()
        wait = WebDriverWait(self.driver, 30)
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class = \"fa fa-user\"]"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        logger.info(f"Entering Email : {email}")
        wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        wait.until(EC.url_contains("account"))
        assert "account" in self.driver.current_url.lower()
        logger.info("Login Successful")


    @pytest.mark.parametrize("email,password,message",get_data("login_data.xlsx", "InvalidLoginData"))
    def test_invalid_login(self, email, password, message):
        logger = get_logger()
        wait = WebDriverWait(self.driver, 30)
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class = \"fa fa-user\"]"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        logger.info(f"Entering Email : {email}")
        wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert message == wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class ,\"alert\")]"))).text
        logger.info("Error message shown Successful")
