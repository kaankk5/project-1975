from fastapi import FastAPI, Depends
from app.repositories.db import init_db
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.services.trade import TradeService
from app.services.authentication import AuthService
from app.controllers.trade import TradeController
from app.controllers.user import UserController
from app.controllers.authentication import AuthController
from app.services.broker_services.binance import BinanceClient
from app.services.broker_services.broker_websocket.binance_ws import BinanceWebSocketClient
from httpx import AsyncClient

# from app.controllers.user import router as user_router
# from app.controllers.auth_controller import auth_router

app = FastAPI()


#
# @app.on_event("startup")
# async def startup_event():
#     # user_controller = UserController()
#
#     user_controller = UserController()
#     user_controller.user_repo = Depends(UserService)
#
#     app.include_router(user_router)
#     await init_db()
# #
@app.on_event("startup")
async def startup_event():
    # User Repository
    user_repository = UserRepository()
    # Request
    async_client = AsyncClient()

    # Broker ws
    binance_ws_client: BinanceWebSocketClient = BinanceWebSocketClient()


    # Broker Services
    binance_client: BinanceClient = BinanceClient(async_client,binance_ws_client)
    # kraken_client: Kraken = Kraken()

    # Services
    user_service: UserService = UserService(user_repository)
    auth_service: AuthService = AuthService()
    trade_service: TradeService = TradeService(user_repository, binance_client)

    # Controller
    user_controller_instance: UserController = UserController(user_service, auth_service)
    auth_controller_instance: AuthController = AuthController(auth_service)
    trade_controller_instance: TradeController = TradeController(trade_service, auth_service)

    # Routes
    app.include_router(user_controller_instance.router)
    app.include_router(auth_controller_instance.router)
    app.include_router(trade_controller_instance.router)
    # await init_db()
