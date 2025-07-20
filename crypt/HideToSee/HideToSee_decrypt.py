import string
ALPHABET=string.ascii_uppercase
alphabet=string.ascii_lowercase
text=input("crypt:")
result=""
for c in text:
    if(c in ALPHABET):
        result+=ALPHABET[25-ALPHABET.index(c)]
    elif(c in alphabet):
        result+=alphabet[25-alphabet.index(c)]
    else:
        result+=c
print(result)