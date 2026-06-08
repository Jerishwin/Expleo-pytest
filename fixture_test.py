import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_validproduct(test_setup_teardown):
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    time.sleep(5)
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

def test_invalidproduct(test_setup_teardown):
    driver.find_element(By.NAME,"search").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    expexted_text = "There is no product that matches the search criteria."
    time.sleep(5)
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted_text)

def test_noproduct(test_setup_teardown):
    driver.find_element(By.NAME,"search").send_keys("")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    time.sleep(5)
    expexted_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expexted_text)