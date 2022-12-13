import websockets
import asyncio

port = 7890

print('Start server on port=' + str(port))


async def echo(websocket, path):
    # print('A client just connected')
    try:
        async for message in websocket:
            print('Received msg from client:' + message)
            await websocket.send("Server Back message:" + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(e)


start_server = websockets.serve(echo, "192.168.10.119", port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
