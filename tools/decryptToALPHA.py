import string 
print("crypt:")
crypt = list(map(int, input().split()))
alpha = string.ascii_lowercase
result = ""
for n in crypt:
    result += alpha(n)

print("result:"+result)
