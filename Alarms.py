# ...existing code...
import time
import psutil
#import winsound  # Works on Windows only
import Funktions



def alarm(delay_seconds):
    time.sleep(delay_seconds)
    #winsound.Beep(14500, 1000)

alarms = {
    "cpu": None,
    "memory": None,
    "disk": None 
}

def create_alarm():
    global alarms
    while True:
        print("--- CREATE ALARM ---")
        print("1. CPU usage")
        print("2. Memory usage")
        print("3. Disk usage")
        print("4. Back to main menu")

        choice = input("Choose an alternative between (1-4): ")

        if choice in ["1", "2", "3"]: 
            hardware_map = {"1": "cpu", "2": "memory", "3": "disk"}
            hardware = hardware_map[choice]

            while True:
                Funktions.console_clean()  # Rensar terminal
                level = input(f"Set a level for alarm ({hardware}) mellan 1-100: ")
                if level.isdigit() and 1 <= int(level) <= 100:
                    alarms[hardware] = f"{level}%"
                    print(f"Alarm for {hardware} set to {level}%.")
                    break
                else:
                    print("Wrong input, please enter a number between 1 and 100.")
            Funktions.console_clean()
            continue

        elif choice == "4":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice, please try again.")

def show_alarms():
    print("--- SHOWING ALARMS ---")
    has_alarms = False
    for hardware, level in alarms.items():
        if level:
            print(f"{hardware.capitalize()}: {level}")
            has_alarms = True
    if not has_alarms:
        print("No alarms have been set.")