# codebase - code-master5
print("This program implements Caesar Cipher.")
print("Select option:")
print("1. Encrypt a message")
print("2. Decrypt a message")
print("Enter 1 or 2:")
option = int(input())

def encryption_function(key, val):
    if (val == ' '):
        return val
    return chr(((ord(val) - 97 + key) % 26) + 97)

def decryption_function(key, val):
    if (val == ' '):
        return val
    return chr(((ord(val) - 97 - key) % 26) + 97)

if (option == 1):
    print("Enter a message to encrypt (a-z only):")
    message = raw_input()
    print("Enter a key to encrypt (integer only):")
    key = int(input())
    message = list(message)
    encrypted_message = []
    for i in range(0, len(message)):
        encrypted_message.append(encryption_function(key, message[i]))
    encrypted_message = ''.join(encrypted_message)
    print("Encrypted Message: " + encrypted_message)

elif (option == 2):
    print("Enter a message to decrypt (a-z only):")
    encrypted_message = raw_input()
    print("Enter a key to decrypt (integer only):")
    key = int(input())
    encrypted_message = list(encrypted_message)
    message = []
    for i in range(0, len(encrypted_message)):
        message.append(decryption_function(key, encrypted_message[i]))
    message = ''.join(message)
    print("Decrypted Message: " + message)

else:
    print("Invalid Option!")
