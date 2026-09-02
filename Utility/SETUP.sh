

sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv python3-pil i2c-tools python3-flask hostapd dnsmasq iptables python3-pil flask render_template
#fonts i put it seperate cause i can idc
sudo apt install -y fonts-firacode fonts-jetbrains-mono fonts-hack fonts-terminus ttf-mscorefonts-installer

cd ~/MeowPiFour

#sets up the python path for the project (i think so atleast)
echo 'PYTHONPATH=/home/avsie/MeowPi-3' | sudo tee -a /etc/environment
source /etc/environment
#installs pip packages
pip3 install --break-system-packages adafruit-blinka adafruit-circuitpython-ssd1306


sudo raspi-config nonint do_i2c 0

#fix for a rare issue i once had with ssh
grep -qxF 'export TERM=xterm-256color' ~/.bashrc || echo 'export TERM=xterm-256color' >> ~/.bashrc

cat << 'EOF'
                           ╱|、
                          (˚ˎ 。7
                          |、˜〵        
                          じしˍ,)ノ
EOF
echo "Setup complete :3"