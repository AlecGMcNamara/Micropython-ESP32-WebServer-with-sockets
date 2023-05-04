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
    
    myText = jsonReceived["V1"];   //get variables from message
    myBool = jsonReceived["V2"];
    myCounter = jsonReceived["V3"]
    
    document.getElementById("V1").innerHTML = myText;     //display variables on webpage
    document.getElementById("V2").innerHTML = myBool;
    document.getElementById("V3").innerHTML = myCounter;
    document.getElementById("V4").innerHTML = jsonReceived["V4"];
    document.getElementById("V5").innerHTML = jsonReceived["V5"];
    document.getElementById("V6").innerHTML = jsonReceived["V6"];
    document.getElementById("V7").innerHTML = jsonReceived["V7"];
    document.getElementById("V8").innerHTML = jsonReceived["V8"];
    document.getElementById("V9").innerHTML = jsonReceived["V9"];
    document.getElementById("V10").innerHTML = jsonReceived["V10"];

    myText = "From Browser";  // create dummy variables
    myBool = true;
    myCounter++;

    //set up JSON message before sending mesage to server
    var jsonSend = {"V1": myText,     // add variables to the message
                    "V2": myBool,
                    "V3": myCounter,
                    "V4": "",                    
                    "V5": "",
                    "V6": "",
                    "V7": "",
                    "V8": "",
                    "V9": "",
                    "V10": ""
                    };

    websocket.send(JSON.stringify(jsonSend));   //send serialized message to ESP32
}

function sendMessage(message) {
  websocket.send(message);
}
