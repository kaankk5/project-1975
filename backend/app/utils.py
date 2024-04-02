import bcrypt
from typing import Any, Dict
import jwt
from datetime import datetime, timedelta
from app.config import Settings
from fastapi import HTTPException


def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def set_password(user_data_dict: Dict[str, Any], hashed_password: str) -> Dict[str, Any]:
    user_data_dict['password'] = hashed_password
    return user_data_dict



def create_access_token(user_id: int) -> str:
    access_token_expires = timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRATION_MINUTES)
    access_token_payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + access_token_expires
    }
    access_token = jwt.encode(
        access_token_payload,
        Settings.JWT_SECRET_KEY,
        algorithm=Settings.JWT_ALGORITHM
    )
    return access_token



def decode_jwt_token(token: str):
        decoded_token = jwt.decode(token, Settings.JWT_SECRET_KEY, algorithms=[Settings.JWT_ALGORITHM])
        return decoded_token
    # except jwt.ExpiredSignatureError:
    #
    #     raise HTTPException(status_code=401, detail="Token has expired")
    # except jwt.InvalidTokenError:
    #     print('error 2')
    #     raise HTTPException(status_code=401, detail="Invalid token")