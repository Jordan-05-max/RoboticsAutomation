
#client socket

import socket

#socket instantiation
client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

#socket binding to IP and port number
client_ip = "127.0.0.1"
client_port_number = 2104
client_socket.bind((client_ip, client_port_number))

#connection request to the server
client_socket.connect(("127.0.0.1", 2024))

#client communication loop
while True:
    msg = input("client: ")
    client_socket.send(msg.encode("utf-8"))
    server_response = client_socket.recv(1000)
    server_response = server_response.decode("utf-8")
    if server_response == "closed":
        break
    print("Server:", server_response)

client_socket.close()
