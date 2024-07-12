import socket

# Define server IP address and port
server_ip = '192.168.1.6'
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to server:", server_ip)

# Send data to the server
data = "Hello, server!"
client_socket.send(data.encode())

# Close the socket
client_socket.close()
