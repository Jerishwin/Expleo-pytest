import pytest
from selenium import webdriver
from Utilities.config_reader import get_value


@pytest.fixture()
def setup(request):

    browser = get_value("config.ini","common info", "browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(get_value("config.ini","common info", "url"))
    request.cls.driver = driver
    yield driver

    driver.quit()