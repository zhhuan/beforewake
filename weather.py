import json
import pymysql.cursors
from urllib.request import urlopen, Request


def get_status():
    req = Request('http://d1.weather.com.cn/sk_2d/101010100.html?_=1510475795976')
    req.add_header('Referer', 'http://www.weather.com.cn/weather1dn/101010100.shtml')
    data = urlopen(req)
    origin_data = data.read()
    decoded_data = origin_data.decode('utf8')
    weather_obj = json.loads(decoded_data[13:])
    get_fullstatus(weather_obj)

def get_fullstatus(weather_obj):
    status = {}
    status['climate'] = weather_obj['weather']
    status['tep_cur'] = weather_obj['temp']
    status['wind_dir'] = weather_obj['WD']
    status['wind_scl'] = weather_obj['WS']
    status['air_aqi'] = weather_obj['aqi']
    save_status(status)


def save_status(status):
    #connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='johan',
                                 password='AlarmJohan',
                                 db='weather_alarm',
                                 charset='utf8')

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `weather` (`climate`, `tep_cur`, `wind_dir`, `wind_scl`, `air_aqi`) VALUES (%s,%s,%s,%s,%s)" 
            cursor.execute(sql,(status['climate'],status['tep_cur'],status['wind_dir'],status['wind_scl'],status['air_aqi']))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()

if __name__ == '__main__':
    get_status()

