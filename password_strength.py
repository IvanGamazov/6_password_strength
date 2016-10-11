from urllib.request import urlretrieve
import os
import getpass


def get_blacklist_passwords():
    bad_passwords_file = 'blacklist.txt'
    if not os.path.exists('blacklist.txt'):
        blacklist_url = "http://slandail.net/wp-content/uploads/2015/06/dropbox_85100_nsfw.txt.txt"
        urlretrieve(blacklist_url, bad_passwords_file)
    bad_passwords = []
    with open(bad_passwords_file) as blacklist:
        for line in blacklist:
            if line.strip():
                bad_passwords.append(line.strip())
    return bad_passwords


def get_password():
    return getpass.getpass("Введите пароль для проверки --> ")


def password_contains_letters(password):
    letters_amount = 0
    for char in password:
        if char.isalpha():
            letters_amount += 1
    if not letters_amount:
        condition = False
    else:
        condition = True
    return condition



def password_contains_digits(password):
    digits_amount = 0
    for char in password:
        if char.isdigit():
            digits_amount += 1
    if not digits_amount:
        condition = False
    else:
        condition = True
    return condition


def password_is_of_different_case(password):
    chars_in_upper_case = 0
    chars_in_lower_case = 0
    letters_in_password = 0
    for char in password:
        if char.isalpha():
            if char.islower():
                chars_in_lower_case += 1
                letters_in_password += 1
            if char.isupper():
                chars_in_upper_case += 1
                letters_in_password += 1
    if letters_in_password > 0:
        if chars_in_lower_case == letters_in_password or \
                        chars_in_upper_case == letters_in_password:
            condition = False
        else:
            condition = True
    else:
        condition = True

    return condition


def password_length_is_ok(password):
    if len(password) < 8:
        condition = False
    else:
        condition = True
    return condition


def password_contains_special_symbols(password):
    special_symbols_count = 0
    for char in password:
        if char.isalnum():
            pass
        else:
            special_symbols_count += 1
    if not special_symbols_count:
        condition = False
    else:
        condition = True
    return condition


def is_password_silly(password, silly_passwords):
    is_silly = False
    for bad_password in silly_passwords:
        if password in bad_password:
            is_silly = True
        else:
            if bad_password in password:
                is_silly = True
    return is_silly


def count_password_strength(password, silly_passwords):
    strength = 10
    if is_password_silly(password, silly_passwords):
        return 1
    if not password_is_of_different_case(password):
        strength -= 2
    if not password_contains_digits(password):
        strength -= 1
    else:
        pass
    if not password_contains_letters(password):
        strength -= 2
    else:
        pass
    if password_contains_special_symbols(password):
        pass
    else:
        strength -= 1
    if not password_length_is_ok(password):
        strength -= 5
    else:
        pass
    return strength


def main():
    password = get_password()
    silly_passwords = get_blacklist_passwords()
    result_strength = count_password_strength(password, silly_passwords)
    print("Сложность Вашего пароля:", result_strength)


if __name__ == '__main__':
    main()
