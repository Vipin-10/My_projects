import tkinter
import speedtest

def speed_check():
    mf=speedtest.Speedtest()
    mf.get_servers() #To get servers
    down= str(round(mf.download() / (1024*1024), 3)) + " Mbps"  #It'll come in bytes. So to convert into Mbps we have to divide it with 1024*1024
    up= str(round(mf.upload() / (1024*1024), 3))  + " Mbps"
    lab_down.config(text= down)
    lab_up.config(text= up)


'''
Getting Speedtest class from speedtest module
Class have multiple functions
'''
mf = tkinter.Tk()     # Calling tkinter class
mf.title("Internet Speed Test")
mf.geometry("500x570")
mf.config(bg="orange")
'''
Calling label function
Inside label function, we will first write Tk's class's object
'''
lab= tkinter.Label(mf, text="Internet Speed Meter", font=("Georgia", 30, "bold"), bg="orange", fg="white")
lab.place(x=28, y=40, height=40, width=444)

lab= tkinter.Label(mf, text="Downloading Speed", font=("Georgia", 25, "bold"), bg="orange", fg="white")
lab.place(x=80, y=140, height= 40)

lab_down= tkinter.Label(mf, text="00", font=("Georgia", 25, "bold"), bg="black", fg="white")
lab_down.place(x=60, y=210, height=40, width= 380)

lab= tkinter.Label(mf, text="Upload Speed", font=("Georgia", 25, "bold"), bg="orange", fg="white")
lab.place(x=130, y=290, height=40)

lab_up= tkinter.Label(mf, text="00", font=("Georgia", 25, "bold"), bg="black", fg="white")
lab_up.place(x=60, y=360, height=40, width= 380)

button= tkinter.Button(mf, text="Check Speed", font=("Georgia", 25, "bold"), relief=tkinter.RAISED, bg="blue", command=speed_check)
button.place(x=130, y=450, height=40)
mf.mainloop()