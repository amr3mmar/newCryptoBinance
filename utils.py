import winsound
import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def beep():
    duration = 4000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)