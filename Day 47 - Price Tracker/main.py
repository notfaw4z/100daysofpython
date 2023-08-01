import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_1_sspa?keywords=sony%2Bxm4&qid=1690911018&s=electronics&sprefix=sony%2Bxm%2Celectronics%2C105&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,en-US;q=0.6"
}

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
TO_ADDRESS = os.environ["TO_ADDRESS"]

response = requests.get(url=URL, headers=header)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
price_float = float(price.split("$")[1])
title = soup.find(class_="a-size-large product-title-word-break").getText().strip()

if price_float < 400:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg=f"{title} is now at ${price_float}"
        )