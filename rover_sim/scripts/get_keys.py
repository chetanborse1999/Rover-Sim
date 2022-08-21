import keyboard
import time
import os

while True:
    command_array = [0,0,0,0] # [forward, backward, left, right]
    if keyboard.is_pressed('0'):
        print("0")
        break
    else:
        if keyboard.is_pressed('w'):
            # print("w")
            command_array[0]=1
        if keyboard.is_pressed('s'):
            # print("s")
            command_array[1]=1
        if keyboard.is_pressed('a'):
            # print("a")
            command_array[2]=1
        if keyboard.is_pressed('d'):
            # print("d")
            command_array[3]=1

    # print(command_array)
    command_string = ''
    for i in command_array:
        command_string+=str(i)
    # print(command_array)
    f = open("thisFile.txt", "r")
    i = len(f.readlines())
    f.close()
    if i<1:
        f = open("thisFile.txt", "a")
        # print(command_string)
        f.write(command_string+"\n")
        f.close()
    else:
        # print("file buffer full")
        time.sleep(0.5)
        os.system('clear')


