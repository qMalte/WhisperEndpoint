const WebSocket = require("ws");
const fs = require("fs");

const token = "<ONE OF YOUR API-KEYS>";
const enpointHost = "<IP OR HOSTNAME>";
const sourceFile = "<PATH TO AUDIO-FILE TO TRANSCRIPBE>";

const socket = new WebSocket(`ws://${enpointHost}:8765`);
 
socket.addEventListener('open', async (event) => {
    console.log("WebSocket Connection was opened!");
    const file = fs.readFileSync(sourceFile);
    socket.send(token);
    socket.send(file);
});

socket.addEventListener('message', (event) => {
    console.log(event.data);
});
