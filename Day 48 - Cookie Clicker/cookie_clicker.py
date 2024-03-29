from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service("D:\chromedriver-win32\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5   # 5 seconds from now
five_min = time.time() + 300 # 5 mins from now

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {item_prices[n]:item_ids[n] for n in range(len(item_prices))}
        print(cookie_upgrades)

        cookie_count = int(driver.find_element(By.XPATH, '//*[@id="money"]').text)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.XPATH, '//*[@id="money"]')
        print(cookie_per_second)
        break



