# import threading
# import requests
from app.services.broker_services.broker import Broker
from app.services.broker_services.broker_websocket.binance_ws import BinanceWebSocketClient

from httpx import AsyncClient


class BinanceClient(Broker):
    BASE_URL = "https://api.binance.com/api/v3"
    PING_URL = "https://api.binance.com/api/v3/ping"
    EXCHANGE_INFO = "https://api.binance.com/api/v3/exchangeInfo"

    def __init__(self, client: AsyncClient, websocket_client: BinanceWebSocketClient):
        self.client = client
        self.websocket_client = websocket_client

    async def broker_side_validation(self, symbol: str) -> bool:
        connection_ok: bool = await self._check_connection()
        symbol_exists: bool = await self._check_symbol_exist(symbol)
        return connection_ok and symbol_exists

    async def _check_connection(self) -> bool:
        try:
            response = await self.client.get(self.PING_URL)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Anneniz sikildi daha exception class acicam aq {e}")
            return False

    async def _check_symbol_exist(self, symbol: str) -> bool:
        params = {"symbol": symbol}
        response = await self.client.get(self.EXCHANGE_INFO, params=params)
        return response.status_code == 200
