from abc import ABC, abstractmethod
from enum import Enum


class BrokerName(Enum):
    BINANCE = "Binance"
    KRAKEN = "Kraken"


class Broker(ABC):

    @abstractmethod
    async def broker_side_validation(self) -> bool:
        """GET STREAM SYMBOL :D"""
        pass
    #
    # @abstractmethod
    # async def check_symbol(self, symbol: str):
    #     """GET STREAM SYMBOL :D"""
    #     pass
