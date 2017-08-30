# codebase - code-master5
print("This program implements Vignere Cipher.")
print("Select option:")
print("1. Encrypt a message")
print("2. Decrypt a message")
print("Enter 1 or 2:")
option = int(raw_input())

def encryption_function(key, val):
    if (val == ' '):
        return val
    return chr(((ord(val) - 97 + ord(key)) % 26) + 97)

def decryption_function(key, val):
    '''
    if (val == ' '):
        return val
    '''
    return chr(((ord(val) - 97 - ord(key)) % 26) + 97)

if (option == 1):
    print("Enter a message to encrypt (a-z only):")
    message = raw_input()
    message = list(message)
    print("Enter a keyword to encrypt (a-z only):")
    key = raw_input()
    key = list(key)
    encrypted_message = []
    for i in range(0, len(message)):
        encrypted_message.append(encryption_function(key[i % len(key)], message[i]))
    encrypted_message = ''.join(encrypted_message)
    print("Encrypted Message: " + encrypted_message)

elif (option == 2):
    print("Enter a message to decrypt (a-z only):")
    encrypted_message = raw_input()
    encrypted_message = list(encrypted_message)
    print("Enter a key to decrypt (integer only):")
    key = raw_input()
    key = list(key)
    message = []
    for i in range(0, len(encrypted_message)):
        message.append(decryption_function(key[i % len(key)], encrypted_message[i]))
    message = ''.join(message)
    print("Decrypted Message: " + message)

else:
    print("Invalid Option!")
