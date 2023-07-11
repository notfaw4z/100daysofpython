import smtplib
import datetime as dt
import random

MY_EMAIL = "sender email"
MY_PASSWORD = "app password"
day_of_week = dt.datetime.now().weekday()

with open("quotes.txt", "r") as data:
    all_quotes = data.readlines()
    quote = random.choice(all_quotes)

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receiver email",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
