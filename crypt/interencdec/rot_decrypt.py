import string
result =""
crypt = input("crypt:")
key = (int)(input("key:"))

ALPHABET = string.ascii_uppercase
alphabet = string.ascii_lowercase
for c in crypt:
    if c in ALPHABET:
        result+=ALPHABET[(ALPHABET.index(c)+26-key)%26]
    elif  c in alphabet:
        result+=alphabet[(alphabet.index(c)+26-key)%26]
    else:
        result+=c
print("result:"+result)