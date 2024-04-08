from fastapi import status

MESSAGE_KEY = "message"
ACCESS_KEY = "access_token"
TOKEN_TYPE_KEY = "token_type"
BEARER_RESPONSE_TEXT = "bearer"

ACCOUNT_NOT_FOUND_MESSAGE = "Account not found"
ACCOUNT_DELETED_MESSAGE = "Account deleted successfully"
USER_CREATED_MESSAGE = "User created successfully"
USER_SIGNUP_MESSAGE = "User signed up successfully"

# User data
USER_ID_TEXT = "user_id"
ACCOUNT_NAME_TEXT = "account_name"
BALANCE_TEXT = "balance"
# API Routes
REGISTER_ROUTE = "/register"
LOGIN_ROUTE = "/login"
ACCOUNTS_ROUTE = "/accounts"
ACCOUNTS_BY_NAME_ROUTE = "/accounts/{account_name}"
HOME_ROUTE = "/"
# VALIDATION
NOT_VALIDATE_CREDENTIALS_MESSAGE = "Could not validate credentials"
AUTH_HEADER_MISSING_MESSAGE = "Authorization header is missing"
INVALID_TOKEN_MESSAGE = "Invalid token"
USER_NOT_FOUND_MESSAGE = "User not found"
AUTH_TEXT = "Authorization"
BEARER_TEXT = "Bearer "
SUB_TEXT = "sub"

# Status
STATUS_401 = 401
STATUS_404 = 404
# HTTP Methods
GET_METHOD = "GET"
POST_METHOD = "POST"
PUT_METHOD = "PUT"
DELETE_METHOD = "DELETE"

# Error
INVALID_USERNAME_PASSWORD_TEXT = "Invalid username or password"
