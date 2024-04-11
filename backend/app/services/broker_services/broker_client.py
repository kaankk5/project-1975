from abc import ABC, abstractmethod
from enum import Enum


class BrokerClient(ABC):

    @abstractmethod
    async def get_stream_symbol(self, symbol: str):
        """GET STREAM SYMBOL :D"""
        pass
