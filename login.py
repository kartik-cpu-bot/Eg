print("Secure Login System")
def main():
    
    login_successful = attempt_user_login({})
    
    if login_successful:
        print("Access granted")
    else:
        print("Access denied")

def attempt_user_login(user_database):
    #Single Account
    test_username = "admin"
    test_password = "1234"
    
    attempt_count = 0
    maximum_attempts = 3 
    login_successful = False
    
    while attempt_count < maximum_attempts and not login_successful:
        print(f"\n Attempt {attempt_count + 1} of {maximum_attempts}")

        username = sanitise_user_input(input("Username: "))
        password = sanitise_user_input(input("Password: "))
        
        user_correct = username == test_username
        password_correct = password == test_password
        
        if user_correct and password_correct:
            print("Login Successful")
            login_successful = True
        else:
            if not user_correct:
                print("User not found")
            else:
                print("Incorrect password")
                
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

if __name__ == "__main__":
    main()