from Crypto.Util.number import *

encrypted_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
convert_to_bytes = long_to_bytes(encrypted_integer)
convert_to_hex = convert_to_bytes.hex()

print(convert_to_bytes)