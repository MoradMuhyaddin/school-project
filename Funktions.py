import os # Rensar skärmen efter input
import psutil # Hämtar 
import time
class SystemMonitor:
    def __init__(self):
            self.cpu = 0 # Skapar tom låda för CPU användning
            self.memory = 0 # Skapar tom låda för ram användning
            self.disk = 0 # Skapar tom låda för disk användning


    def menu_choice(self):
        print("1. Start monitoring")
        print("2. List of active alarms")
        print("3. Create alarm")
        print("4. Show alarm")
        print("5. Start monitoring alarms")
        print("6. Exit")
    
    def start_monitoring(self):
        console_clean()
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage('/').percent
        print(f"---START MONITORING---")
        time.sleep(2)
    
    def display_usage(self):
        console_clean()
        print("--- Last Measured Usage ---")
        print(f"CPU: {self.cpu}%")
        print(f"Memory: {self.memory}%")
        print(f"Disk: {self.disk}%")


def console_clean():
    """Clears the console screen."""
    os.system('cls' if os.name=='nt' else 'clear')