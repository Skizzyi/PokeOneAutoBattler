import pyautogui
import time

print("Starte... bewege die Maus auf den gewünschten Button.")
time.sleep(5)

while True:
    x, y = pyautogui.position()
    print(f"Position: ({x}, {y})", end="\r")  # zeigt Position in einer Zeile an
    time.sleep(0.1)