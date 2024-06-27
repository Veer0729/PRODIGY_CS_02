import re

password = input("Enter your password: ")

if len(password) < 8:
        print("password must be larger than 8 characters")
else:
     char_type = set()


for char in password:

    if char.islower():
        char_type.add("lowercase")
    elif char.isupper():
        char_type.add("Uppercase")
    elif char.isdigit():
        char_type.add("Digit")
    elif re.match(r'[^a-zA-Z0-9]', char):
        char_type.add("special")


if len(char_type) == 1:
    print("Very weak password")
elif len(char_type) == 2:
    print("Weak password")
elif len(char_type) == 3:
    print("Decent password")
elif len(char_type) == 4:
    print("Strong password")