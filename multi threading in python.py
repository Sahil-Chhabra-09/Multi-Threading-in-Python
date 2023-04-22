import tkinter as tk
 
window = tk.Tk()
window.title("Live Multithreading")
 

D1 = (0,0)
D2 = (0,1)
D3 = (1,0)
D4 = (1,1)
D5 = (2,0)
D6 = (2,1)


def display(num, displayLocation, refreshTime):
    frame = tk.Frame(
           master=window,
           relief=tk.RAISED,
           borderwidth=1
    )
    frame.grid(row=displayLocation[0], column=displayLocation[1])
    label = tk.Label(master=frame, text=f"\tRefresh Time : {refreshTime}s\t\t\n\tVal : {num}\t\t")
    label.pack()

import threading, multiprocessing
import random as r
import time

def task(lb, ub, refreshTime, displayLocation):
    while(1):
        num = r.randint(lb, ub)
        display(num, displayLocation, refreshTime)
        time.sleep(refreshTime)
        
t1 = threading.Thread(target = task, args = (10, 20, 10, D1))
t2 = threading.Thread(target = task, args = (-10, 10, 20, D2))
t3 = threading.Thread(target = task, args = (-100, 0, 8, D3))
t4 = threading.Thread(target = task, args = (0, 20, 12, D4))
t5 = threading.Thread(target = task, args = (-40, 40, 16, D5))
t6 = threading.Thread(target = task, args = (100, 200, 14, D6))



t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


window.mainloop()