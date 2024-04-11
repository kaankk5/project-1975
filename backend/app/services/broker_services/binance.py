from app.services.broker_services.broker import Broker


class BinanceClient(Broker):
    async def get_stream_symbol(self, symbol: str):
        """GET STREAM SYMBOL :D"""
        pass
