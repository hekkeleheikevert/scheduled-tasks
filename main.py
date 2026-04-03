
import datetime as dt
import random
import pandas
import smtplib
import os

MY_MAIL = os.environ.get("MY_MAIL")
MY_PSW = os.environ.get("MY_PSW")

today = dt.datetime.now()
today_date = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_date in birthday_dict:
    birthday_boy = birthday_dict[today_date]
    path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(path) as letter:
        contents = letter.read()
        new_wish = contents.replace("[NAME]", birthday_boy["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PSW)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=birthday_boy["email"],
                            msg=f"Subject:Happy Birthday {birthday_boy["name"]}\n\n{new_wish}")

