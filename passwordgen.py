import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+=:?"
len_password = int(input("Enter the length of the password:"))
a = "".join(random.sample(password,len_password))
print(f" Your password is {a}")