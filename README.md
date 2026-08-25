# MeowPiFour

A small project for testing and using many different gadget modes compatible with the **Raspberry Pi Zero 2 W**.

The goal of this project is to display hacking gadgets using an I2C OLED display and buttons connected to the **Raspberry Pi Zero 2** via GPIO pins:
- Evil Twin Wi-Fi attack
- BadUSB

Hardware needed for this project:
- I2C OLED display
- GPIO buttons
- TP-Link Wi-Fi adapter (Recommended)


---

## Install 

Install on a clean install of rpi os 32bit lite with:
```bash
sudo apt install -y git
cd ~
git clone https://github.com/MonomCZ/MeowPiFour.git
cd MeowPiFour
bash Utillity/SETUP.sh
```
## Update | `UPDATE.sh`

To update (pull from git) use MeowPiFour/Utility/UPDATE.sh
```bash
bash ~/MeowPiFour/Utility/UPDATE.sh
```