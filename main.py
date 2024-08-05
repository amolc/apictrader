from ctrader import Ctrader
from time import sleep



server="13.248.185.194" # - Host name: (Current IP address 168.205.95.20 can be changed without notice)
account="demo.pepperstone.3965339" #  - SenderCompID: live.icmarkets.1104926
password="98814000" # - The password you configured

print("server", server)
print("account", account)
print("password", password)

api = Ctrader(server,account,password)
# api = Ctrader(server, account, password)

sleep(5)



def check_connection(stock):
    checkConnection = api.isconnected()
    print("Is Connected?: ", checkConnection)
    sleep(1)
    positions = api.positions()
    api.subscribe(stock)
    sleep(1)
    prices = api.quote(stock)
    sleep(1)
    # print("price",price)
    if stock in prices:
        price_info = prices["XAUUSD"]
        print(price_info)
    bidprice = price_info['bid'] 
    print("bidprice", bidprice)
    sleep(1)
    symbol = stock
    volume =7 # position size:
    stoploss =  round(bidprice - 0.00010,6)
    takeprofit = round(bidprice + 0.00010,6)
    # id = api.buyLimit(symbol, volume, bidprice)
    id = api.buy(symbol, volume, stoploss, takeprofit)
    print(f"Position: {id}")



    # api.logout()

#---------------------List Positions-----------------------#
def list_all_position():
    positions = api.positions()
    print(positions)

def buy_position(stock):
    # Buy position
    api.subscribe(stock)
    sleep(1)
    price = api.quote(stock)
    sleep(1)
    print(price, "priceprice")
    price = price['bid'] 
    print("price", price)
    sleep(1)
    symbol = stock
    volume =7 # position size:
    stoploss =  round(price - 0.00010,6)
    takeprofit = round(price + 0.00010,6)
    # id = api.buyLimit(symbol, volume, price)
    id = api.buy(symbol, volume, stoploss, takeprofit)
    print(f"Position: {id}")
    positions = api.positions()
    print(positions)

    # for position in positions:
    #     close = api.positionCloseById(position['pos_id'], position['amount'])
    # print(positions)    


# def sell_position(stock):
#     try:
#         # Subscribe to the stock
#         api.subscribe("HK50")
#         sleep(1)

#         # Get the price
#         price = api.quote('HK50')
#         print(price, "priceprice")
        
#         if not price or 'bid' not in price:
#             raise ValueError("Failed to retrieve price or bid price not found")

#         bid_price = price['bid']
#         print(bid_price, "bid price")

#         # Define the trading parameters
#         symbol = "HK50"
#         volume = 7  # Position size
#         stoploss = round(bid_price + 0.00010, 6)
#         takeprofit = round(bid_price - 0.00010, 6)

#         # Place a sell order
#         id = api.sell(symbol, volume, stoploss, takeprofit)
#         print(f"Position: {id}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# #---------------------List Positions-----------------------#
def list_all_position():
    positions = api.positions()
    print(positions)


# #---------------------Close position by id-----------------------#
def close_position_by_id(pos_id, amount):
        # close = api.positionCloseById(pos_id, amount)
        # print("close:", close)
        # positions = api.positions()
        # print(positions)
        # for position in positions:
        close = api.positionCloseById(pos_id, amount)
        print(close)    
# #---------------------Close all positions-----------------------#
def close_position_all():
    close_all = api.close_all()
    print("close_all:", close_all)

#---------------------Parcial Close position-----------------------#

# api.positionPartialClose(id, volume) 

#---------------------Log Out-----------------------#

# api logout
# logout = api.logout()
# print("Is logout?: ", logout)

# check_connection("XAUUSD")
list_all_position()  
# buy_position('HK50')
# sell_position(None)
# list_all_position()  
close_position_by_id()
# close_position_all()


{'133629957': {'pos_id': '133629957', 'name': 'XAUUSD', 'long': 7.0, 'short': 0.0, 'price': 2384.19, 'digits': 2, 'clid': None}, 
 '133629326': {'pos_id': '133629326', 'name': 'XAUUSD', 'long': 7.0, 'short': 0.0, 'price': 2389.65, 'digits': 2, 'clid': None},
'133628857': {'pos_id': '133628857', 'name': 'HK50', 'long': 7.0, 'short': 0.0, 'price': 16648.8, 'digits': 1, 'clid': None, 'convert': 'USDK50', 'convert_dir': 1}}