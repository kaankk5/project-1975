from fastapi import FastAPI, Depends
from app.repositories.db import init_db
from app.services.user import UserService
from app.controllers.user import UserController
from app.repositories.user import UserRepository
from app.services.authentication import AuthService
from app.controllers.authentication import AuthController

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
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    auth_service = AuthService()
    user_controller_instance = UserController(user_service,auth_service)

    auth_controller_instance = AuthController(auth_service)

    app.include_router(user_controller_instance.router)
    app.include_router(auth_controller_instance.router)
    # await init_db()
