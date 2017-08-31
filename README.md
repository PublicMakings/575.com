# 575.com
A Rasberry Pi-based webserver that takes poetry submissions and converts them to nested filepaths.

### Hardware
1. Raspberry Pi
2. Power supply
3. Internet connection

### Files
Download the haiku folder and stick it on your desktop. I don't think the location makes a difference.

### Software
may require sudo
1. ```pip3 install pathlib```
2. ```pip3 install textstat```
3. ```pip3 install flask```
4. [ngrok](https://ngrok.com/download)
   
   pick Linux ARM
   
   requires GUI installation
   
   follow the instructions on the site for setup

### Activate!
1. ```python3 /path/to/haiku/app.py```
2. ```./ngrok 5000``` (we use 5000 to match up with Flask)
3. Ngrok will pop a window with a URL.
   
   Plug that URL into your browser and you should see an internet-accessible webpage!
