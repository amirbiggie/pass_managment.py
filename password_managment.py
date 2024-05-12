def user_pass(username , password):
    with open("./password_F.txt", "a") as f:
        f.write(f"{username}-{password}")
    
    print("ADDED :)")





while True:
    user_input = input("Enter the mode (a: add, v: view, q: quit)")

    if user_input == "v":
        print("your passwords are as follows")
        pass
    
    elif user_input == "a":
        print("let's add a new username-password")
        
        username = input("Enter new username:")
        password = input("Enter new password")
        user_pass(username , password)
        

    elif user_input == "q":
        break
    
    else:
        print("wrong mode!")
        
