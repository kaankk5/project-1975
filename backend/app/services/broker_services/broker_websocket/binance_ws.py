import websockets



class BinanceWebSocketClient:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.ws_uri = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@ticker"
        self.websocket = None


    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.ws_uri)
        except Exception as e:
            print(f"Failed to connect to WebSocket: {e}")

    async def disconnect(self):
        if self.websocket:
            await self.websocket.close()
            self.websocket = None

    async def receive_message(self):
        try:
            message = await self.websocket.recv()
            return message
        except Exception as e:
            print(f"Error receiving message from WebSocket: {e}")
            return None