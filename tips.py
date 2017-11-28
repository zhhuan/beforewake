import pymysql.cursors
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def get_suggestion():
    response = urlopen('http://www.weather.com.cn/weather1dn/101010100.shtml')
    data = response.read()
    html = BeautifulSoup(data)
    suggest_node = html.find('div',class_='lv')
    nodes = suggest_node.find_all('dl')
    texts = []
    for node in nodes:
        suggest_text = node.find('dd').get_text()
        quota_text = "'"+suggest_text+"'"
        texts.append(quota_text)
    save_suggests(texts)
    #print(texts)
    return texts

 
def save_suggests(texts):
    #connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='johan',
                                 password='AlarmJohan',
                                 db='weather_alarm',
                                 charset='utf8')

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `suggestion` (`sugg_UV`,`sugg_cold`,`sugg_cloth`,`sugg_car`,`sugg_sport`,`sugg_air`) \
                   VALUES(%s,%s,%s,%s,%s,%s)" % (texts[0],texts[1],texts[2],texts[3],texts[4],texts[5])
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()
