# password manager ke 3 mode dare 
# user va pass ro migire to file save mikone 
# ba sarche ham mitoni pass mored nazareto pida koni
from userID import id



def user_pass(username , password, U_id):
    with open("./password_F.txt", "a") as f:
        f.write(f"{username}|{password}|{U_id}\n")
    
    print("ADDED :)")

def user_view():
    with open("./password_F.txt", "r") as f:
        for item in f:
            item = item.rstrip()
            username ,password = item.split("|")
            print(f"UserName:{username} | Password:{password}")




while True:
    user_input = input("Enter the mode (a: add, v: view, q: quit)")

    if user_input == "v":
        print("your passwords are as follows")
        user_view()
    
    elif user_input == "a":
        print("let's add a new username-password")
        
        username = input("Enter new username:")
        password = input("Enter new password")
        u_id = id().ganereate_id()
        user_pass(username , password , u_id)
        
        

    elif user_input == "q":
        break
    
    else:
        print("wrong mode!")
        
