from Crypto.Cipher import AES
from hashlib import md5
#from secret import a,b,c,d, FLAG

#assert a**4 + b**4 == c**4 + d**4 + 17 and max(a,b,c,d) < 2e4 and AES.new( f"{a*b*c*d}".zfill(16).encode() , AES.MODE_ECB).encrypt(FLAG).hex() == "41593455378fed8c3bd344827a193bde7ec2044a3f7a3ca6fb77448e9de55155"
from sympy.ntheory import discrete_log

# Modulo nguyên tố lớn được sử dụng trong tất cả phép toán
MOD = 4294967087

# Dữ liệu cho trước
test_pt = [577090037, 2444712010, 3639700191, 3445702192,
           3280387012, 271041745, 1095513148, 506456969]
test_ct = [3695492958, 1526668524, 3790189762, 20093842,
           2409408810, 239453620, 1615481745, 1887562585]
flag_enc = [605589777, 4254394693, 463430822, 2146232739,
            4230614750, 1466883317, 31739036, 1703606160]

# Khôi phục input[i] bằng cách giải phương trình:
#   test_pt[i]^x ≡ test_ct[i] (mod MOD)
inputs = [discrete_log(MOD, ct, pt) for pt, ct in zip(test_pt, test_ct)]

# Dùng input khôi phục flag:
#   flag[i] = flag_enc[i]^input[i] mod MOD
flag_nums = [pow(fe, inp, MOD) for fe, inp in zip(flag_enc, inputs)]

# Chuyển các số nguyên thành byte và kết hợp thành chuỗi flag
flag_bytes = b''.join(x.to_bytes(4, 'little') for x in flag_nums)
flag_str = flag_bytes.rstrip(b'\x00').decode(errors='replace')

# In kết quả
print("Recovered input:", inputs)
print("Flag: sigpwny{%s}" % flag_str)

import gmpy2
from Crypto.Cipher import AES

target = bytes.fromhex("41593455378fed8c3bd344827a193bde7ec2044a3f7a3ca6fb77448e9de55155")
MOD = 3000  # thử nhỏ trước, mở rộng sau

right_map = {}
for c in range(1, MOD):
    c4 = gmpy2.powmod(c, 4, 1 << 64)  # không modulo, nhưng nhanh
    for d in range(c, MOD):  # chỉ cần d ≥ c
        val = int(c4 + gmpy2.powmod(d, 4, 1 << 64))
        if val not in right_map:
            right_map[val] = (c, d)

# Duyệt bên trái
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
                print(f"Found: a={a}, b={b}, c={c}, d={d}")
                print("FLAG:", flag)
                exit()
