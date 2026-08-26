#each "mode" has a Name_info.py file which will tell the system how it works what stuff can be changed etc
#
#it will be like this

main_file_name=evil_twin.py #tells the system what file to import

start = run_eviltwin(ssid,captive_portal_type) #this start tell the system what will happen when you start the mode

options = {ssid: ["Free WiFi", "McDonalds", "Starbucks"],
           captive_portal_type: ["Default", "McDonalds", "Starbucks"]} #this tells the system what options can be changed and what the options are

selected_options = {ssid: "Free WiFi", captive_portal_type: "Default"} #this tells the system what the selected options are