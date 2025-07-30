import gmpy2
from Crypto.Cipher import AES

target = bytes.fromhex("41593455378fed8c3bd344827a193bde7ec2044a3f7a3ca6fb77448e9de55155")
MOD = 3000  

right_map = {}
for c in range(1, MOD):
    c4 = gmpy2.powmod(c, 4, 1 << 64)  
    for d in range(c, MOD):  
        val = int(c4 + gmpy2.powmod(d, 4, 1 << 64))
        if val not in right_map:
            right_map[val] = (c, d)

for a in range(1, MOD):
    a4 = gmpy2.powmod(a, 4, 1 << 64)
    for b in range(a, MOD):
        left = int(a4 + gmpy2.powmod(b, 4, 1 << 64))
        right = left - 17
        if right in right_map:
            c, d = right_map[right]
            key = str(a * b * c * d).zfill(16).encode()
            if len(key) == 16:
                cipher = AES.new(key, AES.MODE_ECB)
                flag = cipher.decrypt(target)
                print("FLAG:", flag)
                exit()
