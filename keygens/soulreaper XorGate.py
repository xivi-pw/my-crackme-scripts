# https://crackmes.one/crackme/6a768ab608712c1a17cbacdd

def generate(username):
    password = ""
    for char in username:
        xor_result = ord(char) ^ 0x23
        password += f"{xor_result:02x}"
    password += "@password"
    return password

username = input("Enter Username: ")
password = generate(username)
print(f"Password is {password}")
