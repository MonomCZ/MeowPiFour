main_file_name = "evil_twin"
start = 'run_eviltwin()'

options = {
    "presets": {"FREE WIFI": {"ssid": "FREE WIFI", "portal": "free_wifi.html"}, "STARBUCKS WIFI": {"ssid": "STARBUCKS WIFI", "portal": "starbucks.html"}},
    'WLAN': {"TP_LINK_ADAPTER": "wlan1", "INTERNAL_WIFI_CHIP": "wlan0"}
}

#If no value is selected, the default value will be used.
selected_options = {
    "SSID": "FREE WIFI",
    
    "PORTAL": "free_wifi.html"
     

}
