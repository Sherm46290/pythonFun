import re

password = "Short7!"
flag = 1
while True:
    if (len(password) < 8):
        flag = 2
        break
    elif not re.search("[a-z]", password):
        flag = 2
        break
    elif not re.search("[A-Z]", password):
        flag = 2
        break
    elif not re.search("[0-9]", password):
        flag = 2
        break
    elif not re.search("[!@#$%^*()_<>?]", password):
        flag = 2
        break
    else:
        flag = 1
        print("Valid Password")
        break

if flag == 2:
    print("Not a Valid Password")

