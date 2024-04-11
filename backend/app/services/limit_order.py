from app.schemas.trade import TradeCreate


class LimitOrderService:

    @staticmethod
    async def check_market_buy(trade_create: TradeCreate) -> bool:
        if trade_create.buying_price or trade_create.selling_price:
            return False
        else:
            return True
