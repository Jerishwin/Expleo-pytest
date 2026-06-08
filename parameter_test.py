import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("input_broser",['chrome','firefox'])
@pytest.mark.parametrize("input_url",['https://www.flipkart.com/','https://www.amazon.in/'])
def test_url(input_broser,input_url):

    if input_broser=="chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver=webdriver.Chrome(options)
    if input_broser=="firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver=webdriver.Firefox(options)
    
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    time.sleep(5)
    driver.close()