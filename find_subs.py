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
print(f"{Fore.LIGHTWHITE_EX}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ {Fore.LIGHTCYAN_EX} Created by: {Fore.LIGHTRED_EX}Totenkopf {Fore.LIGHTWHITE_EX}/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\n")

def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass

target_url = input("\nTarget website: ")

with open("/root/PycharmProjects/crawler/wordlist.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        if "." in word:
            test_url = word + target_url
        response = request(test_url)
        if response:
            print(f"\n{Fore.YELLOW}[+] Subdomain found --> {Fore.LIGHTGREEN_EX}{test_url}")



