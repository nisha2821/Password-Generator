import random

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special_chars="!@#$%^&*"

length=int(input("Enter the password length:"))
if length < 4:
    print("password length must be at least 4")
else:

    password=[]

    password.append(random.choice(uppercase))
    password.append(random.choice(lowercase))
    password.append(random.choice(numbers))
    password.append(random.choice(special_chars))

    all_characters=uppercase+lowercase+numbers+special_chars

    for i in range(length-4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    final_password= "".join(password)
    print("Generated Password:",final_password)