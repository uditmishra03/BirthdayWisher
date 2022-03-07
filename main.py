import smtplib
from random import choice
import datetime as dt

MY_EMAIL = "uditmiishraa@gmail.com"
PASSWORD = "Ram@1010420"

today = dt.datetime.today()
todayIs = today.weekday()

if todayIs == 0:
    # Create a list from the text file.
    with open("quotes.txt", "r") as data:
        all_quotes = data.readlines()
    quote = choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # This is for encryption of message sent over the protocol
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tarangmishraa@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
