import smtplib
#
# my_email = "pythonmailtest2023@gmail.com"
# password = "lhsq tscb rqsj rcxa"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="guiaugusto.castello@gmail.com", msg="subject:Hello world\n\nEmail's body")

import datetime as dt
import random

MY_EMAIL = "pythonmailtest2023@gmail.com"
MY_PASSWORD = "lhsq tscb rqsj rcxa"

now = dt.datetime.now()
weekday = 1
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="guiaugusto.castello@gmail.com",
            msg=f"Subject:Monday's motivation\n\n {quote}"
        )

