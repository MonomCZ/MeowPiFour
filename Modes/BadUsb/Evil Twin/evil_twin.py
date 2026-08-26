import textwrap
import os 
import time 
import sys
import subprocess
import threading
from flask import Flask, render_template
from config import WIFI_PRESETS, ACTIVE_PRESET
preset = WIFI_PRESETS[ACTIVE_PRESET]

#For comands like stop procesess  -- "systemctl", "stop", "NetworkManager  
def cmd(comand, ignore_error = False): # ignore_error so the script dont fail if we are trying to turn off a function that isnt even on
    result = subprocess.run(comand, capture_output=True, text=True)
    if result.returncode !=0 and not ignore_error:
          print(f"ERROR: {result.stderr.strip()}")
          sys.exit(1)
    return result     

#Configruration
IFACE = "wlan1" #The exterbal wifi adapter that will be used to create the evil twin access point otherwise use "wlan0" for the internal wifi adapter.
PORTAL_IP = "192.168.4.1"
WIFI_SSID = preset["ssid"]
wifi_interface = "wlan1"

def stoping_services():
    print("Stoping all services...")
    cmd(["systemctl", "stop", "wpa_supplicant"], ignore_error=True)
    cmd(["systemctl", "disable", "wpa_supplicant"], ignore_error=True) # to turn off wpa_suplicatnt
    cmd(["systemctl", "stop", "NetworkManager"], ignore_error=True)
    cmd(["systemctl", "stop", "hostapd"], ignore_error=True)
    cmd(["systemctl", "stop", "dnsmasq"], ignore_error=True)
    print("Step 1 DONE... all services where stoped")


# Step 2 configuring interfaces
def configuring_interfaces():
     print("Configureting intarfeces")
     cmd (["ip", "link", "set", IFACE, "up"], ignore_error=True) # Turn on InterFace
     cmd (["ip", "addr", "flush", "dev", IFACE], ignore_error=True) # Flush InterFace
     cmd(["ip", "addr", "add", f"{PORTAL_IP}/24", "dev", IFACE], ignore_error=True) # to add IP to InterFace
     print("Step 2 DONE ... Configureting intarfeces was successful")


#Step 3 Rewriting config files (Configuring HOSTAPD and DNSMASQ)
config_hostapd = textwrap.dedent (f"""\
     interface={IFACE}
     driver=nl80211
     ssid={WIFI_SSID}
     hw_mode=g
     channel=6
     wmm_enabled=0
     auth_algs=1
     ignore_broadcast_ssid=0
""")

def configurating_hostapd():
     os.makedirs("/etc/hostapd", exist_ok=True)
     with open("/etc/hostapd/hostapd.conf", "w") as f:
          f.write(config_hostapd)

config_dnsmasq = textwrap.dedent(f"""\
     interface={IFACE}
     bind-interfaces
     dhcp-range=192.168.4.10,192.168.4.100,255.255.255.0,12h
     dhcp-option=3,192.168.4.1
     dhcp-option=6,192.168.4.1
     address=/#/192.168.4.1
     no-resolv
 """)

def configurating_dnsmasq():
     with open("/etc/dnsmasq.conf", "w") as f:
          f.write(config_dnsmasq)

def starting_services():
     #Useing definicions to configure.
     configurating_hostapd()
     configurating_dnsmasq()
     time.sleep(1)
     #Starting the servecises
     cmd(["systemctl", "unmask", "hostapd"], ignore_error=True) 
     cmd(["systemctl", "start", "hostapd"])
     time.sleep(2)
     cmd(["systemctl", "start", "dnsmasq"])

     print("All services are running DNSMASQ ... ON HOSTAPD... ON")