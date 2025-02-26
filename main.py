import random
import smtplib
import datetime as dt


# Todo.1 open quotes file and make list
with open ("quotes.txt","r" , encoding="utf-8") as file :
    content = file.readlines()

# todo.2 create date time to send the quotes which might be monday
date = dt.datetime.now()
day_of_week = date.weekday()
weekly_quotes = random.choice(content)
message =f"Subject : Weekly Motivational Quotes \n\n{weekly_quotes} "

# todo.3  create smtplip  email sender to send it
# sending an emails every monday < You could replace the 0 to any other value 1 or 2 to chang the day respectively >
if day_of_week == 0:
    email = "youre_email@gmail.com"
    # password comes from your app password in your email settings
    password = "app password"
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="receiver email" , msg=message.encode('utf-8'))
