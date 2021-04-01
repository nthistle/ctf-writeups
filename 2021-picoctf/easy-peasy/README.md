# Easy Peasy

## Challenge

> Author: madStacks
>
> Points: 40
>
> Description: A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 36449` [otp.py](otp.py)

## Solution

It isn't too hard to tell from the source itself, but a hint sums this problem up well: "Maybe there's a way to make this a 2x pad". Here are the relevant lines from the source.

```python
KEY_LEN = 50000

...

def encrypt(key_location):
    ui = ... # ui = "user input"
    
    start = key_location
    stop = key_location + len(ui)
    
    if stop >= KEY_LEN:
        stop = stop % KEY_LEN
        key = kf[start:] + kf[:stop]
    else:
        key = kf[start:stop]
    
    key_location = stop
    
    ...
```

When you first connect, it encrypts the flag with location 0, and then it allows you to make any number of encryption requests, adjusting the location each time so it uses new bytes of the pad. [One-time pad](https://en.wikipedia.org/wiki/One-time_pad) is secure if used properly, but as the Wikipedia page and problem hint mention, if the key is reused, you lose perfect secrecy. In this case, once you go through all 50,000 key bytes, it wraps around to the beginning, effectively reusing the pad. Here's the [solve script](solve.py):

```python
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
```

Giving the flag, `picoCTF{75302b38697a8717f0faee9c0fd36a57}`