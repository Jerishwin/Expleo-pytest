import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
def test_search(search_term):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.google.com")
    search = driver.find_element(By.ID,"APjFqb")
    search.send_keys(search_term)
    driver.close()