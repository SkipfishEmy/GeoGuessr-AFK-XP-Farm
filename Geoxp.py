from pyautogui import click, position, press 
import time
import keyboard 

def test_func():
    time.sleep(2)

    x = 1641
    y = 779


    def click_button(x, y):
        for i in range (1):
            click(x, y)
            print('click:', i)
            time.sleep(2)
            keyboard.press('space')
            keyboard.release('space')
            print('press:', i)
      

    click_button(x, y)

for i in range(2000):
    test_func()

