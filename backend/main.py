from fastapi import FastAPI
from app.routers import login

app = FastAPI()
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str,age:int):

    return {"message": f"Hello {name}"}
