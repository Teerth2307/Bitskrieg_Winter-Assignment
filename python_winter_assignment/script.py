hex = '334e8543752e4f35123b7e3d30846b1d7d2575742e2a01'
x= [int(hex[i:i+2], 16) for i in range(0, len(hex), 2)]
n = len(x)
y = x[::-1]
decoded_xor = []
for i, z in enumerate(y):
    val_minus_i = (z - i) % 256
    original_val = val_minus_i ^ 66
    decoded_xor.append(original_val)

y = decoded_xor

final_flag = [0] * n
for i in range(n):
    mapped_index = (i * 7) % n
    final_flag[i] = y[mapped_index]

flag = "".join([chr(x) for x in final_flag])
print(f"\n{flag}")