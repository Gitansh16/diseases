import asyncio
import websockets

async def handle_connection(websocket, path):
    print(f"Client connected from {websocket.remote_address}")

    try:
        while True:
            message = await websocket.recv()
            response = f"Server received: {message}"

            print(f"{websocket.remote_address}: {message} | {response}")

            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print(f"Connection with {websocket.remote_address} closed")

start_server = websockets.serve(handle_connection, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

