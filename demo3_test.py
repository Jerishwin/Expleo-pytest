import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
def test_search(search_term):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("www.google.com")
    search = driver.find_element(By.ID,"APjFqb")
    search.send_keys(search_term)
    driver.close()