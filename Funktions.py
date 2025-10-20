import os
import psutil
import time
class Class_funktions:
    def __init__(self):
            self.cpu = 0
            self.memory = 0
            self.disk = 0


    def menu_choice(self):
        print("1. Start monitoring")
        print("2. List of active alarms")
        print("3. Create alarm")
        print("4. Show alarm")
        print("5. Start monitoring alarms")
        print("6. Exit")
    
    def start_monitoring(self):
        self.console_clean()
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage('/').percent
        print(f"---START MONITORING---")
        time.sleep(2)
    
    def list_alarms(self):
        self.console_clean()
        print("Active alarms:")
        print(f"CPU Alarm: {self.cpu}%")
        print(f"Memory Usage: {self.memory}%")
        print(f"Disk Usage: {self.disk}%")
        input("Press Enter to continue...")
    


    def console_clean(self):
        os.system('cls' if os.name=='nt' else 'clear')


    def show_alarms(func):
         func.console_clean()
         print("---SHOWING ALARMS---")