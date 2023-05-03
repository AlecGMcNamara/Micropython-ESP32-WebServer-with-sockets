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
        s = ujson.loads(await ws.receive())
        print(s["V1"])
        print(s["V2"])
        print(s["V3"])
        myCounter = s["V3"]
        time.sleep(1)
        
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
