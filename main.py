from pyowm import OWM



location = "Aachen,DE" #input("Введите локацию для запроса погоды:")

with open("api_key", "r") as file:
    weather_api_key = file.read()
print("Используется такой ключ:", weather_api_key)

try:
    open_weather_map = OWM(weather_api_key)
    open_weather_map.config['language'] = 'ru' # Язык результатов

    # запрос данных о текущем состоянии погоды
    now = open_weather_map.weather_manager().weather_at_place(location)
    forecast = open_weather_map.weather_manager().forecast_at_place(location, '3h') # 3h вернет недельный, так как daily не работает 

except:
    print("Извините. Ошибка запроса к серверу погоды")
    exit(1)

status = now.weather.detailed_status
temperature = int(now.weather.temperature('celsius')["temp"])
print("Сейчас за окном:", status,  "\nТемпература:", temperature)


if forecast.will_have_rain():
    print("На неделе будет дождь:", )
    dates = set()
    for rain in forecast.when_rain():
        dates.add(rain.reference_time('iso').split()[0])
    for date in dates:
        print(date)
