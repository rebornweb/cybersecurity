#Light Kali with just tools

#Start docker
#Start container
#docker run -tid -p 80 -v $PWD/:/home --name kali -d kalilinux/kali-rolling

#Jump in container
docker exec -it kali bash
#Ref https://www.kali.org/tools/
#RUN apt update && apt -y install kali-linux-headless && apt install -y kali-tools-top10 && apt install -y bind9-dnsutils

#Copy container to new image then bind local volumn
#docker commit 86e1a14e53e3 kali_updated

#docker run -ti -v "$PWD/somedir":/somedir kali_updated /bin/bash