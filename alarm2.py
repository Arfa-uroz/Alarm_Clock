from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image

import datetime
import time
from pygame import mixer
from threading import *



root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")
root.configure(bg="#fef0f8")
root.resizable(False,False)


a = Label(root,font=("Helvatica",15),text="Set Alarm",bg="#fef0f8",fg="black")
a.grid(row=0,column=0)
frame_line = Frame(root, width=400, height=5, bg="black")
frame_line.grid(row=1,column=0)
'''frame_body = Frame(root, width=400, height=290, bg="white")
frame_line.grid(row=3,column=0)'''

alarm_icon = ImageTk.PhotoImage(Image.open(r"D:\Python_Programs\projectAlarm\icons8-alarm-clock.png"))
#alarm_icon.resize((100,100))
#alarm_icon = ImageTk.PhotoImage(alarm_icon)

img = Label(root,height=70,width=70,image=alarm_icon, bg="#fef0f8")
img.place(x=10,y=50)

hours =Label(root,font=("Helvatica",10),text="Hours",bg="#fef0f8",fg="black")
hours.place(x=150,y=60)
c_hours = Combobox(root,width=2,font=("Helvatica",10))
c_hours['values'] = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23'
        )
c_hours.current(0)
c_hours.place(x=150,y=90)

min =Label(root,font=("Helvatica",10),text="Minutes",bg="#fef0f8",fg="black")
min.place(x=210,y=60)
c_min = Combobox(root,width=2,font=("Helvatica",10))
c_min['values'] = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
c_min.current(0)
c_min.place(x=210,y=90)

sec =Label(root,font=("Helvatica",10),text="Seconds",bg="#fef0f8",fg="black")
sec.place(x=280,y=60)
c_sec = Combobox(root,width=2,font=("Helvatica",10))
c_sec['values'] = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
c_sec.current(0)
c_sec.place(x=280,y=90)

def acti_alarm():
    t = Thread(target=alarm)
    t.start()

selected = IntVar()

def sound_of_alarm():
    mixer.music.load(r"D:\Python_Programs\projectAlarm\alarm_clock_old.mp3")
    mixer.music.play()
    selected.set(0)

mixer.init()

def stop_forcefully():
    mixer.music.stop()
    print("Deactivated alarm")


def alarm():
    while True:
        #control = 1
        set_alarm_time = f"{c_hours.get()}:{c_min.get()}:{c_sec.get()}"
        time.sleep(1)

        curr_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(curr_time,set_alarm_time)

        #if control == 1:
        if curr_time == set_alarm_time:
            print("Time to wake up!!!")
            sound_of_alarm()
            rad2 = Button(root,font=("Helvatica",10),text="Stop ",bg="#fef0f8",command=stop_forcefully)
            rad2.place(x=200,y=150) 

    
            


rad1 = Button(root,font=("Helvatica",10),text="Save ",bg="#fef0f8",command=acti_alarm)
rad1.place(x=120,y=150)





root.mainloop()