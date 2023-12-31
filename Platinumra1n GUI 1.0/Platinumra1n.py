import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from PIL import ImageTk, Image
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
import webbrowser

path = os.getcwd()

print(path)

root = tk.Tk()
frame = tk.Frame(root, width="600", height="300")

frame.pack(fill=BOTH,expand=True)
#frame.configure(background='#ECECEC')

root.iconphoto(False, tk.PhotoImage(file='goldrainicon.png'))

LAST_CONNECTED_UDID = ""
LAST_CONNECTED_IOS_VER = ""

def ios14():
    subprocess.run("./ios14/ibypass.sh", shell=True)
    
def credits():
    messagebox.showinfo("Credits", "This program was developed by @ios_euphoria and @Rodion_Shopify, Thanks to @Toni__Dev and @Rodion_Shopify for iOS 14 and 15 support. Additionally thanks to the Palera1n team for iOS 15 - 16 jailbreak. ")
    
def ios15():
        # Create a popup window
    messagebox.showinfo("iOS 15", "iOS 15 Enabled! Now Press Activation Bypass!")

    # Disable the button and change its text
    ios15.config(state="disabled", text="iOS 15 enabled")
    

def detectDevice():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    #step 1 technically
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./goldra1n/euphoria_scripts/ideviceinfo > ./goldra1n/euphoria_scripts/lastdevice.txt")
    
    time.sleep(2)

    f = open("./goldra1n/euphoria_scripts/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if("ERROR:" in fileData):
        #no device was detected, so retry user!
        print("ERROR: No device found!")

        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
    else:
        #we definitely have something connected...

        #find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start)+len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)

        #find the iOS
        #we definitely have something connected...
        start2 = 'ProductVersion: '
        end2 = 'ProductionSOC:'
        s2 = str(fileData)

        foundData2 = s2[s.find(start2)+len(start2):s2.rfind(end2)]
        deviceIOS = str(foundData2)
        LAST_CONNECTED_IOS_VER = str(deviceIOS)

        if(len(UDID) > 38):
            #stop automatic detection
            timerStatus = 0

            print("Found UDID: "+LAST_CONNECTED_UDID)
            messagebox.showinfo("iDevice is detected!","Found iDevice on iOS "+LAST_CONNECTED_IOS_VER)
#            cbeginExploit10["state"] = "normal"
#            cbeginExploit2["state"] = "normal"
            
            #messagebox.showinfo("Ready to begin!","We are ready to start bypass!")
            
            cbeginExploit10["state"] = "normal"

        else:
            print("Couldn't find your device")
            messagebox.showinfo("Somethings missing! 0x405","Try disconnecting and reconnecting your device.")

def startDFUCountdown():
    print("Get ready to put device into DFU mode...")


def enterRecMode():
    print("Kicking device into recovery mode...")
    os.system("./palera1n/euphoria_scripts/enterrecovery.sh")

def exitRecMode():
    print("Kicking device out of recovery mode...")
    os.system("./palera1n/euphoria_scripts/exitrecovery.sh")
    messagebox.showinfo("Sent command!","Kicked device out of recovery mode!\n\nNow if your device is not exiting recovery mode still and keeps looping to it, either re-jailbreak with the same jailbreak you did or remove the jailbreak you installed.")

def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")

def jailbreakIOS15SemiTethered():
    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER
    
    #iOSVER = str(LAST_CONNECTED_IOS_VER)
    iOSVer = askstring('Device iOS?', 'What iOS are you trying to bypass?')
    
    #check if theres a valid string to continue to reversing jb
    if(len(iOSVer) < 2):
        showinfo('Bypass Failed', 'Give me a valid iOS version.')
    else:
        showinfo('Ready to Jailbreak...', 'Hi, iOS '+str(iOSVer)+'. \n\nWe will now attempt to bypass iOS '+str(iOSVer)+' Semi-Tethered.')
        print("Starting bypass...")
        os.system("idevicepair unpair")
        os.system("idevicepair pair")
        os.system(f"cd ./goldra1n/ && ./goldra1n.sh --tweaks {iOSVer} --semi-tethered")
        
        print("Device is bypassed!\n")
        showinfo('Bypass Success!', 'Device is now bypassed!')

def callback(url):
   webbrowser.open_new_tab(url)

def quitProgram():
    print("Exiting...")
    os.system("exit")


root.title('PlatinumRa1n v1.0')
frame.pack()

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("grh.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.place(x=140, y=-50)

my_label2 = Label(frame,
                 text = "Designed for iOS 14.0 - 16.3")
 
# place the widgets
# in the gui window
my_label2.place(x=200, y=100)

my_label3 = Label(frame,
                 text = "ver 1.0")
 
# place the widgets
# in the gui window
my_label3.place(x=10, y=290)

cdetectDevice = tk.Button(frame,
                   text="Pair iDevice",
                   command=detectDevice)
cdetectDevice.place(x=50, y=150)

credits = tk.Button(frame,
                   text="Credits",
                   command=credits)
credits.place(x=60, y=250)

ios14 = tk.Button(frame,
                   text="iOS 14",
                   command=ios14)
ios14.place(x=255, y=150)

ios15 = tk.Button(frame,
                   text="Enable iOS 15",
                   command=ios15)
ios15.place(x=430, y=150)

cbeginExploit12 = tk.Button(frame,
                   text="Activation Bypass!",
                   command=jailbreakIOS15SemiTethered,
                   state="normal")
cbeginExploit12.place(x=220, y=180)

cexitRecovery = tk.Button(frame,
                   text="Exit Recovery Mode",
                   command=exitRecMode)
cexitRecovery.place(x=216, y=250)

#installdepen = tk.Button(frame,
#                   text="Install Dependencies",
#                   command=installDependenciesSH)
#installdepen.place(x=400, y=250)

#KILL USB TO STOP CONNECT AND DISCONNECT ISSUE
os.system("sudo killall -STOP -c usbd")

root.geometry("600x320")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

root.mainloop()


