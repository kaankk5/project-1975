from fastapi import APIRouter
from app.services.trade import TradeService
from app.services.authentication import AuthService


class TradeController:

    def __init__(self, trade_service: TradeService, auth_service: AuthService):
        self.trade_service = trade_service
        self.auth_service = auth_service
        self.router = APIRouter()
        self.add_routes()


