'''

Networking with python is not an easy topic

make sure you will check the documentation for for advanced networking concepts....

'''

import socket

# Create socket object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# define the host and port 

host = '127.0.0.1'
port = 12345

# bind the socket to the address.
server_socket.bind((host, port))

# start listening for incomming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}...")

# accept a connection and get the client socket 
client_socket, client_address = server_socket.accept()

print(f'Connection established with {client_address}')

# recieve data from the client 

data = client_socket.recv(1024).decode('utf-8')
print(f'Received: {data}')

# echo the received data back to the client
client_socket.send(data.encode('utf-8'))

# close the sockets

client_socket.close()
server_socket.close()





