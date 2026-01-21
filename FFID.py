import os
import time

def priyanshu_banner():
    os.system('clear')
    print("\033[1;36m")
print(" ███████╗███████╗██╗██████╗ ██████╗  █████╗ ███╗   ██╗")
print(" ██╔════╝██╔════╝██║██╔══██╗██╔══██╗██╔══██╗████╗  ██║")
print(" █████╗  █████╗  ██║██║  ██║██████╔╝███████║██╔██╗ ██║")
print(" ██╔══╝  ██╔══╝  ██║██║  ██║██╔══██╗██╔══██║██║╚██╗██║")
print(" ██║     ██║     ██║██████╔╝██████╔╝██║  ██║██║ ╚████║")
print(" ╚═╝     ╚═╝     ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝")
print("\033[1;31m         --- FREE FIRE ID BAN REPORT TOOL ---")
print("\033[1;32m      Created by: Priyanshu Gupta (The Black Hat)")
print("\033[1;36m------------------------------------------------------\033[0m")


def start_ban():
    priyanshu_banner()
    # Target ki details lena
    target_id = input("\033[1;33m[+] Enter Target UID (e.g. 12345678): \033[0m")
    
    print(f"\n\033[1;31m[*] Connecting to Garena Anti-Cheat Server...")
    time.sleep(2)
    print(f"\033[1;32m[*] ID Found: {target_id} (Level: 65, Region: IND)")
    time.sleep(1)

    print(f"\n\033[1;33m[!] Starting Mass Reporting Sequence...")
    # Reporting simulation
    for i in range(1, 101):
        print(f"\033[1;32m[✓] Report #{i} Sent: Reason - Modified Files (OB44 Hack)")
        time.sleep(0.1)

    print("\n\033[1;31m[!] ALL REPORTS SENT SUCCESSFULLY!")
    print("\033[1;33m[*] ID STATUS: Under Review (Ban in 24-48 Hours)")

if __name__ == "__main__":
    start_ban()
