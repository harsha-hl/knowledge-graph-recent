import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# start a new Chrome browser session
driver = webdriver.Chrome()

# navigate to the form page
driver.get("http://127.0.0.1:8080/query")

driver.maximize_window()
# locate the form elements
button = driver.find_element(by=By.ID, value="tranbutton")

if not button.is_enabled():
    print("Element is disabled")

button.click()
wait = WebDriverWait(driver, 5)
div = wait.until(EC.visibility_of_element_located((By.ID, "transSpec")))
print('Visible')

# locate the form elements
ids = driver.find_element(by=By.ID, value="ID")
submit_button = driver.find_element(by=By.ID, value="transubmit")

if not ids.is_enabled():
    print("Element is disabled")

# fill out the form
ids.send_keys("12827, 12855, 12888")



# submit the form
submit_button.click()
wait = WebDriverWait(driver, 5)
div = wait.until(EC.visibility_of_element_located((By.ID, "example_wrapper")))
print('Visible2')
scroll_duration = 5
scroll_pause_time = 0.1

# Get the height of the page
page_height = driver.execute_script("return document.body.scrollHeight")

# Calculate the total number of scrolls needed
scrolls = int(page_height / (scroll_duration / scroll_pause_time))

# Calculate the scroll distance for each iteration
scroll_step = page_height / scrolls

# Scroll from top to bottom of the page
for i in range(scrolls):
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(scroll_pause_time)

# close the browser
driver.quit()