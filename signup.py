from selenium import webdriver
from selenium.webdriver.common.by import By
# Use this class to use specific keys besides letters/numb
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Find field for first name
f_name = driver.find_element(By.NAME, value="fName")
# Type first name
f_name.send_keys("Sonni")

# Last name
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Gunnels")

# Email
email = driver.find_element(By.NAME, value="email")
email.send_keys("test@gmail.com")

# Submit button
submit = driver.find_element(By.XPATH, value='/html/body/form/button')
submit.click()
