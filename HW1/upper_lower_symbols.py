# Task - Count all Upper latin chars and Lower latin chars in the string
test_string = input('Enter string: ')
lower_chars = upper_chars = 0
for char in test_string:
    if 'a' <= char <= 'z':
        lower_chars += 1
    elif 'A' <= char <= 'Z':
        upper_chars += 1
print(f'Numbers of lower chars is: {lower_chars}')
print(f'Numbers of upper chars is: {upper_chars}')
