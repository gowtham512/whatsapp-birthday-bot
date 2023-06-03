import pywhatkit
import pandas as pd
import time
from datetime import datetime
import random


today = datetime.today().strftime("%d-%m")
df=pd.read_csv('contacts.csv')
for index, row in df.iterrows():
    date = row['Date']
    print(date)
    phone = row['Phone']
    print(f"+{phone}")
    if date==today:
        now = datetime.now()
        hour = now.hour
        minutes = now.minute
        seconds = now.second
        if seconds<=50:
            c = random.randint(1,2)
            print(f"birthday_images/{c}.jpg")
            pywhatkit.sendwhats_image(f"+{phone}",f"birthday_images/{c}.jpg")
            time.sleep(30)
            print("Successfully Sent!")
        else:
            c = random.randint(1,2)
            pywhatkit.sendwhats_image(f"+{phone}",f"birthday_images/{c}.jpg")
            time.sleep(30)
            print("Successfully Sent!")
