import hashlib

def read():
    with open("accounts.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            global username
            username = line.split("/")
            user = username[0]
            password = username[1]

def write(user, passwordname):
    with open("accounts.txt", "a") as file:
        file.write("\n" + user + "/" + passwordname)

read()

while True:
    query_user = input("Type user or create account: ")

    if query_user in username[0]:
        print("user found in the database!")
    elif query_user not in username[0]:
        create_user = input("user not found in the database. Do you want to create a new user? [y/n]")
        if create_user == "y":
            new_user = input("input new name for user: ")
            new_password = input("input new password: ")
            write(new_user, new_password)
            break
        else:
            print("canceling...")
            print("Done!")
            break
    
    query_password = input("Type password for " + query_user + ":")

    if query_password in username[1]:
        print("access granted!")
    elif query_password not in username[1]:
        print("access denied!")
        break
    
    else:
        break