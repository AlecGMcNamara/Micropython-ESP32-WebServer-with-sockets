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
    
    var myText = "";
    var myBool = false; 
    
    myText = jsonReceived["Device"];
    testNumber = jsonReceived["myPie"];
    myBool = jsonReceived["myBit"]
    
    document.getElementById("myMessage").innerHTML = testNumber;

    myText = "From Browser";
    myBool = true;
    testNumber += testNumber;

    //set up JSON message before sending mesage to server
    testNumber++;
    var jsonSend = {"Device": myText,
                    "myPie": testNumber,
                    "myBit": myBool};

    websocket.send(JSON.stringify(jsonSend));   
}

function sendMessage(message) {
  websocket.send(message);
}
