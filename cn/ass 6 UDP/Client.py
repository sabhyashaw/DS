import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter Message: ")

client.sendto(message.encode(), ("localhost", 9999))

data, addr = client.recvfrom(1024)

print("Server Message:", data.decode())

client.close()