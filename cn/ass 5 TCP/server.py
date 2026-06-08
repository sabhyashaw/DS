import socket

s = socket.socket()

print("Socket Created")

s.bind(("localhost", 9999))

print("Socket binded to port 9999")

s.listen(5)

print("Socket is listening...")

c, addr = s.accept()

print("Client Connected", addr)

data = c.recv(9998).decode()

print("### Client saying:", data)

c.send("Message received successfully".encode())

c.close()

s.close()