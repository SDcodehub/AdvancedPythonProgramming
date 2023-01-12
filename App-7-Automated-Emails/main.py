import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday.strftime('%Y-%m-%d'),
                         to_date=today.strftime('%Y-%m-%d'),
                         language='en')
    email = yagmail.SMTP(user="spidy.in@gmail.com", password="fpackzekbzpjxpsw")
    email.send(to=row['email'],
               subject=f"Hi {row['interest']} news for today",
               contents=f"Hi {row['name']}, about your interest {row['interest']}" \
                        f"\n {news_feed.get()} \n Sagar")


while True:
    if datetime.datetime.now().hour == 13 and datetime.datetime.now().minute == 42:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)