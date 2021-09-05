import multiprocessing
import keyboard
from pynput.mouse import Button, Controller
mouse = Controller()
import time
import sys

def help():
 print("Usage: autoclicker.py autoclick_level")
 print("Level 0: About 13 CPS")
 print("Level 1: About 19 CPS")
 print("Level 2: About 37 CPS")
 print("Level 3: About 54 CPS")
 print("Level 4: About 70 CPS")
 print("Level 5: About 84 CPS")
 print("Level 6: About 135 CPS")
 print("Level 7: About 147 CPS")
 print("Level 8: About 200 CPS")
 print("Level 9: About 400 CPS")
 print("Level E(EXTREME): try it yourself :)")

if not len(sys.argv) == 2:
 help()
 exit()

global sleep

if sys.argv[1] == "1":
 sleep = 1000

elif sys.argv[1] == "0":
 sleep = 750

elif sys.argv[1] == "2":
 sleep = 2000

elif sys.argv[1] == "3":
 sleep = 3000

elif sys.argv[1] == "4":
 sleep = 4000

elif sys.argv[1] == "5":
 sleep = 5000

elif sys.argv[1] == "6":
 sleep = 8000

elif sys.argv[1] == "7":
 sleep = 9000

elif sys.argv[1] == "8":
 sleep = 12000

elif sys.argv[1] == "9":
 sleep = 30000

elif sys.argv[1] == "E":
 sleep = 70000

else:
 help()
 exit()

print('''
 .d8b.  db    db d888888b  .d88b.   .o88b. db      d888888b  .o88b. db   dD d88888b d8888b. 
d8' `8b 88    88 `~~88~~' .8P  Y8. d8P  Y8 88        `88'   d8P  Y8 88 ,8P' 88'     88  `8D 
88ooo88 88    88    88    88    88 8P      88         88    8P      88,8P   88ooooo 88oobY' 
88~~~88 88    88    88    88    88 8b      88         88    8b      88`8b   88~~~~~ 88`8b   
88   88 88b  d88    88    `8b  d8' Y8b  d8 88booo.   .88.   Y8b  d8 88 `88. 88.     88 `88. 
YP   YP ~Y8888P'    YP     `Y88P'   `Y88P' Y88888P Y888888P  `Y88P' YP   YD Y88888P 88   YD 

Github/ngn13 - Python autoclicker

j to activate, k to deactivate                                                                                        
''')
enable = False
while True:
 try:
  if keyboard.is_pressed('j'):
   enable = True
  elif keyboard.is_pressed('k'):
   enable = False

  if enable == True:
   mouse.click(Button.left, 1)
   time.sleep(50 / sleep)
  else:
   pass
 
 except KeyboardInterrupt:
  print("\nExiting!")
  exit()

