#!usr/bin/env python

import requests
from colorama import Fore
import subprocess

subprocess.call("clear")

logo = """


 ██████ ██████   █████  ██     ██ ██      ███████ ██████  
██      ██   ██ ██   ██ ██     ██ ██      ██      ██   ██ 
██      ██████  ███████ ██  █  ██ ██      █████   ██████  
██      ██   ██ ██   ██ ██ ███ ██ ██      ██      ██   ██ 
 ██████ ██   ██ ██   ██  ███ ███  ███████ ███████ ██   ██ 

"""

print(f"{Fore.LIGHTGREEN_EX}{logo}")
print(
    f"{Fore.LIGHTWHITE_EX}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ {Fore.LIGHTCYAN_EX} Created by: {Fore.LIGHTRED_EX}Totenkopf {Fore.LIGHTWHITE_EX}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\n")


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = input("\nTarget website: ")

with open("/root/PycharmProjects/crawler/dirs.txt", "r") as directory:
    for line in directory:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print(f"\n{Fore.YELLOW}[+] Directory found --> {Fore.LIGHTCYAN_EX}{test_url}")



