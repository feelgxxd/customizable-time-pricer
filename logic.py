import keyboard
import time
import os

half_hour = 0.5 * 60 * 60
meter = 400 / half_hour

cost = 2
while True:
    if keyboard.is_pressed('k'):
        break

    os.system('cls||clear')
    print(cost)
    cost += (meter / 100)
    time.sleep(1)

print("total cost:", cost)