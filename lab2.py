import requests
city = "Moscow,RU"
appid = "5a5f32112e4f26968a1015a2fc930e71"
res = requests.get("https://api.openweathermap.org/data/2.5/forecast"),
parans={'q':city,'units':'netric','lang': 'ru''APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']),"> \r\nПогодные условия<",
i['weatrher'][0]['description'],"r \r\nСкорость ветра>", i["wind"]["speed"],"\r\nВидимость","<",i["visibility"],">")
print("__________________")