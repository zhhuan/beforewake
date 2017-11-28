import time
import get_forecast
import text2audio
from pygame import mixer


def soundStart():
    filename = 'default.mp3'
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    time.sleep(10)
    # print(time.localtime())
    # mixer.music.stop()
    # print(time.localtime())



def main():
    get_forecast.get_status()
    #cur_time = time.localtime()
    #filename = '%s%s%s\.mp3' %(cur_time[0],cur_time[1],cur_time[2])
    text2audio.run(result='default.mp3')
    time.sleep(10)
    not_executed = 1
    while(not_executed):
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
        if hour == 20 and minute == 23:
            soundStart()
            not_executed = 0

if __name__ == '__main__':
    main()
