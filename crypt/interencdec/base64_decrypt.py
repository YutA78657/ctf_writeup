import base64
crypt=input("crypt:")
decoded = base64.b64decode(crypt).decode()
print("result:"+decoded)
