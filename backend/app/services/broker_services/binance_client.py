from app.services.broker_service.broker_client import BrokerClient


class BinanceClient(BrokerClient):
    async def get_stream_symbol(self, symbol: str):
        """GET STREAM SYMBOL :D"""
        pass
