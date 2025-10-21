import os
import psutil
import time

class Class_funktions:
    def __init__(self):
            self.cpu = 0 # Skapar tom låda för CPU användning
            self.memory = 0 # Skapar tom låda för ram användning
            self.disk = 0 # Skapar tom låda för disk användning


    def menu_choices(self):
        print("1. Start monitoring")
        print("2. Show last measured stats")
        print("3. Create alarm")
        print("4. Show alarm")
        print("5. Start monitoring alarms")
        print("6. Exit")
    
    def start_monitoring(self):
        func.console_clean()
        self.cpu = psutil.cpu_percent() # Mäter cpu användning
        self.memory = psutil.virtual_memory().percent # Mäter minne användning i procent
        self.disk = psutil.disk_usage('/').percent # Mäter disk använding i procent
        print(f"---START MONITORING---")
        time.sleep(2) # Programmet pausas i 2 sekunder innan den går tillbaks till menyn
        print(f"CPU: {self.cpu}%")
        print(f"Memory: {self.memory}%")
        print(f"Disk: {self.disk}%")
    
    def show_last_stats(self):
        func.console_clean()
        print("--- Last Measured Stats ---")
        print(f"CPU Usage: {self.cpu}%") 
        print(f"Memory Usage: {self.memory}%")
        print(f"Disk Usage: {self.disk}%")


    def console_clean(self):
        # Rensar konsollen  
        os.system('cls' if os.name=='nt' else 'clear')

func = Class_funktions()