#Write a script that checks the login that the user enters.
#If the login is "First", then greet the users. 
#If the login is different, send an error message (need to use loop while).
while True:
    login = input("Enter your login: ")
    if login == "First":
        print(f"Greetings, user {login}!")
        break
    else:
        print("Login error! Please try again!")
        continue