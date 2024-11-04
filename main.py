import string
import random

print("Welcome to Password Management System!")
# Get the app/website name
def get_app_name():
    while True:
        try:
            app_name = input("What’s the name of the app/website account you’re creating: ").strip()
            if not app_name:
                raise ValueError("App/website name cannot be empty.")
            return app_name
        except ValueError as e:
            print(e)

# Uppercase Alphabet List
uppercase_alphabet_list = list(string.ascii_uppercase[:26])

# Lowercase Alphabet List
lowercase_alphabet_list = list(string.ascii_lowercase[:26])

# Number 0-9 List
number_list = []
for i in range(0, 10):
    number_list.append(str(i))

# Symbol List
symbol_list = list(string.punctuation)


# Password generator
def password_gen_Q(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["yes", "no"]:
            return response
        print("Please answer with 'Yes' or 'No'.")


# Security questions
def security_question(prompt):
    while True:
        try:
            response = input(prompt).lower()
            if response in ["yes", "no"]:
                return response
            else:
                raise ValueError("Please answer with 'Yes' or 'No'.")
        except ValueError as e:
            print(e)


def main_menu():
    print("Main Menu for Password Management System:")
    print("1. Password Management System")
    print("2. Summary of Passwords")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Please choose an option (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid option. Please choose a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        choice = main_menu()
        if choice == 1:
            # Get the app/website name
            app_name = get_app_name()
            print(f"App/Website Name: {app_name}")
            with open("Password List.txt", "a") as file:
                file.write(f"Apps/Website Name: {app_name}\n")

            # Password Generator
            password_gen_help = password_gen_Q("Would you like us to help generate a random password (Yes/No): ")
            if password_gen_help == "yes":
                try:
                    num_uppercase = int(input("How many uppercase letters do you need: "))
                    num_lowercase = int(input("How many lowercase letters do you need: "))
                    num_no = int(input("How many digit numbers do you need: "))
                    num_symbol = int(input("How many symbols do you need: "))
                except ValueError:
                    print("Please enter a valid number.")

                password = []
                for letters in range(num_uppercase):
                    password.append(random.choice(uppercase_alphabet_list))

                for letters in range(num_lowercase):
                    password.append(random.choice(lowercase_alphabet_list))

                for digits in range(num_no):
                    password.append(random.choice(number_list))

                for symbols in range(num_symbol):
                    password.append(random.choice(symbol_list))

                random.shuffle(password)
                shuffled_password = "".join(password)
                print(f"The password for {app_name} is {shuffled_password}")
                with open("Password List.txt", "a") as file:
                    file.write(f"Password: {shuffled_password}\n")

            else:
                user_password = input("What is the password you fill in the app/website: ")
                confirm_user_password = input("Please re-enter your password to confirm: ")
                while user_password != confirm_user_password:
                    print("Password does not match. Please try again.")
                    confirm_user_password = input("Please re-enter your password to confirm: ")
                print("Password Saved!")

                with open("Password List.txt", "a") as file:
                    file.write(f"Password: {confirm_user_password}\n")

            # Security Questions
            s_ques_main = security_question("Are there any security questions (Yes/No): ")

            security_dict = {}

            while s_ques_main != "no":
                try:
                    s_Q = input("What security question is being answered: ").strip()
                    if not s_Q:
                        raise ValueError("Security question cannot be empty.")

                    s_A = input("What answer did you provide for the security question: ").strip()
                    if not s_A:
                        raise ValueError("Answer cannot be empty.")

                    security_dict[s_Q] = s_A

                    with open("Password List.txt", "a") as file:
                        file.write(f"Security Question: {s_Q}\n")
                        file.write(f"Security Answer: {s_A}\n")

                except ValueError as e:
                    print(e)
                s_ques_main = security_question("Are there still any security questions (Yes/No): ")

            if security_dict:
                print("Here are the questions and answers:")
                for question, answer in security_dict.items():
                    print(f"question: {question}")
                    print(f"answer: {answer}\n")
            else:
                print("No security questions provided.")
                with open("Password List.txt", "a") as file:
                    file.write(f"Security Question: No security questions provided.\n")

            with open("Password List.txt", "a") as file:
                file.write("-" * 50 + "\n")
        elif choice == 2:
            with open("Password List.txt", "r") as file:
                print(file.read())

        elif choice == 3:
            print("Exit successfully, bye!")
            break


if __name__ == "__main__":
    main()
