import json
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def get_weather():
    req = Request('http://d1.weather.com.cn/sk_2d/101010100.html?_=1510475795976')
    req.add_header('Referer','http://www.weather.com.cn/weather1dn/101010100.shtml')
    data = urlopen(req)
    origin_data = data.read()
    decoded_data = origin_data.decode('utf8')
    weather_obj = json.loads(decoded_data[13:])
    print(weather_obj)
    # print('城市: %s \n温度: %s`C \n湿度: %s \n风级: %s\n天气: %s\n空气: %s' %(weather_obj['cityname'], weather_obj['temp']\
    #         ,weather_obj['SD'],weather_obj['WS'], weather_obj['weather'],weather_obj['aqi']))
if __name__ == '__main__':
    get_weather()