# https://crackmes.one/crackme/6a512a5e71ee08cad748dcb2

import struct

def checksum(username):
    data = username.encode()
    
    if len(data) < 8:
        return sum(data) & 0xFFFFFFFF
    
    total = 0
    for i in range(0, len(data) & ~7, 8):
        chunk = data[i:i+8]
        if len(chunk) < 8:
            chunk += b'\x00' * (8 - len(chunk))
        
        dword1 = struct.unpack('<I', chunk[0:4])[0]
        dword2 = struct.unpack('<I', chunk[4:8])[0]
        
        b1 = dword1 & 0xFF
        b2 = (dword1 >> 8) & 0xFF
        b3 = (dword1 >> 16) & 0xFF
        b4 = (dword1 >> 24) & 0xFF
        b5 = dword2 & 0xFF
        b6 = (dword2 >> 8) & 0xFF
        b7 = (dword2 >> 16) & 0xFF
        b8 = (dword2 >> 24) & 0xFF
        
        total += b4 + b4 + b3 + b4
        total += b8 + b8 + b7 + b8
    
    for i in range(len(data) & ~7, len(data)):
        total += data[i]
    
    return total & 0xFFFFFFFF

username = input("Username: ")
c = checksum(username)
print(f"Serial: {c * 123}")
