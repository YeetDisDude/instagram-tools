import requests
import time
import json
import random
from colorama import Fore
import os

clear = lambda: os.system('cls')

while True:
    clear()
    menu = input(f"""
{Fore.LIGHTGREEN_EX}Instagram tools made by {Fore.LIGHTRED_EX}YeetDisDude#0001{Fore.RESET} | {Fore.LIGHTYELLOW_EX}Version 0.1{Fore.RESET}
{Fore.GREEN}[1]{Fore.RESET} - NGL link Spammer
{Fore.GREEN}[2]{Fore.RESET} - Check NGL validity\n""")
    if menu == "1":
        clear()
        url = input(f"{Fore.LIGHTRED_EX}Enter the ngl link:\n{Fore.LIGHTWHITE_EX}")
        message = input(f"{Fore.LIGHTRED_EX}Enter the message you want to send:\n{Fore.LIGHTWHITE_EX}")
        deviceids = ["1", "2", "3", "4", "5"]
        amount = input(f"{Fore.LIGHTRED_EX}how many times do you want to spam it | 1 for forever:\n{Fore.LIGHTWHITE_EX}{Fore.RESET}")
        randomdeviceid = random.choice(deviceids)
        payload = {
            "question": message,
            "deviceId": randomdeviceid
        }
        if amount == "1":
            sent = 0
            success = 0
            fail = 0
            while True:
                sent = sent+1
                forever = requests.post(url=url, json=payload)
                status = forever.status_code
                if forever:
                    success = success+1
                    print(f"{Fore.LIGHTCYAN_EX}Status code: {status}{Fore.RESET} | sent: {sent} | {Fore.LIGHTGREEN_EX}success: {success} | {Fore.RED}failed: {fail}{Fore.RESET}")
                else:
                    fail = fail+1
                    print(f"{Fore.LIGHTCYAN_EX}Status code: {Fore.RED}{status}{Fore.RESET} | sent: {sent} | {Fore.LIGHTGREEN_EX}success: {success} | {Fore.RED}failed: {fail}{Fore.RESET}")
        else:
            amountint = int(amount)
            sent = 0
            success = 0
            fail = 0
            for i in range(amountint):
                sent = sent+1
                r = requests.post(url=url, json=payload)
                status = r.status_code
                if r:
                    success = success+1
                    print(f"{Fore.LIGHTCYAN_EX}Status code: {status}{Fore.RESET} | sent: {sent} | {Fore.LIGHTGREEN_EX}success: {success} | {Fore.RED}failed: {fail}{Fore.RESET}")
                else:
                    fail = fail+1
                    print(f"{Fore.LIGHTCYAN_EX}Status code: {Fore.RED}{status}{Fore.RESET} | sent: {sent} | {Fore.LIGHTGREEN_EX}success: {success} | {Fore.RED}failed: {fail}{Fore.RESET}")
            print(f"{Fore.LIGHTMAGENTA_EX}Done.{Fore.RESET}")
            time.sleep(5)
    if menu == "2":
        clear()
        iguser = input(f"{Fore.LIGHTCYAN_EX}Enter the instagram user:\n")
        linktocheck = "https://ngl.link/" + iguser
        print(f"{Fore.LIGHTGREEN_EX}Checking link | {linktocheck}{Fore.RESET}{Fore.LIGHTCYAN_EX}")
        checklink = requests.get(url=linktocheck)
        if checklink:
            print(f"{Fore.LIGHTGREEN_EX}Link is Valid")
            time.sleep(2)
        else:
            print(f"{Fore.RED}Link is Invalid!")
            Fore.RESET
            time.sleep(2)
        
