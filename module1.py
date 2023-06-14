import random
import string

def registration(users, passwords):
    username = input("Sisestage kasutajanimi: ")
    if username in users:
        print("Sellise nimega kasutaja juba eksisteerib!")
        return users, passwords

    password_option = input("Valige parooli loomise valik (1 - automaatselt, 2 - käsitsi): ")

    if password_option == "1":
        password = generate_password()
        print("Automaatselt genereeritud parool:", password)
    elif password_option == "2":
        password = input("Sisestage parool: ")
        if not validate_password(password):
            print("Parool ei vasta nõuetele!")
            return users, passwords
    else:
        print("Vigane valik!")
        return users, passwords

    users.append(username)
    passwords.append(password)
    print("Registreerimine õnnestus!")
    return users, passwords


def authorization(users, passwords):
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username in users:
        index = users.index(username)
        if passwords[index] == password:
            return True
    return False

def change_credentials(users, passwords):
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if username in users:
        index = users.index(username)
        if passwords[index] == password:
            new_username = input("Введите новое имя пользователя: ")
            if new_username in users:
                print("Пользователь с таким именем уже существует!")
                return users, passwords
            new_password_option = input("Выберите опцию изменения пароля (1 - автоматически, 2 - самостоятельно): ")
            if new_password_option == "1":
                new_password = generate_password()
            elif new_password_option == "2":
                new_password = input("Введите новый пароль: ")
                if not validate_password(new_password):
                    print("Пароль не соответствует требованиям!")
                    return users, passwords
            else:
                print("Неверная опция!")
                return users, passwords

            users[index] = new_username
            passwords[index] = new_password
            print("Данные успешно изменены!")
            return users, passwords

    print("Неверное имя пользователя или пароль!")
    return users, passwords

def generate_password():
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

def save_dictionary(users, passwords, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for username, password in zip(users, passwords):
            file.write(f"{username}:{password}\n")

def load_dictionary(file_path):
    users = []
    passwords = []
    with open(file_path, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip().split(":")
            username = line[0]
            password = line[1]
            users.append(username)
            passwords.append(password)
    return users, passwords




