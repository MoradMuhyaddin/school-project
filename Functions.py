import os
import psutil
import time
from datetime import datetime

class Class_funktions:
    def __init__(self):
            # Skapar tomma lådor för CPU, ram och disk användning
            self.cpu = 0
            self.memory = 0
            self.disk = 0

    def menu_choices(self):
        # Menyval för användaren
        print("1. Start monitoring")
        print("2. Show last measured stats")
        print("3. Create alarm")
        print("4. Show alarm")
        print("5. Start monitoring alarms")
        print("6. Exit")
    
    def start_monitoring(self):
        func.console_clean()
        # Mäter systemets CPU, minne och disk användning
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage('/').percent
        # Skapar en tidsstämpel för mätningen
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"---START MONITORING---")
        time.sleep(2) # Programmet pausas i 2 sekunder innan den går tillbaks till menyn
        print(f"CPU: {self.cpu}%")
        print(f"Memory: {self.memory}% ({psutil.virtual_memory().used / (1024**3):.2f}GB / {psutil.virtual_memory().total / (1024**3):.2f}GB)")
        print(f"Disk: {self.disk}% ({psutil.disk_usage('/').used / (1024**3):.2f}GB / {psutil.disk_usage('/').total / (1024**3):.2f}GB)")

    def show_last_stats(self):
        func.console_clean()
        # Om inga stats har mätts än
        if self.cpu == 0 and self.memory == 0 and self.disk == 0:
            print("No stats have been measured yet. Please start monitoring first.")
            return
        else:
            # Visar den senaste mätta statsen
            print("--- LAST MEASURED STATS ---")
            print(f"CPU: {self.cpu}%")
            print(f"Memory: {self.memory}% ({psutil.virtual_memory().used / (1024**3):.2f}GB / {psutil.virtual_memory().total / (1024**3):.2f}GB)")
            print(f"Disk: {self.disk}% ({psutil.disk_usage('/').used / (1024**3):.2f}GB / {psutil.disk_usage('/').total / (1024**3):.2f}GB)")
            print(f"Time: {self.timestamp}")
    
    def console_clean(self):
        # Rensar konsollen  
        os.system('cls' if os.name=='nt' else 'clear')

# Skapar en instans av Class_funktions
func = Class_funktions()
