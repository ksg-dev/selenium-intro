# Challenge: scrape python site for upcoming events and output dictionary
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events = driver.find_element(By.CLASS_NAME, value="event-widget")
# print(events.text)
events_dates = events.find_elements(By.TAG_NAME, value="time")
events_names = events.find_elements(By.CSS_SELECTOR, value="a")

dates = [event.text for event in events_dates]
formatted_dates = []
year = date.today().year
for each in dates:
    month, day = each.split("-")
    d = f"{year}-{month}-{day}"
    formatted_dates.append(d)


names = [event.text for event in events_names][1:]


for t, n in zip(formatted_dates, names):
    event_dicts = {"time": t, "name": n}
    new_dict = {i: event_dicts for i in range(4)}

print(new_dict)
# print(formatted_dates)
# print(dates)
# print(names)

# Instructor solution once get two lists
# Tried something similar but date still wasn't formatted correctly
"""
event_times = [list of event times]
event_names = [list of event names]
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
        }

"""


driver.quit()
