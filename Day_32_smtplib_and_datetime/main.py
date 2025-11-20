import smtplib
import datetime as dt
import random
#
my_gmail = ""
g_pass = ""
my_yahoo = ""

#
# #this is how you send an email using python. This email will most likely end up in spam using this method
#
# with smtplib.SMTP('smtp.gmail.com', 587) as gmail_connection:
#     gmail_connection.starttls()
#     gmail_connection.login(my_gmail, g_pass)
#     gmail_connection.sendmail(my_gmail, my_yahoo, "Subject:Hello\n\nThis is the body of my email")


#
# now = dt.datetime.now()
# year = now.year
#
# new_date = dt.date(year = 1998, month=5, day=10)
# print(now)

def send_email(**kw):
    sendfr = kw.get("sendfr")
    sendfrp = kw.get("sendfrp")
    sendto = kw.get("sendto")
    message = kw.get("message")
    host = kw.get("host")
    port = kw.get("port")
    with smtplib.SMTP(host, port) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(sendfr, sendfrp)
        gmail_connection.sendmail(sendfr, sendto, message)

subject = 'Subject:Daily Motivational Quote\n\n'
today = dt.datetime.today()

with open('./quotes.txt', 'r') as quotes:
    daily_quotes = [quote.strip() for quote in quotes]

if today.weekday() == 2:
    quote_today = random.choice(daily_quotes)
    send_email(
        sendfr=my_gmail,
        sendfrp=g_pass,
        sendto=my_yahoo,
        message=f'{subject}{quote_today}',
        host="smtp.gmail.com",
        port=587,
    )

#
# print(today.weekday())
# print(today.day)
# print(today.strftime("%A"))
