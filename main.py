import arp_spoof
import not_internet_for_target
import mac_changer
import os
import sys
import time
try:
  from colorama import Fore
except:
  time.sleep(1)
  print("[-] Pleass Install The Librery --> colorama")
  sys.exit()

from baner import baner
os.system("clear")
baner()
time.sleep(0.6)
print(Fore.LIGHTBLACK_EX + "\n[1] ~ ARP Spoofer")
time.sleep(0.3)
print(Fore.LIGHTBLACK_EX + "[2] ~ Bloack Target For Internet")
time.sleep(0.3)
print(Fore.LIGHTBLACK_EX + "[3] ~ MAC Changer")
time.sleep(1)
number = int(input(Fore.LIGHTBLACK_EX + "\nPleass Enter Your Number : "))
if number == 1:
    arp_spoof._all_()
if number == 2:
    not_internet_for_target._all_()
if number == 3:
    mac_changer._all_()
else:
    print(Fore.RED + "\n[-] Your Number Not Found !!!")
    sys.exit()

