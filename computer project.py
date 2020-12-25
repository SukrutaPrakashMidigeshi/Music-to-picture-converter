from tkinter import *
from colour import Color
import sounddevice as sd

m = 6
fs = 44100 # frequency per second of the sound
time_seconds = m*m
# m*m is the time in seconds


print("please provide the audio input")
sound = sd.rec(int(time_seconds * fs), samplerate=fs, channels=2, dtype="int16")

# converting the audio signals into integer type array consisting of tuples with two entries


colour = Tk()
window = Canvas(colour, bg="white", width=210*m*10, height=210*m*10)


print("please wait for the sound file to be processed")


for x in range(210*m):
    for y in range(210 * m):
        a = len(str((abs(sound[x*y][0]))))
        b = len(str((abs(sound[x*y][1]))))
        h1 = int("1" + ("0" * a))
        h2 = int("1" + ("0" * b))
        e1 = abs(((sound[x*y][0]) / h1))
        e2 = abs(((sound[x*y][1]) / h2))
        e3=((((e1+e2)/2)+abs((e1-e2)))/2)
        a1=sound[x*y][0]
        a2=sound[x*y][1]
        if ((a1 % 2 == 0) and (a2 % 2 == 0)):

                 window.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill=Color(rgb=(e3, e2, e1)))

        elif ((a1 % 2 == 0) and (a2 % 2 != 0)):

                 window.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill=Color(rgb=(e3, e2, e1)))

        elif ((a1 % 2 != 0) and (a2 % 2 == 0)):

                 window.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill=Color(rgb=(e2, e3, e1)))

        else:

                 window.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill=Color(rgb=(e2, e3, e1)))





window.pack( pady =  "30")

colour.mainloop()



