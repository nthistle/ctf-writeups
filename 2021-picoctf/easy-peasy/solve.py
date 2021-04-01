import socket
import binascii

s = socket.socket()

s.connect(("mercury.picoctf.net", 36449))

d = b""
while b"encrypt?" not in d:
    d += s.recv(2048)

flag = binascii.unhexlify(d.decode().split("\n")[2])

s.send(("A"*(50000-len(flag))).encode()+b"\n")

d = b""
while b"encrypt?" not in d:
    d += s.recv(2048)

s.send(("A"*len(flag)).encode()+b"\n")

d = b""
while b"encrypt?" not in d:
    d += s.recv(2048)

d = d.decode().split("\n")[1]
d = binascii.unhexlify(d)

print("picoCTF{" + "".join(chr(a ^ b ^ ord("A")) for a, b in zip(d, flag)) + "}")

