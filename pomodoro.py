
import wave
from time import sleep
import pynput
import keyboard
from pygame import mixer
import sys

def playmusic():
    filz = "alertsfx.mp3"
    mixer.init()
    mixer.music.load(filz)
    mixer.music.play()
    if keyboard.read_key() == 'space':
        mixer.music.stop()


def settings():
    global cycle
    global breaktime
    global amt_cycles
    sumting = True
    while sumting:
        try:
            cycle = int(input("How many minutes long do you want the study cycle to be?: "))
            breaktime = int(input("How many minutes long do you want your break to be?: "))
            amt_cycles = int(input("How many cycles do you wanna do?: "))
            sumting = False
        except ValueError:
            print("Something went wrong, try again.")
            sumting = True
        
def timingz(cycle,breaktime,amt_cycles):
    if type(amt_cycles) == int:
        for times in range(amt_cycles):
            sleep(cycle*60)
            playmusic()
            sleep(amt_cycles*60)
            playmusic()
    

def main():
    settings()
    print("Cycle starting now")
    timingz(cycle,breaktime,amt_cycles)


if __name__ == '__main__':
    print("btw: You can use space to stop the music")
    main()
   



