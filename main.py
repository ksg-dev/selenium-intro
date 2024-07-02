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
# print(search_bar.get_attribute("placeholder"))
# Then we want to access submit button
button = driver.find_element(By.ID, value="submit")
# print(button.size)
# Get an element without a name, class, or id
# This is a link within an anchor tag within a div element w this name
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# Using XPATH - copy XPATH when you right click
submit_bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug_link.text)

# # Close particular tab
# driver.close()
#
# Close entire browser
driver.quit()