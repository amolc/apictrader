from ctrader import Ctrader
from time import sleep



server="13.248.185.194" # - Host name: (Current IP address 168.205.95.20 can be changed without notice)
account="demo.pepperstone.3965339" #  - SenderCompID: live.icmarkets.1104926
password="11gXWOqeaf!" # - The password you configured

print("server", server)
print("account", account)
print("password", password)

api = Ctrader(server,account,password, "HK50", 1, 0.00005, debug=True)
print("is struck here 2", api)
sleep(3)

print("is struck here 3")
checkConnection = api.isconnected()
print("Is Connected?: ", checkConnection)
sleep(1)
print("is struck here 4")