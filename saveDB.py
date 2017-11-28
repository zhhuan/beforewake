import pymysql.cursors

#connect to the database
connection = pymysql.connect(host='localhost',
                             user='johan',
                             password='AlarmJohan',
                             db='weather_alarm',
                             charset='utf8')

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `weather` (`climate`, `air_sta`, `tep_cur`, `tep_low`) VALUES ('晴', '良好', 1, 20)"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()