# import the important library
import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # to use Raspberry Pi board pin numbers
GPIO.setup(11, GPIO.OUT) # set up GPIO output channel


mainwindow=tk.Tk()
mainwindow.title('Test ')
mainwindow.geometry('640x340')


my_label=tk.Label(mainwindow,text="My First UI",
                  font=("Arial",22), bg= "Green",fg="white")
my_label.grid(row=0,column=0,sticky='NSEW',padx=10,pady=10)

button_on=tk.Button(mainwindow,text="On",bg="black",fg="white",
                    command=lambda :my_on())
button_on.grid(row=1,column=0,sticky='NSEW',padx=10,pady=10)


button_off=tk.Button(mainwindow,text="OFF",bg="black",fg="white",
                     command=lambda:my_off())
button_off.grid(row=1,column=1,columnspa=1,sticky='NSEW',padx=10,pady=10)


def my_on():
    print('Led Turn On !!!!! ')
    GPIO.output(11, GPIO.LOW) # set RPi board pin 11 low. Turn off LED.
    time.sleep(1)
    print('Yes you did it !')


def my_off():
    print('Led Turned Off !!!!!!  ')
    GPIO.output(11, GPIO.HIGH) # set RPi board pin 11 high. Turn on LED.
    time.sleep(2)
    print('Great Work ! ')




mainwindow.mainloop()