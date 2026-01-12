# socket_client.py

import socket

def client_program():
    # define host name and port (of the server to connect to)
    host = 'localhost'  # as both code is running on same pc
    port = 5000         # socket server port number
    
    # create socket
    client_socket = socket.socket()
    
    # connect to the server
    client_socket.connect((host, port))
    
    # prompt the user to enter a message
    message = input(" -> ")  # take input
    
    # message loop
    while message.lower().strip() != 'bye':
        # send message to the server as bytes
        client_socket.send(message.encode())
        
        # receive response from the server
        data = client_socket.recv(1024).decode()
        
        print('Received from server: ' + data)
        
        # prompt the user to enter a new message
        message = input(" -> ")  # take new input
        
    # close the connection
    client_socket.close()
    
if __name__ == '__main__':
    client_program()