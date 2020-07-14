#configure

db_users = {"alex":"123", "baby":"321", "root":"toor"}
#db_passwd = ("123","321","\a")
i = 0

print("Welcome to auth system.")
login = input("Enter your name, please\a: ")
if login in db_users:
    print ("Hello, ", login)
    while i < 3:
        passwd = input(login + ", enter your password: ")
        if passwd == db_users[login]:
            print ("Access granted")
            break
        i=i+1
        print ("Passwd error. Try Harder")
    else:
        print ("Access denied")
else:
    print ("Name is uncorrect")
