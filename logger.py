#####   Trade recording & reporting utility functions   #####

# 1. Recording Trades
# 2. Retrieving full trade history
# 3. Aggregating volume by price level
# 4. Computing VWAP (Volume Weighted Average Price)


import json
from datetime import datetime
from book import *

#### TradeLogger class ####
class TradeLogger:
    def __init__(self):
        self._trades = []
        self._trade_map = {}

    def record_trade(self, trade: Trade):
        """ Record a trade """
        self._trades.append(trade)
        self._trade_map[trade.trade_id] = trade

    def get_trade_history(self):
        """ Return list of trades """
        # Return a tuple to prevent mutation of the internal list
        return tuple(self._trades)
    
    def vol_by_price(self):
        """ Aggregate volume by price level """
        volume_by_price = {}
        for t in self._trades:
            if t in self._trades:
                volume_by_price.setdefault(t.price, 0)
                vol_by_price[t.price] += t.quantity 
            return volume_by_price
    
    def get_vwap(self):
        """ calculates vwap """
        total_value = sum(t.price*t.quantity for t in self._trades)
        total_qty = sum(t.quantity for t in self._trades)
        return (total_value/total_qty) if total_qty > 0 else 0.0

        