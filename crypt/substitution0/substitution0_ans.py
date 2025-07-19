import string
result=""
ctable=input("table:")
ntable=[0]*26
ALPHABET=string.ascii_uppercase
alphabet=string.ascii_lowercase
i=0
for c in ctable:
    ntable[i]=ALPHABET.index(c)
    i+=1
crypt=input("crypt:")
for c in crypt:
    if c in ALPHABET:
        result+=ALPHABET[ntable.index(ALPHABET.index(c))]
    elif c in alphabet:
        result+=alphabet[ntable.index(alphabet.index(c))]
    else:
        result+=c
print("result:"+result)