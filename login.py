import hashlib

h = hashlib.new("SHA256")

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
    h.update(query_user.encode())
    query_user_hash = h.hexdigest()

    if query_user_hash in username[0]:
        print("user found in the database!")
    elif query_user_hash not in username[0]:
        create_user = input("user not found in the database. Do you want to create a new user? [y/n]")
        if create_user == "y":
            new_user = input("input name for new user: ")
            h.update(new_user.encode())
            new_user_hash = h.hexdigest()

            new_password = input("input new password: ")
            h.update(new_password.encode())
            new_password_hash = h.hexdigest()

            write(new_user_hash, new_password_hash)
            break

        else:
            print("canceling...")
            print("Done!")
            break
    
    query_password = input("Type password for " + query_user + ":")
    h.update(query_password.encode())
    query_password_hash = h.hexdigest()

    if query_password_hash in username[1]:
        print("access granted!")
        break
    elif query_password_hash not in username[1]:
        print("access denied!")
        break
    
    else:
        break