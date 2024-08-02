# Assuming the provided class code is saved in a module named fix_module

from fix import FIX, Side, OrderType
import logging
import time

# Define the position_list_callback to handle position list updates
def position_list_callback(position_list, spot_price_list, client_id):
    # This function will be called with updated position lists
    print(f"Updated position list for client {client_id}:")
    for pos_id, position in position_list.items():
        print(f"Position ID: {pos_id}, Details: {position}")

# Define a dummy order_list_callback as it is required by the FIX class but not used in this context
def order_list_callback(order_list, spot_price_list, client_id):
    pass

# Set up logging if needed
logging.basicConfig(level=logging.DEBUG)



# Create an instance of the FIX class
fix = FIX(
    broker='pepperstone',
    login="3965339",
    server="13.248.185.194", # - Host name: (Current IP address 168.205.95.20 can be changed without notice)
    password="98814000", # - The password you configured
    currency='USD',
    client_id='3965339',
    position_list_callback=position_list_callback,
    order_list_callback=order_list_callback,
    update_fix_status=None  # You can define a status update callback if needed
)

# Request the position list
fix.position_request()

# Since FIX is using threads to handle connections and messages, you may want to keep the main thread running
# to allow the background threads to process incoming messages
try:
    while True:
        time.sleep(1)  # Keep the main thread alive
except KeyboardInterrupt:
    # Handle graceful shutdown on Ctrl+C
    print("Shutting down...")
    fix.logout()
