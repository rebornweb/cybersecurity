#Light Kali with just tools

#Start docker daemon
#Start container
#docker run -tid -p 80 -v $PWD/:/home --name kali -d kalilinux/kali-rolling

#Jump in container
docker exec -it kali bash
#Ref https://www.kali.org/tools/
#RUN apt update && apt -y install kali-linux-headless && apt install -y kali-tools-top10 && apt install -y bind9-dnsutils

#Optional
#Make a new user and add to new docker group to enable the use of sudo
# useradd newuser
# groupadd docker
# usermod -aG docker newuser
#Add user to sudoers
#usermod -aG sudo newuser
#docker exec -it --user [username] [container] bash

#Copy container to make new image then bind local volumn
#docker commit 86e1a14e53e3 kaliupdated:cybersec

#Start new container
#docker run --privileged -tid -p 80 -v $PWD/:/home --name kali -d rebornweb/kaliupdated:cybersec
