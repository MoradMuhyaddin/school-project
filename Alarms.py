
import time
import psutil
#import winsound  # Works on Windows only
from Funktions import *

alarm_func = Class_funktions()

def alarm(delay_seconds):
    time.sleep(delay_seconds)
    #winsound.Beep(14500, 1000)

alarms = {
    "CPU": [],
    "RAM": [],
    "Disk": [] 
}

def create_alarm():
    global alarms
    while True:
        alarm_func.console_clean()
        print("--- CREATE ALARM ---")
        print("1. CPU usage")
        print("2. Memory usage")
        print("3. Disk usage")
        print("4. Back to main menu")

        choice = input("\nChoose an option (1-4): ")

        if choice == "4":
            print("Returning to main menu...")
            time.sleep(1)
            break

        if choice in ["1", "2", "3"]: 
            hardware_map = {"1": "CPU", "2": "RAM", "3": "Disk"}
            hardware = hardware_map[choice]

            while True:
                alarm_func.console_clean()
                level_input = input(f"Set alarm level for {hardware.upper()} (1-100%): ")
                if level_input.isdigit() and 1 <= int(level_input) <= 100: # Om input är mellan 1-100
                    level = int(level_input) 
                    alarms[hardware].append(level) # Lägger till nytt larm till listan
                    print(f"Alarm for {hardware} set to {level}%.")
                    time.sleep(2)
                    break # Tillbaka till sub-menyn
                
                print("\nInvalid input. Please enter a number between 1 and 100.")
                time.sleep(1)
        else:
            print("\nInvalid choice, please try again.")
            time.sleep(1)

def show_alarms():
    alarm_func.console_clean()
    print("--- SHOWING ALARMS ---")
    for hardware, level in alarms.items():
        if level:
            for index in sorted(level):
                print(f"{hardware.capitalize()}: {index}%")
    else:
        print("No alarms have been set.")

def start_monitoring_alarms():
    while True:
        alarm_func.console_clean()
        print("--- SHOWING ALARMS ---")
        alarm_func.start_monitoring()
        time.sleep(0.5)
        for hardware, levels in alarms.items():
            current_usage = 0
            if hardware == "CPU":
                current_usage = psutil.cpu_percent(interval=1)
            elif hardware == "RAM":
                current_usage = psutil.virtual_memory().percent
            elif hardware == "Disk":
                current_usage = psutil.disk_usage('/').percent

            for level in levels:
                if current_usage >= level:
                    print(f"ALARM! {hardware} usage is at {current_usage}%, which exceeds the set alarm level of {level}%!")
                    alarm(1) # Väntar 1 sekund innan alarmet går igång
        print("Press Ctrl+C to stop monitoring alarms.")
        time.sleep(5)  # Väntar 5 sekunder innan nästa mätning
