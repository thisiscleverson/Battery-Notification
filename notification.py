import psutil
import time
import os
from playsound import playsound
import notify2

notify2.init("Battery-Notification")

Title = "Battery"
Msg = "Your battery is ranning low"

Title_charging = 'Battery Charging'
Msg_charging = 'Your battery is charging'

values_low = 20          # valor da bateria que deve avisar quando a bateria estiver no final
suspend_LOW_battery = 10 # valor mini para suspender o notebook

show_once = True
show_once_plugged = True
show_once_suspend = True

icon_Battery_low = '/home/cleverson/app/icon/icons-ranning-low.png'   # icone da bateria com pouca carga
icon_Battery_charging = '/home/cleverson/app/icon/icons-charging-battery.png' # icone da bateria se estiver carregando

sound_Battery_low = '/home/cleverson/app/sound/soft_notification-battery-ranning-low.mp3' # toque da bateria com pouca carga
sound_Battery_charging = '/home/cleverson/app/sound/notification_sound-battery-charging.mp3' # toque da bateria se estiver carregando

#--------------------------------------------------------------------#


def notifyme(Title, Message,icon):
    n = notify2.Notification(Title,Message,icon)
    return n


def battery_status():
    power = psutil.sensors_battery()
    plugged = power.power_plugged
    percent = int(power.percent)
    return percent,plugged


#----------------------------------------------------------------#

time.sleep(1)

if __name__ == "__main__":
    
    while True:

        percent_battery,plugged = battery_status()


        if percent_battery == values_low and show_once == True and plugged != True: # mostrar noticação se a bateria estiver com pouca carga
            n=notifyme(Title, Msg, icon_Battery_low)
            n.show()
            playsound(sound_Battery_low)
            show_once = False

        elif percent_battery == suspend_LOW_battery and show_once_suspend == True: # suspender o notebook se a carga chegar ao minimo
            os.system("systemctl suspend -i")
            show_once_suspend = False

        elif plugged == True and show_once_plugged == True: # verificar se o notebool esta com o carregador
            n=notifyme(Title_charging, Msg_charging,icon_Battery_charging)
            n.show()
            playsound(sound_Battery_charging)
            show_once_plugged = False 

        elif percent_battery != values_low and show_once == False and plugged != False: # atualizar o show_once ser tudo já foi execultado
            show_once = True
            show_once_plugged = True

        elif plugged != True and show_once_plugged != True:
            show_once_plugged = True

        time.sleep(3)


