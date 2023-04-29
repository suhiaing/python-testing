import ast

def write_dictionary_to_file(dictionary, filename):
    with open(filename, 'a') as file:
        file.write(str(dictionary) + '\n')

def read_dictionaries_from_file(filename):
    dictionaries = []
    with open(filename, 'r') as file:
        contents = file.readlines()
        for line in contents:
            dictionary = ast.literal_eval(line.strip())
            dictionaries.append(dictionary)
    return dictionaries

def main_sector():
    main_option = int(input("Press 1 to Register:\nPress 2 to Login\nPress 3 to Exit: "))
    if main_option == 1:
        registration()
    elif main_option == 2:
        login()
    elif main_option == 3:
        exit(1)
    else:
        print("Invalid Option")
        main_sector()

def registration():
    user_email = input("Enter your email: ")
    email_get = Email_exit(user_email)

    if email_get is not None:
        print("Email already exists.")
        registration()
    else:
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")
        user_phone = int(input("Enter your phone: "))
        user_age = int(input("Enter your age: "))

        id = len(db) + 1
        to_insert = {id: {"email": user_email, "u_name": user_name, "password": user_password,
                          "phone": user_phone, "age": user_age}}
        db.append(to_insert)
        write_dictionary_to_file(to_insert, 'dictionary.txt')

def login():
    user_found = -1
    print("This is the login sector.")
    l_user_email = input("Enter your email to login: ")
    l_user_password = input("Enter your password to login: ")

    for i in range(len(db)):
        if db[i][i + 1]["email"] == l_user_email and db[i][i + 1]["password"] == l_user_password:
            user_found = i
            break
    if user_found != -1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("Not Found.")

def user_profile(user_found):
    print("Welcome:", db[user_found][user_found + 1]["u_name"])

    option = int(input("Press 1 to exit: "))
    if option == 1:
        main_sector()
def Email_exit(email):
    for i in range(len(db)):
        if db[i][i + 1]["email"] == email:
            return i

if __name__ == '__main__':
    while True:
        db = []
        loaded_dictionaries = read_dictionaries_from_file('dictionary.txt')
        db.extend(loaded_dictionaries)
        print("Loaded Dictionaries:")
        for dictionary in loaded_dictionaries:
            print(dictionary)
        main_sector()
