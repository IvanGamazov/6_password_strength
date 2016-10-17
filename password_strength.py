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
    return letters_amount > 0


def password_contains_digits(password):
    digits_amount = 0
    for char in password:
        if char.isdigit():
            digits_amount += 1
    return digits_amount > 0


def password_is_of_different_case(password):
    chars_in_upper_case = 0
    chars_in_lower_case = 0
    alphas_in_password = 0
    for char in password:
        if char.islower() and char.isalpha():
            chars_in_lower_case += 1
            alphas_in_password += 1
        if char.isupper() and char.isalpha():
            chars_in_upper_case += 1
            alphas_in_password += 1
    alphas_in_one_case = chars_in_lower_case == alphas_in_password or \
                  chars_in_upper_case == alphas_in_password
    return alphas_in_password <= 0 or not alphas_in_one_case


def password_length_is_ok(password):
    return len(password) >= 8


def password_contains_special_symbols(password):
    special_symbols_count = 0
    for char in password:
        if not char.isalnum():
            special_symbols_count += 1
    return special_symbols_count > 0


def is_password_silly(password, silly_passwords):
    is_silly = False
    for bad_password in silly_passwords:
        if password in bad_password or bad_password in password:
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
    if not password_contains_letters(password):
        strength -= 2
    if not password_contains_special_symbols(password):
        strength -= 1
    if not password_length_is_ok(password):
        strength -= 5
    return strength

if __name__ == '__main__':
    password = get_password()
    silly_passwords = get_blacklist_passwords()
    result_strength = count_password_strength(password, silly_passwords)
    print("Сложность Вашего пароля:", result_strength)