from pymodbus.client.sync import ModbusTcpClient
import random
import time

# UR3 IP address
host = '169.254.147.178'  

# Standard port for Modbus TCP communication.
port = 502

# Set up the client.
client = ModbusTcpClient(host, port)
while True:
    client.connect()
    data = random.randint(25,35) # Generates random numbers between 25 and 25
    wr = client.write_registers(1,1,unit=1) # Write a 1 in register #1
    time.sleep(5)

# This will only write a 1 in register #1; just to confirm Modbus communication is active and running.
# Works great for debugging.
