import string
ALPHABET=string.ascii_uppercase
alphabet=string.ascii_lowercase
number=string.digits
key="cylab"
text=input("crypt:")
result=""
i=0
for c in text:
    if(c in ALPHABET):
        result+=ALPHABET[(ALPHABET.index(c)-alphabet.index(key[i%len(key)]))%26]
        i+=1
    elif(c in alphabet):
        result+=alphabet[(alphabet.index(c)-alphabet.index(key[i%len(key)]))%26]
        i+=1
    else:
        result+=c
print(result)