"""
 Implements a simple HTTP/1.0 Server

"""

import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an AF_INET socket of type SOCK_STREAM
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)


try:
    while True:    
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        print(request)

        response = b'HTTP/1.0 200 OK\n\nHello World'
        client_connection.sendall(response)
        client_connection.close()
except KeyboardInterrupt:
    server_socket.close()
