from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import ujson
import time 

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')

@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
        mydevice = "Video"
        myBit = False
        myPie = 3.14
        jsonSend={
            "Device":mydevice,
            "myBit":myBit,
            "myPie":myPie
            }
        await ws.send(ujson.dumps(jsonSend))
        s = ujson.loads(await ws.receive())
        print(s["Device"])
        print(s["myBit"])
        print(s["myPie"] * 2)
        time.sleep(5)
        
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
