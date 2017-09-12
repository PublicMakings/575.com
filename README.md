# 575.com
A directory.
Ripe with abstract potential...
Open the folder!

### Before you Begin
We'll be using Ngrok to connect to tunnel into our network. I picked
this solution because I don't know too much about securing
[port-forwarding](https://www.howtogeek.com/66214/how-to-forward-ports-on-your-router/) 
on my router. This solution works, but might not be the best for a
permanent project with a stable URL.

### Hardware
1. Raspberry Pi
2. Power supply
3. Internet connection

### Files
Download the haiku folder and unzip it on your desktop.

### Software
To be installed on the RPi. May require sudo.
1. ```pip3 install pathlib```
2. ```pip3 install textstat```
3. ```pip3 install flask```
4. [ngrok](https://ngrok.com/download)
   
   pick Linux ARM
   
   requires GUI installation
   
   follow the instructions on the site for setup

### Activate!
1. Terminal session 1: ```python3 /path/to/haiku/read.py```
2. Terminal session 2: ```python3 /path/to/haiku/write.py```
3. Terminal session 3: ```./ngrok http 5000``` (assuming you are in the install directory)
4. Terminal session 4: ```./ngrok http 5001``` (assuming you are in the install directory)
      
   Plug that URL into your browser and you should see an
   internet-accessible webpage! Note: Ngrok will not allow you to do two
   simultaneous connections if you have a free account.
