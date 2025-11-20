import datetime as dt, pandas as pd
import glob, random
from main import send_email

my_gmail = ""
g_pass = ""
my_yahoo = ""
subject = 'Subject:Happy Birthday!\n\n'

#TODO check today
today = dt.datetime.today()

#TODO see if today is one of the birthdays in the birthdays csv
df = pd.read_csv('./birthdays.csv')
ppl_born_today = df[(df['month'] == today.month) & (df['day'] == today.day)]

#TODO select a birthday letter
def select_letter():
    files = glob.glob("./letter_templates/*.txt")
    random_file = random.choice(files)
    with open(random_file, 'r') as file:
        email_body = file.read()
    return email_body

#TODO Insert the name of the individual whose b-day is today in the name part of the letter
for index, row in ppl_born_today.iterrows():
    template = select_letter()
    name = row['name'].strip()
    email = row['email'].strip()
    body = template.replace('[NAME]',name)

#TODO send an email
    send_email(
            sendfr=my_gmail,
            sendfrp=g_pass,
            sendto=email,
            message=f'{subject}{body}',
            host="smtp.gmail.com",
            port=587,
        )
