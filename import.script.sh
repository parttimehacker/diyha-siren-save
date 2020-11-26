#/usr/bin/bash
#
# import required python libraries

echo "Install Mqtt, psutil, pylint and screen"
sudo pip3 install paho-mqtt
sudo pip3 install psutil
sudo pip3 install pylint
sudo apt -y install screen

echo "Install Adafruit stuff"
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
cd ..
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git 
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install
cd ..
