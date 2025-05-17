#####Order, Trade, Exception ######

from collections import deque
from datetime import datetime
from decimal import Decimal 
from typing import Deque, List, Optional, Union

class Order:
    """ Represent a limit order """
    def __init__(self, order_id: Union[str, int], side: str, price: Union[float, Decimal], quantity: int, timestamp: Optional[datetime] = None):
        self.order_id=order_id
        self.side=side
        self.price=price
        self.quantity=quantity
        self.timestamp=timestamp
        #status flags
        self._filled= False
        self._canceled = False
    
    def __repr__(self):
        return f'Order Received: {order_id} {side} {price} {quantity} {timestamp} {filled}'
    
    def reduce(self, quantity_filled):
        self.quantity -= quantity_filled
        if self.quantity == 0:
            print(f'Order: {self.quantity} filled')
            return self._filled = True
    
    def is_filled(self):
        """Check if order is filled"""
        return self._filled
    
    def mark_canceled(self):
        """ mark order as cancelled """
        self._canceled = True
        self._filled = True

    


#### Trade class  #######

class Trade:
    def __init__(self, buy_order_id: Union[str, int], sell_order_id: [str, int], price: Decimal, quantity: int, timestamp: Optional[datetime] = None):
        self.buy_order_id=buy_order_id
        self.sell_order_id=sell_order_id
        self.price=price
        self.quantity=quantity
        self.timestamp=timestamp
