import requests

# WEATHER PORTION #
# Check Weather for 8am, 12pm and 4pm
weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
weather_params= {
    'lat':-29.858681,
    'lon':31.021839,
    'units': 'metric',
    'exclude':'current,minutely,daily,alerts',
    'appid':'69f04e4613056b159c2761a9d9e664d2' # its not my api id
}

weather_response = requests.get(url=weather_url, params=weather_params)
weather_response.raise_for_status()
weathers = weather_response.json()['hourly'][:12]

# print(weathers)
def morning_weather():
    morning = weather_response.json()['hourly'][2]
    # print(morning)
    morning_temp = morning['temp']
    morning_weather = morning['weather'][0]['description']
    return f"Weather at 8am: {round(morning_temp)}°, {morning_weather}."



def afternoon_weather():
    afternoon = weather_response.json()['hourly'][6]
    # print(lunch)
    afternoon_temp = afternoon['temp']
    afternoon_weather = afternoon['weather'][0]['description']
    return f"Weather at Lunch Time (12pm): {round(afternoon_temp)}°, {afternoon_weather}."

def evening_weather():
    evening = weather_response.json()['hourly'][10]
    evening_temp = evening['temp']
    evening_weather = evening['weather'][0]['description']
    return f"Weather at 4pm: {round(evening_temp)}°, {evening_weather}."


def rain():
    will_rain = False
    for idx in range(12):
        if weathers[idx]['weather'][0]['id']<700:
            will_rain = True
            break
    return will_rain