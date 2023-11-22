import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# start a new Chrome browser session
options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
weave = Select(driver.find_element(by=By.ID, value="testweave"))
category = Select(driver.find_element(by=By.ID, value="testcategory"))
type1 = Select(driver.find_element(by=By.ID, value="testtype"))
submit_button = driver.find_element(by=By.ID, value="transubmit")
time.sleep(4)
category.select_by_index(0)
category.select_by_index(1)
time.sleep(4)
weave.select_by_index(2)
weave.select_by_index(3)
time.sleep(4)
type1.select_by_index(2)
type1.select_by_index(3)
time.sleep(4)
# submit the form
submit_button.click()
time.sleep(4)
wait = WebDriverWait(driver, 5)
div = wait.until(EC.visibility_of_element_located((By.ID, "example_wrapper")))
print('Visible2')
scroll_duration = 3
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