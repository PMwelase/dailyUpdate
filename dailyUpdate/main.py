from datetime import datetime as dt
import smtplib
import requests
import pandas as pd
from weather import *
from loadshedding import *


# GET TIME
now = dt.now()
today = now.weekday()


# HOW TO SEND EMAIL
df = pd.read_csv("subs.csv")



if __name__ == "__main__": 
    from_email='pmwelase023@student.wethinkcode.co.za'
    password="ugfg tfht geck izxr"

    morning_weather = morning_weather()
    afternoon_weather = afternoon_weather()
    evening_weather = evening_weather()

    content = f"Here's how your day is looking:\n{morning_weather}\n{afternoon_weather}\n{evening_weather}\n\n"
    if rain() == True:
        content += "You might want to carry an umbrella.\n"

    if len(affected_hours) > 0:
        content += f"There'll likely be loadshedding at the Durban Campus today at {(all_affected_hours())[0][0:5]}\n\n"
        if len(affected_hours) == 2:
            content += f"and at {(all_affected_hours[1][0:5])}"
        content += f"Make sure you've saved your work before then."

    else:
        content += f"We are currently NOT expecting any loadshedding today."
        
    content = content.encode('ascii', 'ignore').decode('ascii')
    
    for index, row in df.iterrows():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=row["email"],
                msg=f"Subject:Daily Update\n\nHi {row['name']},\n\n{content}\n\nWarm Regards,\nPhumelela"
                
        )



