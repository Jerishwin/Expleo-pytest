import pytest
import read_config
from selenium import webdriver

@pytest.fixture(params=[read_config.get_config("browser","name")])
def setup_teardown(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(read_config.get_config("url","name"))
    request.cls.driver=driver
    yield
    driver.quit()