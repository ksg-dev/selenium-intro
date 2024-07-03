from selenium import webdriver
from selenium.webdriver.common.by import By
# Use this class to use specific keys besides letters/numb
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(article_count.text)

# Find link by link text and click
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find Search <input> by name - have to click mag glass now first
open_search_bar = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
open_search_bar.click()

# Then find search bar
search = driver.find_element(By.NAME, value="search")

# Type in search bar
search.send_keys("Python")
# Press enter
search.send_keys(Keys.ENTER)

# driver.quit()