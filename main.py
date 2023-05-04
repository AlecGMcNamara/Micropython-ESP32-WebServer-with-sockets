from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import ujson
import time 

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'
myCounter=1

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/ws')
@with_websocket
async def wsMessage(request, ws):
    while True:
        myDevice = "Video"  #set up test variables
        myBit = False
        global myCounter    #Use static integer
        jsonSend={          #create message
            "V1":myDevice,  #add variables to message
            "V2":myBit,
            "V3":myCounter,
            "V4":"",
            "V5":"",
            "V6":"",
            "V7":"",
            "V8":"",
            "V9":"",
            "V10":""
            }
        await ws.send(ujson.dumps(jsonSend))           #send serialized message to browser
        jsonReceive = ujson.loads(await ws.receive())  #receive serialized message from browser
        print(jsonReceive["V1"])    #log message variables
        print(jsonReceive["V2"])
        print(jsonReceive["V3"])
        print(jsonReceive["V4"])
        print(jsonReceive["V5"])
        print(jsonReceive["V6"])
        print(jsonReceive["V7"])
        print(jsonReceive["V8"])
        print(jsonReceive["V9"])
        print(jsonReceive["V10"])
        myCounter = jsonReceive["V3"]         #Save to variable
        myCounter +=1
        time.sleep(1)               #time between messages (1 second) can be 0.1 seconds!
        
# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)

# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass
