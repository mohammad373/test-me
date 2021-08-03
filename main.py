import arp_spoof
import not_internet_for_target
import os
import sys
import time
from baner import baner
os.system("clear")
baner()
time.sleep(0.6)
print(Fore.LIGHTBLACK_EX + "\n[1] ~ ARP Spoofer")
time.sleep(0.3)
print(Fore.LIGHTBLACK_EX + "[2] ~ Bloack Target For Internet")
number = int(input(Fore.LIGHTBLACK_EX + "\nPleass Enter Your Number : ")
if number == 1:
             arp_spoof._all_()
if number == 2:
             not_internet_for_target._all_()
