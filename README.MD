# Write Up  
ESP32 Micropython Webserver project 

Stripped down version from.... 
https://www.donskytech.com/using-websocket-in-micropython-a-practical-example/  
.... Thanks for sharing :-)

Serves simple page from ESP32 and then makes socket connection to easily send and receive 10 variables in the background. Ideal template for fast development of IOT devices. Added JSON objects to easily send / receive variables and IO between ESP32 and browser.

Edit 'main.py' to define the variables to send to the browser, edit 'index.js' to edit the variables sent back to the ESP32.

Requires latest MicroPython firmware on ESP32, programmed and uploaded with 'Thonny'
