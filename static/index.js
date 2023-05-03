// WebSocket support
var targetUrl = `ws://${location.host}/ws`;
var websocket;
window.addEventListener("load", onLoad);

function onLoad() {
  initializeSocket();
}

function initializeSocket() {
  console.log("Opening WebSocket connection MicroPython Server...");
  websocket = new WebSocket(targetUrl);
  websocket.onopen = onOpen;
  websocket.onclose = onClose;
  websocket.onmessage = onMessage;
}
function onOpen(event) {
  console.log("Starting connection to WebSocket server..");
}
function onClose(event) {
  console.log("Closing connection to server..");
  setTimeout(initializeSocket, 2000);
}

function onMessage(event) {
  var jsonReceived = JSON.parse(event.data);
    
    myText = jsonReceived["V1"];
    testNumber = jsonReceived["V2"];
    myBool = jsonReceived["V3"]
    
    document.getElementById("myMessage").innerHTML = testNumber;

    myText = "From Browser";
    myBool = true;
    testNumber += testNumber;

    //set up JSON message before sending mesage to server
    testNumber++;
    var jsonSend = {"V1": myText,
                    "V2": testNumber,
                    "V3": myBool,
                    "V4": "",                    
                    "V5": "",
                    "V6": "",
                    "V7": "",
                    "V8": "",
                    "V9": "",
                    "V10": ""
                    };

    websocket.send(JSON.stringify(jsonSend));   
}

function sendMessage(message) {
  websocket.send(message);
}
