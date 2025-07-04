import pyautogui
import time
import random

# === Koordinaten (bitte ggf. anpassen!) ===
FIGHT_BUTTON = (1250, 1320)
ATTACKS = [
    (1160, 1250),  # Attacke 1 (oben links)
    (1390, 1250),  # Attacke 2 (oben rechts)
    (1160, 1330),  # Attacke 3 (unten links)
    (1390, 1330)   # Attacke 4 (unten rechts)
]

# === Mausbewegungs-Toleranz zum Stoppen ===
MOUSE_TOLERANCE = 400  # px

# === Zufällige Verzögerungen ===
def short_delay():
    time.sleep(random.uniform(0.2, 0.5))

# === Startmeldung mit Countdown ===
start_delay = 10
print(f"Auto-Farmer startet in {start_delay} Sekunden...")
print("Zum Stoppen: Maus deutlich bewegen (>400 Pixel)")

for i in range(start_delay, 0, -1):
    print(f"Starte in {i}...", end='\r')
    time.sleep(1)

print("Starte jetzt!")

# Startposition der Maus merken
initial_mouse_pos = pyautogui.position()

try:
    while True:
        # === Sicherheits-Check: Mausbewegung ===
        current_mouse_pos = pyautogui.position()
        dx = abs(current_mouse_pos[0] - initial_mouse_pos[0])
        dy = abs(current_mouse_pos[1] - initial_mouse_pos[1])
        distance = (dx**2 + dy**2)**0.5

        if distance > MOUSE_TOLERANCE:
            print(f"\n🛑 Mausbewegung erkannt ({int(distance)} px) – Skript wird gestoppt.")
            break

        # === Fight-Button klicken ===
        pyautogui.click(1250, 1320)
        print("Fight-Knopf")
        short_delay()
        

        # === Attacken ===
        attack = random.choice(ATTACKS)
        pyautogui.click(attack)
        print(f"Attacke bei {attack} ausgeführt")
        pyautogui.press("space")
        
        # Taste w gedrückt halten
        pyautogui.keyDown('w')
        time.sleep(1.5)
        pyautogui.keyUp('w')
        print("Taste w")

        # Direkt danach Taste s gedrückt halten
        pyautogui.keyDown('s')
        time.sleep(2)
        pyautogui.keyUp('s')
        print("Taste s")

        pyautogui.keyDown('1')
        time.sleep(0)
        pyautogui.keyUp('1')
        print(" Taste 1 ")


except KeyboardInterrupt:
    print("\n🧼 Skript manuell mit STRG+C beendet.")
