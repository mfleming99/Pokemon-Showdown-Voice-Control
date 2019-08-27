from voice_recognition import listen
from showdown_handler import select_input
import time
while(True):
    time.sleep(10)
    command = listen()
    while(not select_input(command)):
        command = listen()
