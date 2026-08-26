# MeowPiFour

Interface for managing python projects (with mostly pen testing projects inlcuded) for **Raspberry Pi Zero 2 W**.

The goal of this interface is to have an easy way to manage and use your (our) python projects with a nice and compact GPIO oled display controlled with 5 GPIO buttons.
Current inlcluded projects are:
- **Evil Twin Wi-Fi attack** (planned)
- **BadUSB** (planned)

Hardware needed for this project:
- **I2C OLED display**
- **GPIO buttons**
- **TP-Link Wi-Fi adapter** (Recommended for nicer use of the evil twin mode)


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
## Update

To update (pull from git) use MeowPiFour/Utility/UPDATE.sh
```bash
bash ~/MeowPiFour/Utility/UPDATE.sh
```