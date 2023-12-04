word = "lable"
xor_result = []
new_string = ""
newer_string = ""
for character in word:
    xor_result.append(ord(character)^13)

for number in xor_result:
    new_string += chr(number)

print(new_string)

# less code
for character in word:
    newer_string += chr(ord(character)^13)

print(newer_string)