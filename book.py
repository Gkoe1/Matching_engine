#########   SIMPLIFIED ORDER MATCHING ENGINE    #############


##########  OrderBook Core Classes (Entry, Match, Cancel)   ##########
######################################################################
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


######  OrderBook Class    ##########

class OrderBook:
    """
        matching engine
    """
    def __init__(self):

        ##map order_id 
        self._order_map: Dict[Union[str, int], Order] = {}
        #list of trades
        self._trades: List[Trade] = []

    def add_order(self, order: Order):
        ## Validating Order
        if order.quantity <= 0 or order.price <= 0:
            raise ValueError("Price and Quantity must be positive")
        if order.order_id in self._order_map:
            raise ValueError(f"Duplicate Order: {order.order_id}")
        
        
        ##match order
        self._match_order(order)
        ## Enqueue Remainder
        if order.quantity > 0 and not order.is_filled():
            self._enqueue_order(order)
            self._order_map[order.order_id] = order

        
    def cancel_order(self, order_id: Union[str,int]):
        """
        Cancels Order by ID
        """
        order = self._order_map.get(order_id)
        if not order or order.is_filled():
            raise keyError{f' Cannot cancel order: {order_id}'}

        #Remove from book
        side_book = self.bids if order.side == "buy" else self.asks
        queue = side_book(order.price)
        queue.remove(order)
        order.mark_canceled()
        del self._order_map[order_id]

        if not queue:
            del side_book[order.price]

    
    def get_best_bid(self):
        """returns highest bid price """
        return max(self.bids) if self.bids else None

    def get_best_ask(self):
        """return lowest ask price """
        return min(self.asks) if self.asks else None

    def get_snapshot(self, depth: Optional[int]=None):

        def extract(side_book: Dict[Decimal, Deque[Order]], reverse: bool):
            levels = sorted(side_book.items(), key=lambda x: x[0], reverse=reverse)
            result - []
            for price , queue in levels(:depth):
                total = sum(o.quantity for o in queue)
                result.append((price, total))
            return result
        return {
            "bids": extract(self.bids, True),
            "asks": extract(self.ask, False)
        }

    def get_trade_history(self):
        """ return list of trades """
        return List(self._trades)


    def _match_order(self, incoming: Order):
        
        opposite = self.asks if incoming.side == "buy" else self.bids

        ## crossing condition
        def crosses(price: Decimal):
            if incoming.side == "buy":
                return incoming.price >= price
            else:
                return incoming.price <= price
            
        while incoming.quantity > 0 and opposite:
            best_price = min(opposite) if incoming.side == "buy" else max(opposite)
            if not crosses(best_price):
                break
            queue = opposite[best_price]
            resting = queue[0]
            fill_quantity = min(incoming.quantity, resting.quantity)

            incoming.reduce(fill_quantity)
            resting.reduce(fill_quantity)
            #record trade
            trade = Trade(
                buy_order_id=(incoming.order_id if incoming.side == "buy" else resting.order_id),
                sell_order_id=(resting.order_id if incoming.side == "buy" else incoming.order_id),
                price=best_price,
                quantity=fill_quantity,
            )

            ##append to local history
            self._trades.append(trade)
            # record trades
            self.TradeLogger.record_trade(trade)
            ##Cleaning up 
            if resting.is_filled():
                queque.popleft()
                del self._order_map[resting.order_id]
            if not queue:
                del opposite[best_price]

    
    def _enqueue_order(self, order: Order):
        side_book = self.bids if order.side == "buy" else self.asks
        if order.price not in side_book:
            side_book[order.price] = deque()
        side_book[order.price].append(order)

    def __repr__(self):
        return f"OrderBook: {self.get_snapshot()}"
    def __str__(self):
        return f"OrderBook: {self.get_snapshot()}"
    def __len__(self):
        return len(self._order_map)
    