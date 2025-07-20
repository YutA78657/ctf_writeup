import string
ALPHABET=string.ascii_uppercase
alphabet=string.ascii_lowercase
text=input("crypt:")
table=['a','i','p','f','h','r','s','w','m','o','?','?','d','k','?','u','l','g','y','b','?','n','t','e','v','c']
numTable=[]
result=""
for c in table:
    if(c in alphabet):
        numTable.append(alphabet.index(c))
    else:
        numTable.append(-1)

for c in text:
    if(c in ALPHABET):
        if(numTable[ALPHABET.index(c)]==-1):
            result+='?'
        else:
            result+=ALPHABET[numTable[ALPHABET.index(c)]]
    elif(c in alphabet):
        if(numTable[alphabet.index(c)]==-1):
            result+='?'
        else: 
            result+=alphabet[numTable[alphabet.index(c)]]
    else:
        result+=c

print(result)
