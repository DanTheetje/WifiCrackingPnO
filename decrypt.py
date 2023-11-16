import base64

data = base64.b64decode("")
key = ""

S = range(256)
j = 0
out = []

#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

print("".join(out))