#!/usr/bin/env python3
# https://crackmes.one/crackme/6a512a442c3088f968e1341b


def compute_serial(username):
    iVar18 = 0
    
    username_bytes = username.encode('ascii')
    length = len(username_bytes)
    
    pos = 0
    while pos + 8 <= length:
        val1 = int.from_bytes(username_bytes[pos:pos+4], 'little')
        
        iVar30 = (val1 & 0xFF)
        iVar31 = (val1 >> 24) & 0xFF
        iVar32 = (val1 >> 16) & 0xFF
        iVar33 = (val1 >> 8) & 0xFF
        
        val2 = int.from_bytes(username_bytes[pos+4:pos+8], 'little')
        
        iVar18_contrib = (val2 & 0xFF)
        iVar27 = (val2 >> 24) & 0xFF
        iVar28 = (val2 >> 16) & 0xFF
        iVar29 = (val2 >> 8) & 0xFF
        
        iVar18 += iVar30 + iVar18_contrib + iVar32 + iVar28 + iVar31 + iVar27 + iVar33 + iVar29
        
        pos += 8
    
    while pos < length:
        iVar18 += username_bytes[pos]
        pos += 1
    
    serial = (iVar18 * 0x539) ^ 0x5a5a
    
    return serial & 0xFFFFFFFF


def main():
    print()
    
    username = input("Enter Username: ").strip()
    
    if not username:
        print("[-] Username cannot be empty!")
        return
    
    serial = compute_serial(username)
    print(f"[+] Valid Serial: {serial}")
    print(f"[*] Verification formula: (sum_of_chars * 0x539) ^ 0x5a5a = {serial}")


if __name__ == "__main__":
    main()
