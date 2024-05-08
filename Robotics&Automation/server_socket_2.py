

#server socket

import socket

#socket instantiation
server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

# binding socket to IP address and port number
server_ip = "192.168.43.246"
server_port_nunmber = 2024
server_socket.bind((server_ip, server_port_nunmber))

#listen
server_socket.listen(1)

#accept
(server_client_socket_1, client_address) = server_socket.accept()   # client_address --> (client_IP, client_port_number)
print("new connection request accepted")
#server communication loop
while True:
    client_request = server_client_socket_1.recv(1000)
    client_request = client_request.decode("utf-8")
    if client_request == "close":
        server_client_socket_1.send("closed".encode("utf-8"))
        break    
    print("client:", client_request)
    server_client_socket_1.send(input("response: ").encode("utf-8"))

server_client_socket_1.close()
    
