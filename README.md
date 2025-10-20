# Funktionalitet
# - Starta övervakning
    Startar CPU, minnes och diskanvändning.
    Switch knapp på övervakningen
# - Lista aktiv övervakning
    Visa CPU, minnes och diskanvändning.
    Visa användaren att ingen övervakning är aktiv.
    Om den är aktiv så visas procent och se hur mycket GB som används.
    Ett val visas som man kan gå tillbaka till menyn
# - Skapa larm
    Startar en sub-meny som visar...
    1. CPU användning
    2. Minnes användning
    3. Disk användning
    4. Tillbaka till menyn
    Efter user choice så får user välja procentuell nivå där larmet aktiveras
    Procentuell nivå är mellan 1-100
    Efter user input då kommer nivå bekräftelse
    Else user input är invalid felmeddelande
    Tillbaka till menyn
# - Ta bort larm - optional
    Tar bort vald larm
    Gå tillbaka till huvudmeny
# - Visa larm
    Listar alla larm som user input har skrivit
    Ett val visas som man kan gå tillbaka till menyn
# - Starta övervakningsläge
    Starta ett läge som visar larm procent och visar hur datorn använder


# Non-functional Requirements:
# 3 files of code
# (larm_tracker.py (main),
# tracker_class.py,
# transaction_class.py,
# one or more JSON files)

# Data:
# Övervakning
# Larm