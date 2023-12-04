hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytes_flag = bytes.fromhex(hex_string)
og_hex_string = bytes_flag.hex()

print(bytes_flag)

if (og_hex_string == hex_string):
    print("They match")
    print(hex_string + " = " + og_hex_string)