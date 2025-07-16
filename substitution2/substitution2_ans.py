import string
text=input("crypt:")
result=""
ALPHABET=string.ascii_uppercase
alphabet=string.ascii_lowercase
table=["?"]*26
table[2]='i'
table[3]='g'
table[4]='f'
table[5]=''
table[6]=''
table[7]='o'
table[8]='t'
table[9]=''
table[10]='?'
table[11]=''
table[12]='a'
table[13]='e'
table[14]=''
table[15]=''
table[16]='p'
table[17]=''
table[18]='h'
table[19]='s'
table[20]='c'
table[21]=''
table[22]=''
table[23]='l'
table[24]=''
table[25]=''

for c in text:
    if(c in alphabet):
        result+=table[alphabet.index(c)]
    else:
        result+='?'
print(result)