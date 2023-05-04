# Write Up  
ESP32 Micropython Webserver project 

Stripped down version from.... 
https://www.donskytech.com/using-websocket-in-micropython-a-practical-example/  
.... Thanks for sharing :-)

Serves simple page from ESP32 and then makes socket connection to send and receive 10 variables in the background. Ideal template for fast development of IOT devices. Added JSON objects to easily add variables and IO to messages between ESP32 and browser.

Just edit 'main.py' to define the variables to send to the browser, edit 'index.js' to edit the variables sent back to the ESP32.

Requires latest MicroPython firmware on ESP32, programmed and uploaded with 'Thonny'

To use:

Clone repository to local folder eg: documents\thonny\WebserMinumum

Open folder in Thonny

Change WiFi settings in Boot.py to your network 

Upload to ESP32 with Thonny

Click small red stop ICON to restart Micropython running on ESP

Note ESP IP address from Thonny log

Open Browser (Chrome works best) go to IP address port 5000  eg 192.168.0.68:5000
