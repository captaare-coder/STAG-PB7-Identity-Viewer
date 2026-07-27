import subprocess
import sys
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("""
╔════════════════════════════════╗
       STAG PB7 ACCESS NODE
╠════════════════════════════════╣

[1] Generate Certificate
[2] View Certificate
[3] Verify Integrity
[4] Archive Search
[5] System Status
[6] Exit

╚════════════════════════════════╝
""")


while True:

    clear()
    banner()

    command = input("COMMAND: ")

    if command == "1":
        subprocess.run([sys.executable, "generator.py"])

    elif command == "2":
        subprocess.run([sys.executable, "viewer.py"])

    elif command == "3":
        subprocess.run([sys.executable, "verifier.py"])

    elif command == "4":
        subprocess.run([sys.executable, "archive_search.py"])

    elif command == "5":

        clear()

        print("""
╔════════════════════════════════╗
        STAG PB7 STATUS
╠════════════════════════════════╣

GENERATOR:
        🟢 ONLINE

VIEWER:
        🟢 ONLINE

VERIFIER:
        🟢 ONLINE

ARCHIVE CORE:
        🟢 ONLINE

SEARCH ENGINE:
        🟢 ONLINE


PB7 SYSTEM:
        OPERATIONAL

CLEARANCE:
        LEVEL 7

╚════════════════════════════════╝
""")

        input("\nPRESS ENTER TO RETURN...")


    elif command == "6":

        clear()

        print("""
╔════════════════════════════════╗
       STAG PB7 NODE OFFLINE
╠════════════════════════════════╣

SESSION CLOSED

SECURE SHUTDOWN COMPLETE

╚════════════════════════════════╝
""")

        break


    else:
        print("INVALID COMMAND")
        input("PRESS ENTER...")