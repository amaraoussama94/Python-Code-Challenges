import sched # sched for event (planning)
import time
import winsound as ws  #ork only for windows systeme


def set_alarm(alarm_time , wave_file , message):
    s = sched.scheduler (time.time , time.sleep)
    s.enterabs(alarm_time , 1 , print , argument=(message ,)) # 1 to maker it high praio
    s.enterabs(alarm_time , 1 ,  ws.PlaySound , argument=(wave_file , ws.SND_FILENAME))
    print('alarm set for ' , time.asctime(time.localtime(alarm_time)))
    s.run()
    
alarm_time= time.time()+1 #1s
wave_file='Warning.wav'
message='test'
set_alarm(alarm_time , wave_file , message)
