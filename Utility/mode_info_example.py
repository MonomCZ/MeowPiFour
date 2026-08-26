#each "mode" has a Name_info.py file which will tell the system how it works whot stuff can be changed etc
#
#it will be like this

main_file_name=evil_twin.py #tells the system what mode to importls ~/.ssh/

start = run_eviltwin(ssid,captive_portal_type) #this start tell the system what will happen when you start the mode

options = {ssid: ["Free WiFi", "McDonalds", "Starbucks"],
           captive_portal_type: ["Default", "McDonalds", "Starbucks"]} #this tell the system what options can be changed and what the options are

