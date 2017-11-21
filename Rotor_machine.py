# code-master5
#
'''  Runnig instructions -
         python3 Rotor_machine.py
         first three inputs like - 3 6 9
         Plaintext like - asdfasdfkjlkasdfjlkj
         Output like - 
             Encrypted data
             skvxskvxcbdcskvxbdcb
             Decrypted data
             asdfasdfkjlkasdfjlkj
 '''

def ceaser(text, key):
    ans = ''
    for i in text:
        temp = ord(i)
        if(temp >= 97 and temp <= 122):
            encrypted = ((temp - 97) + key)%26 + 97
        else:
            encrypted = temp
        ans = ans + chr(encrypted)
    return ans
if __name__ == '__main__':
    print('Enter 3 keys of rotors')
    a,b,c = map(int, input().split(' '))
    print('Enter plain text')
    text = input()
    print('Encrypted data');
    x = ceaser(text,a)
    y = ceaser(x,b)
    z = ceaser(y,c)
    print(z)
    print('Decrypted data');
    x = ceaser(z,-c)
    y = ceaser(x,-b)
    z = ceaser(y,-a)
    print(z)
