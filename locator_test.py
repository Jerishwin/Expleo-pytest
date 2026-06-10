from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")

first_name = driver.find_element(By.XPATH,'//label[text()="First Name "]/following-sibling::input[@name="name"]')

last_name = driver.find_element(locate_with(By.TAG_NAME, "input").below(first_name))

first_name.send_keys("Jerishwin")
last_name.send_keys("Joseph")

password = driver.find_element(By.XPATH,'//div/input[@type="password"]')

email = driver.find_element(locate_with(By.TAG_NAME, "input").above(password))

re_password = driver.find_element(locate_with(By.TAG_NAME, "input").below(password))

email.send_keys("jerish")
password.send_keys("12345678")
re_password.send_keys("12345678")

clear_button = driver.find_elements(By.XPATH,'//button[@type="reset"]')[0]

reset_button = driver.find_elements(By.XPATH,'//button[@type="reset"]')[1]

register_button = driver.find_element(locate_with(By.TAG_NAME, "button").near(clear_button))

register_button.click()

driver.quit()