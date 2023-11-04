# import smtplib
#
# my_email = "pythonmailtest2023@gmail.com"
# password = "lhsq tscb rqsj rcxa"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="guiaugusto.castello@gmail.com", msg="subject:Hello world\n\nEmail's body")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)

print(date_of_birth)
