import time
import psutil
import os
#import winsound  # Works on Windows only
import Funktions
import Alarms
func = Funktions.Class_funktions()

def main():
    
    monitoring = True

    while monitoring:

        valid_choice = False
        while not valid_choice:
            func.console_clean()
            func.menu_choice()
            choice = input("Choose between (1-6): ")
            match choice:
                case "1":
                    func.start_monitoring()
                    valid_choice = True
                case "2":
                    func.list_alarms()
                    input("Press Enter to continue...")
                    valid_choice = True
                case "3":
                    Alarms.create_alarm(func)
                    input("Press Enter to continue...")
                    valid_choice = True
                case "4":
                    Alarms.show_alarms()
                    input("Press Enter to continue...")
                    valid_choice = True



main()