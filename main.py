import smtplib

my_email = "pythonmailtest2023@gmail.com"
password = "lhsq tscb rqsj rcxa"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="guiaugusto.castello@gmail.com", msg="subject:Hello world\n\nEmail's body")
