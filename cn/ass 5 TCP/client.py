import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter Message: ")

client.sendto(msg.encode(), ("localhost", 9999))

data, addr = client.recvfrom(1024)

print("Server Reply:", data.decode())

client.close()