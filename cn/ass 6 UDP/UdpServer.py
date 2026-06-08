import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", 9999))

print("UDP Server is running...")

while True:
    data, addr = server.recvfrom(1024)

    print("Client Message:", data.decode())

    msg = "Hello Client, Message received"

    server.sendto(msg.encode(), addr)