user = input("User: ")
pswd = input("Paswd: ")

if user == "diego":
    if pswd == "1234":
        print("Successfuly")
    else:
        print("Wrong password")
else:
    if pswd == "1234":
        print("Wrong user")
    else:
        print("Wrong user and password")