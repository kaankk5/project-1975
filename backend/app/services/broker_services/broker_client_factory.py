from app.services.broker_services.broker_client import BrokerType, BrokerClient
from app.services.broker_services.binance_client import BinanceClient


class BrokerClientFactory:
    @staticmethod
    def create_client(broker_type: BrokerType) -> BrokerClient:
        if broker_type == BrokerType.BINANCE:
            return BinanceClient()
        elif broker_type == BrokerType.KRAKEN:
            return 'KrakenClient()'
        elif broker_type == BrokerType.KRAKEN:
            return 'KrakenClient()'
        elif broker_type == BrokerType.KRAKEN:
            return 'KrakenClient()'
        elif broker_type == BrokerType.KRAKEN:
            return 'KrakenClient()'

        else:
            raise ValueError("Unsupported broker type")
