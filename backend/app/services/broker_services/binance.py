from app.services.broker_services.broker import Broker


class BinanceClient(Broker):
    async def get_stream_symbol(self, symbol: str):
        print(31)
        pass

    async def check_symbol(self, symbol: str):
        pass

