'''

'''

password = input("please enter a password for the website: ")
print("!!dont forget this password!!")

login_password = ("please input the password you set for your accaunt")

while login_password != password:
    print("wrong password")
    login_password = input("please input the password you set for your accaunt")

print("you inputed a correct password congrats!!")