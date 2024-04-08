from app.repositories.user import UserRepository


class TradeService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
