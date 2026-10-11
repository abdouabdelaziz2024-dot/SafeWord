import random
import time
import string

while True:
    print("\nWelcome to Password SafeWord")
    print("1. Generate a new password")
    print("2. View saved passwords")
    print("3. Search for a password")
    print("4. Delete a password")
    print("5. Edit a password")
    #print("6. Check password strength")
    print("7. Exit")
    choice = input("Enter your choice: " + "\n" + "\n")

    if choice == "1":
        web_app = input("Enter a Website or App Name: ")
        uname = input("Enter your username:")
        length = int(input("How long do you want your password to be? "))

        z = (''.join
        (random.choice(string.ascii_letters
        + string.digits + string.punctuation)
        for i in range(length)))
        y = time.strftime("%Y.%m.%d")


        print("\nYour username is:", uname)
        print("Web app name is:", web_app)
        print("Your Password is:", z)
        print("Date of Creation is:", y)

    # Save password
        with open("passwords.txt", "a") as f:
            f.write(
            "Web app name is: " + web_app +  "\n"
            + "Your username is: " + uname + "\n"
            +"Your Password is: " + z +     "\n"
            + "Date of Creation is: " + y +  "\n"
            + "-------------------------------\n"
            )
    elif choice =="2":
        with open("passwords.txt", "r") as f:
            saved_passwords = f.read()

        print("\nSaved Passwords:")
        print("-------------------------------")
        print(saved_passwords)

# search
    elif choice == "3":
        website = input("Enter a Website or App Name: ")

        with open("passwords.txt", "r") as f:
            saved_passwords = f.read()

        if website in saved_passwords:
            print("Website already exists")
        elif website not in saved_passwords:
            print("Website does not exists")
        lines = saved_passwords.split("\n")
        for i, line in enumerate(lines):
            if "Web app name is: " + website in line:
                print("\n".join(lines[i:i + 4]))




# Delete a password

    elif choice == "4":
        website = input("Enter a website or app Name to delete: ")
        with open("passwords.txt", "r") as f:
            saved_passwords = f.read()
            lines = saved_passwords.split("\n")
            found = False
            for i, line in enumerate(lines):
                if "Web app name is: " + website in line:
                    del(lines[i:i + 5])
                    found = True
            with open("passwords.txt", "w") as f:
                f.write("\n".join(lines))
            if website not in saved_passwords:
                print("Website does not exists")


# Edit a password

    elif choice == "5":
        website = input("Enter a website or app Name to Edit details: ")
        found = False
        with open("passwords.txt", "r") as f:
            saved_passwords = f.read()
            lines = saved_passwords.split("\n")
            for i, line in enumerate(lines):
                if "Web app name is: " + website in line:
                    found = True
                    print("1. Edit a website or app Name")
                    print("2. Editing username")
                    print("3. Editing password")
                    choice1 = input("Enter a choice: ")

                    if choice1 == "1":
                        new_website = input("Enter a new website or app Name: ")
                        lines[i] = "Web app name is: " + new_website
                    elif choice1 == "2":
                        new_un = input("Enter a new username: ")
                        lines[i + 1] = "Your username is: " + new_un
                    elif choice1 == "3":
                        new_pass = input("Enter a new password: ")
                        lines[i + 2] = "Your Password is: " + new_pass
                    with open("passwords.txt", "w")  as f:
                        f.write("\n".join(lines))
        if found == False:
            print("Website or App does not exist")

    #elif choice == "6":
        website = input("Enter a website or app Name to check password strength: ")
        found = False
        with open("passwords.txt", "r") as f:
            saved_passwords = f.read()
            lines = saved_passwords.split("\n")
            for i, line in enumerate(lines):
                if "Web app name is: " + website in line:
                    found = True
                    saved_password = lines[i + 2]
                    saved_password = saved_password.replace("Your Password is: ", "")










# Exit
    elif choice =="7":
        print("\nExiting...")
        exit()