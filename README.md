# Matching_engine

A personal project that simulates a simplified financial order matching engine. This engine models the core mechanics of a limit order book, including order entry, matching, cancellation, and trade logging. It is designed for learning, experimentation, and as a foundation for building more advanced trading systems.

---

## Features

- **Limit Order Entry:**  
  Add buy and sell limit orders with price, quantity, and timestamp.

- **Order Matching:**  
  Matches incoming orders against the order book using price-time priority.

- **Order Cancellation:**  
  Cancel open (unfilled) orders by order ID.

- **Trade Logging:**  
  Records all executed trades with details such as order IDs, price, quantity, and timestamp.

- **Trade History:**  
  Retrieve a full history of all trades executed by the engine.

- **Volume by Price Aggregation:**  
  Aggregates and reports traded volume at each price level.

- **VWAP Calculation:**  
  Computes the Volume Weighted Average Price (VWAP) for all trades.

- **Order Book Snapshot:**  
  Provides a snapshot of the current state of the order book, including best bid/ask and depth.

---

## Limitations

- **No Persistence:**  
  All data is stored in memory; restarting the engine will lose all orders and trades.

- **No Concurrency:**  
  The engine is not thread-safe and does not support concurrent order entry or matching.

- **No Market Orders:**  
  Only limit orders are supported; market orders and advanced order types are not implemented.

- **No Partial Fills Across Multiple Orders:**  
  Matching logic is basic and may not handle complex partial fills or advanced matching scenarios.

- **No Real-Time Data Feeds or APIs:**  
  There is no external API or real-time data feed integration.

- **Minimal Error Handling:**  
  Error handling is basic and may not cover all edge cases.

---

## Contribution & Learning

I am open to corrections, suggestions, and contributions!  
If you spot any issues, have ideas for improvements, please open an issue or submit a pull request.

I would also be glad for any opportunity for more advanced learning or mentorship in trading systems, matching engines, or related fields.

---

## Getting Started

1. Clone the repository.
2. Install Python 3.8+.
3. Run the `main.py` script to see the engine in action.

---

Thank you for checking out this project!
