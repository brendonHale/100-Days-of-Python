import smtplib
import datetime as dt
import random

MY_EMAIL = "scuba_steve@imawesome.com"
MY_PASSWORD = "qwerty"

now = dt.datetime.now()
weekday = now.weekday()

# Checks for Monday
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.imawesome.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



# import smtplib
#
# my_email = "scuba_steve@imawesome.com"
# # App password from email privacy settings
# password = "qwerty"
#
# # Make sure to check SMTP connection string as dictated by individual email sites
# with smtplib.SMTP("smtp.imawesome.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="skeletor@masteroftheuniverse.com",
#         msg="Subject:Hello\n\nYo, what's up my dude?"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# date_of_birth = dt.datetime(year=1999, month=3, day=14)