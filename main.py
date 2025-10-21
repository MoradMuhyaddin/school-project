import time
import psutil
import os
#import winsound  # Works on Windows only
import Funktions
import Alarms
func = Funktions.Class_funktions()

def main():
    
    app_is_running = True

    while app_is_running:

        valid_choice = False
        while not valid_choice:
            Funktions.console_clean() 
            # Kallar console_clean från Funktions.py
            func.menu_choices() 
            # Kallar på menyn från Class_funktions klassen
            choice = input("Choose between (1-6): ")
            match choice:
                case "1":
                    func.start_monitoring()
                    valid_choice = True
                case "2":
                    func.show_last_stats()
                    input("Press Enter to continue...")
                    valid_choice = True
                case "3":
                    Alarms.create_alarm() 
                    # Kallar på create_alarm funktionen i Alarm.py
                    input("Press Enter to continue...")
                    valid_choice = True
                case "4":
                    Alarms.show_alarms() # Kallar på show_alarm funktionen i Alarm.py
                    input("Press Enter to continue...")
                    valid_choice = True
                case "5":
                    pass
                
                case "6":
                    quit()

main()