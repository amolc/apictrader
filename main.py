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

# checkConnection = api.isconnected()
# print("Is Connected?: ", checkConnection)
# sleep(1)




#---------------------Subscribe to symbols-----------------------#

# symbols = api.subscribe("EURUSD")

# print("symbols:", symbols)


#---------------------List of quotes for all symbols----------------------#



#---------------------Market position and pending orders-----------------------#

# Buy position
# api.subscribe("EURUSD")
# sleep(1)
# price = api.quote()
# print(price, "priceprice")
# price = price['EURUSD']['bid'] 

# symbol = "EURUSD"
# volume = 0.01 # position size:
# stoploss =  round(price - 0.00010,6)
# takeprofit = round(price + 0.00010,6)
# id = api.buy(symbol, volume, stoploss, takeprofit)
# print(f"Position: {id}")

# sell position 
# api.subscribe("EURUSD")
# sleep(1)
# price = api.quote()
# print(price, "priceprice")
# price = price['EURUSD']['bid'] 


# symbol = "EURUSD"
# volume = 0.01 # position size
# stoploss =  round(price + 0.00010,6)
# takeprofit = round(price - 0.00010,6)

# id = api.sell(symbol, volume, stoploss, takeprofit)
# print(f"Position: {id}")

#---------------------List Positions-----------------------#

positions = api.positions()
print(positions)


#---------------------Close position by id-----------------------#

for position in positions:
    api.positionCloseById(position['pos_id'], position['amount'])

#---------------------Close all positions-----------------------#

# api.close_all()


#---------------------Parcial Close position-----------------------#

# api.positionPartialClose(id, volume) 

#---------------------Log Out-----------------------#

# api logout
# logout = api.logout()
# print("Is logout?: ", logout)