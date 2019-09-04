from win32com.client import GetObject
import time
import tkinter as tk
from tkinter import ttk




def center_window(box, w=300, h=200):
    # get screen width and height
    ws = box.winfo_screenwidth()
    hs = box.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    box.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
def popupmsg(msg):
    LARGE_FONT= ("Verdana", 12)
    popup = tk.Tk()
    center_window(popup,500, 300) 
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=100, padx=100)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
WMI = GetObject('winmgmts:')

while True:
    for battery in WMI.InstancesOf('Win32_Battery'):
        batteryStatus = int(battery.BatteryStatus) #1 = Discharging
        chargeRemaining = int(battery.EstimatedChargeRemaining)
        if chargeRemaining <= 40 and (batteryStatus != 6  and batteryStatus != 2):
            popupmsg("PlugIn Loading")
        elif chargeRemaining >= 80 and (batteryStatus == 6 or batteryStatus == 2):
            popupmsg("Unplug Loading")
    time.sleep(600)

