import whisper
import asyncio
import websockets
import urllib.parse

API_KEYS = [
    "<GENERATE A CUSTOM STRING AS API-KEY>"
]

def transcribe(path):
    model = whisper.load_model("medium")
    options = {
        "language": "German",
        "fp16": False
    }
    res = model.transcribe(path, **options)
    text = res["text"]
    return text

async def handleRequest(websocket):
    print("New Request in Progress")

    # Authorization
    token = await websocket.recv()
    if token in API_KEYS:
        print("Client Authorized")
        await websocket.send("{ 'state': 'In Progress' }")
        message = await websocket.recv()
        with open("temp.wav", "wb") as file:
            file.write(message)
        text = transcribe('temp.wav')
        await websocket.send("{ 'state': 'Done', 'message': " + text + "}")
        print("Transcribe Success")
    else:
        print("Client is Unauthorized")
        await websocket.send("{ 'state': 'Access Denied' }")
    
    print("Request Done")

async def handler(websocket):
    await handleRequest(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Der Whisper-Endpunkt wurde unter Port: 8765 gestartet!")
        await asyncio.Future()

asyncio.run(main())