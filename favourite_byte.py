from pwn import xor
import base64

bytes_from_hex = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
b64 = base64.b64encode(bytes_from_hex)
hex_flag = b64.hex()

print(bytes_from_hex)
print(hex_flag)