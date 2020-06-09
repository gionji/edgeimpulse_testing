# Questo e'
# https://docs.edgeimpulse.com/reference#remote-management



import asyncio
import websockets
import json

SERVER = 'wss://remote-mgmt.edgeimpulse.com'
API_KEY = 'ei_5d60c246c831b7939ba2dd768ebd3996d22601587bd576ec08de9890ad8c0fd4'


import websocket


hello = {
    "hello": {
        "version": 2,
        "apiKey": "ei_238fae...",
        "deviceId": "unique device id",
        "deviceType": "DISCO_L475VG_IOT01A1",
        "connection": "ip",
        "sensors": [
            { 
                "name": "Built-in accelerometer", 
                "maxSampleLengthS": 300,
                "frequencies": [ 62.5, 100 ]
            }
        ]
    }
}




try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        data = json.dumps(hello)

        print('\n' + data + '\n')

        ws.send( data )
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp( SERVER ,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
