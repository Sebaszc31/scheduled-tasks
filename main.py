import random
import smtplib
import pandas
import datetime as dt
import os

MY_EMAIL = "sebasydaniudemy@gmail.com"
MY_PASSWORD = "tqxo zagz fphr dide  "

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("Day 32/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index , data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"Day 32/letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        birthday_person = birthdays_dict[today_tuple]
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs= birthday_person["email"], 
            msg= f"Subject:Happy Birthday!!\n\n{contents}")





