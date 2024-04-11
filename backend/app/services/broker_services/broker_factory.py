
from app.services.broker_services.broker import BrokerType, Broker
from app.services.broker_services.binance import BinanceClient


class BrokerFactory:
    @staticmethod
    def create_client(broker_type: BrokerType) -> Broker:
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
            raise ValueError("Unsupported broker_services type")
