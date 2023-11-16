import base64

data = base64.b64decode("ff e2 c1 54 cd be 4a 8a f6 d0 3d 7e ba da bf f4 46 b6 82 85 18 f1 03 9d 96 94 08 02 28")
key = "63 72 79 70 74 69 84"

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