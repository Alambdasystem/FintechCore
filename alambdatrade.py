from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order

class IBClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

class IBWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextOrderId = orderId

    def error(self, reqId, errorCode, errorString):
        print("Error {}: {}".format(errorCode, errorString))

def create_contract(symbol, sec_type, exchange, currency):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.exchange = exchange
    contract.currency = currency
    return contract

def create_order(action, quantity, order_type):
    order = Order()
    order.action = action
    order.totalQuantity = quantity
    order.orderType = order_type
    return order

def place_order(contract, order):
    app.placeOrder(app.nextOrderId, contract, order)

def buy_stock(symbol, quantity):
    contract = create_contract(symbol, "STK", "SMART", "USD")
    order = create_order("BUY", quantity, "MKT")
    place_order(contract, order)

def sell_stock(symbol, quantity):
    contract = create_contract(symbol, "STK", "SMART", "USD")
    order = create_order("SELL", quantity, "MKT")
    place_order(contract, order)

# Replace with your paper trading account credentials
account_id = "YOUR_ACCOUNT_ID"
host = "YOUR_HOST"
port = 7497
client_id = 1

app = IBClient(IBWrapper())
app.connect(host, port, client_id)

# Check if the connection is successfully established
if app.isConnected():
    app.run()

    # Once connected, you can place buy/sell orders
    # Example usage:
    buy_stock("AAPL", 10)
    sell_stock("AAPL", 5)

app.disconnect()
