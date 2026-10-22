
print("Secure Login System")
credentials = {}

def sign_up(): 
    username = input("Enter an username: ")
    password = input("Enter a password: ")
    credentials[username] = password

def login():
    
    login_successful = attempt_user_login()
    
    if login_successful:
        print("Access granted")
    else:
        print("Access denied")

def attempt_user_login():
    
    attempt_count = 0
    maximum_attempts = 3 
    login_successful = False
    
    while attempt_count < maximum_attempts and not login_successful:
        print(f"\n Attempt {attempt_count + 1} of {maximum_attempts}")

        username = sanitise_user_input(input("Username: "))
        password = sanitise_user_input(input("Password: "))

        print(credentials)
        
        if :
            print("Login Successful")
            login_successful = True
        else:
            print("User not found or Incorrect Password")

                
        attempt_count += 1

        if not login_successful and attempt_count < maximum_attempts:
            remaining = maximum_attempts - attempt_count
            print(f"{remaining} attempts remaining")
            
    if not login_successful:
        print("Account locked")
        
    return login_successful
    
def sanitise_user_input(user_input):
    user_input = str(user_input)
    user_input.strip
    if len(user_input) > 25:
        print("Input too long, please try again.")
        main()


    return user_input
    
def compute_password_hash(password):
    return 0

while True:
    choice = sanitise_user_input(input("Sign Up (S) or Login in (L): "))
    choice.lower
    print(choice)
    if choice == "s":
        sign_up()
    elif choice == "l":
        login()
    else:
        print("Try Again")
