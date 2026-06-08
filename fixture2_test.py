import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_teardown")
class TestSearch:
    def test_validproduct(self):
        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
        time.sleep(5)
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_invalidproduct(self):
        self.driver.find_element(By.NAME,"search").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
        expexted_text = "There is no product that matches the search criteria."
        time.sleep(5)
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted_text)

    def test_noproduct(self):
        self.driver.find_element(By.NAME,"search").send_keys("")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
        time.sleep(5)
        expexted_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted_text)

