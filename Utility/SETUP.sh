

sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv python3-pil i2c-tools
cd ~/MeowPiFour


sudo raspi-config nonint do_i2c 0

