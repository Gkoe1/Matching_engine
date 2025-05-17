from book import Order, OrderBook
from logger import TradeLogger
from datetime import datetime
from decimal import Decimal

# Initialize logger and order book
trade_logger = TradeLogger()
order_book = OrderBook()
order_book.TradeLogger = trade_logger  # Attach logger to order book

# Add some orders
order1 = Order(order_id=1, side="buy", price=Decimal("100.5"), quantity=10, timestamp=datetime.now())
order2 = Order(order_id=2, side="sell", price=Decimal("100.5"), quantity=5, timestamp=datetime.now())
order3 = Order(order_id=3, side="sell", price=Decimal("101.0"), quantity=7, timestamp=datetime.now())
order4 = Order(order_id=4, side="buy", price=Decimal("99.5"), quantity=8, timestamp=datetime.now())

# Add orders to the book
order_book.add_order(order1)
order_book.add_order(order2)
order_book.add_order(order3)
order_book.add_order(order4)

# Cancel an order
try:
    order_book.cancel_order(3)
except Exception as e:
    print(f"Cancel error: {e}")

# Print order book snapshot
print("Order Book Snapshot:")
print(order_book)

# Print trade history
print("\nTrade History:")
for trade in trade_logger.get_trade_history():
    print(vars(trade))

# Print volume by price
print("\nVolume by Price:")
print(trade_logger.vol_by_price())

# Print VWAP
print("\nVWAP:")
print(trade_logger.get_vwap())