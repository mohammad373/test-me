def _all_():
  import os
  import time
  import sys
  import time
  import subprocess
  from baner import baner
  try:
    import re
  except:
    time.sleep(1)
    print("[-] Pleass Install The Librery --> re")
    sys.exit()
  try:
    from colorama import Fore
  except:
    time.sleep(1)
    print("[-] Pleass Install The Librery --> colorama")
    sys.exit()
  try:
    import netifaces
  except:
    time.sleep(1)
    print("[-] Pleass Install The Librery --> netifaces")
    sys.exit()
  time.sleep(0.6)
  os.system("clear")
  baner()
  time.sleep(1)
  def result():
    my_list = input(Fore.LIGHTBLACK_EX + "\n[!] Pleass Enter Your New Mac And Name Netword : ").split(",")
    if len(my_list) != 2:
      time.sleep(1)
      print(Fore.RED + "\n[-] Your Data Hase The Problem !!!")
    try:
      nwe_mac = my_list[0]
    except:
      time.sleep(1)
      print(Fore.RED + "\n[-] Your Arguman Hase The Problem !!!")
      sys.exit()
    try:
      name_network = my_list[1]
    except:
      time.sleep(1)
      print(Fore.RED + "\n[-] Your Arguman Hase The Problem !!!")
      sys.exit()
    name_all_network = netifaces.interfaces()
    if name_network not in name_all_network:
      time.sleep(1)
      print(Fore.RED + "\n[-] Your Name Network Hase The Problem !!!")
      sys.exit()
    else:
      pass
    if re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:" , nwe_mac):
      time.sleep(1)
      print(Fore.RED + "\n[-] Your New Mac Hase The Problem !!!")
      sys.exit()
    subprocess.run(["sudo" , "ifconfig" , name_network , "down"] , shell=True)
    subprocess.run(["sudo" , "ipconfig" , name_network , "hw" , "ether" , nwe_mac])
    subprocess.run(["sudo" , "ifconfig" , name_network , "up"] , shell=True)
