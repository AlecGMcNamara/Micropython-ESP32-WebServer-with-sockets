from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import ujson
import time
import uasyncio

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'
myCounter=0

async def sendM(ws):   #send websocket message to web page
    while True:
        myDevice = "Video"
        myBit = False
        global myCounter
        jsonSend={
            "V1":myDevice,
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
        await ws.send(ujson.dumps(jsonSend))
        await uasyncio.sleep(.1)   #delay between sending messages to Browser
       
async def recM(ws):     #receive messages from Browser
    while True:
        jsonReceice = ujson.loads(await ws.receive())
        #print(jsonReceice["V1"])   #print to log
        #print(jsonReceice["V2"])
        #print(jsonReceice["V3"])
        global myCounter
        myCounter = jsonReceice["V3"]  #save to variable
        myCounter +=1

async def call_tasks(ws):      #Manage tasks 
    await uasyncio.gather(sendM(ws), recM(ws))

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')


@app.route('/ws')
@with_websocket
async def wsMessage(request, ws):
    uasyncio.run(call_tasks(ws))         #start tasks when connection made
            
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

