from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# start a new Chrome browser session
driver = webdriver.Chrome()

# navigate to the form page
driver.get("http://127.0.0.1:8080/query")

time.sleep(2)
# locate the form elements
ids = driver.find_element(by=By.ID, value="ID")
submit_button = driver.find_element(by=By.ID, value="transubmit")

if not ids.is_enabled():
    print("Element is disabled")
time.sleep(2)

# fill out the form
ids.send_keys("12827, 12855, 12888")

# submit the form
submit_button.click()

# close the browser
driver.quit()