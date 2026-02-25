import socket
import time

#adresa a port serveru
host = "127.0.0.1"
port = 50000

#vytvoreni socketu
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#otevrit kanal
tcp_socket.connect((host, port))

for i in range(5):
    msg = "data" + str(i)
    tcp_socket.sendall(msg.encode('ascii'))

    #prijem
    data = tcp_socket.recv(1024)
    print(data)

#uzavreni kanalu
tcp_socket.close()