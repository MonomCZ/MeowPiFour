main_file_name = "evil_twin"
start = 'run_eviltwin()'

options = {
    "presets": {"FREE WIFI": {"ssid": "FREE WIFI", "portal": "free_wifi.html"}, "STARBUCKS WIFI": {"ssid": "STARBUCKS WIFI", "portal": "starbucks.html"}},
    'WLAN': ["TP_LINK_ADAPTER", "INTERNAL_WIFI_CHIP"]
}

selected_options = {
    "SSID": "FREE WIFI",
    'WLAN': "TP_LINK_ADAPTER"
}
