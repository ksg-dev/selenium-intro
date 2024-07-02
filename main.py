from selenium import webdriver
# To hold a piece of data from a site
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# Update URL to python page
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Find search bar on python site
search_bar = driver.find_element(By.NAME, value="q")
# add . to access attributes
print(search_bar.get_attribute("placeholder"))
# Then we want to access submit button
button = driver.find_element(By.ID, value="submit")
print(button.size)

# # Close particular tab
# driver.close()
#
# Close entire browser
driver.quit()