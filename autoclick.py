#!/usr/bin/python3

import sys, pyautogui, time, keyboard, argparse

parser = argparse.ArgumentParser(description="Autoclicker")
parser.add_argument('-t', nargs=1, required=True, type=int, help='time in seconds')
args = parser.parse_args()

t_end = time.time() + args.t[0]
blu = True

for i in range(3,0,-1):
    print(str(i)+"...", end=" ", flush=True)
    time.sleep(1)
print("Go!")
print('hold CTRL to stop')

while time.time() < t_end:
    pyautogui.click(interval=0.01) 
    if keyboard.is_pressed('ctrl'):
        break
