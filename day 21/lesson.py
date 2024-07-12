def check_gmail(email):
    return email.endswith("@gmail.com")
def check_password(password):
    return len(password)>= 8
def register():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if check_gmail(email) and check_password(password):
        print("You registerd")
    else:
        print("You Didnt registerd")
if __name__ =="__main__":
    register()