from typing import Any
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/login")
def login():
    return {'data': 'basarili'}
