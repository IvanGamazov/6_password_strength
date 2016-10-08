from urllib.request import urlretrieve
import os
from enum import Enum


class SymbolsAmount(Enum):
    zero = 0
    one = 1
    more = 2


class PasswordLength(Enum):
    very_short = -5
    short = -3
    normal = 0


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
    return input("Введите пароль для проверки --> ")


def password_contains_letters(password):
    letters_amount = 0
    for char in password:
        if char.isalpha():
            letters_amount += 1
    if not letters_amount:
        return SymbolsAmount.zero
    if letters_amount >= 2:
        return SymbolsAmount.more
    else:
        return SymbolsAmount.one


def password_contains_digits(password):
    digits_amount = 0
    for char in password:
        if char.isdigit():
            digits_amount += 1
    if not digits_amount:
        return SymbolsAmount.zero
    if digits_amount >= 2:
        return SymbolsAmount.more
    else:
        return SymbolsAmount.one


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
            return False
        else:
            return True
    else:
        return True


def check_password_length(password):
    if len(password) < 6:
        return PasswordLength.very_short
    if len(password) < 8:
        return PasswordLength.short
    else:
        return PasswordLength.normal


def password_contains_special_symbols(password):
    special_symbols_count = 0
    for char in password:
        if char.isalnum():
            pass
        else:
            special_symbols_count += 1
    if not special_symbols_count:
        return False
    else:
        return True


def is_password_silly(password, silly_passwords):
    is_silly = False
    for bad_password in silly_passwords:
        if password.find(bad_password) != -1:
            is_silly = True
        else:
            if bad_password.find(password) != -1:
                is_silly = True
    return is_silly


def count_password_strength(password, silly_passwords):
    strength = 10
    if is_password_silly(password, silly_passwords):
        return 1
    if not password_is_of_different_case(password):
        strength -= 2
    if password_contains_digits(password) == SymbolsAmount.zero:
        strength -= 2
    if password_contains_digits(password) == SymbolsAmount.one:
        strength -= 1
    if password_contains_digits(password) == SymbolsAmount.more:
        pass
    if password_contains_letters(password) == SymbolsAmount.zero:
        strength -= 2
    if password_contains_letters(password) == SymbolsAmount.one:
        strength -= 1
    if password_contains_letters(password) == SymbolsAmount.more:
        pass
    if password_contains_special_symbols(password):
        pass
    else:
        strength -= 1
    if check_password_length(password) == PasswordLength.very_short:
        strength -= 5
    if check_password_length(password) == PasswordLength.short:
        strength -= 3
    if check_password_length(password) == PasswordLength.normal:
        pass
    return strength


def main():
    password = get_password()
    silly_passwords = get_blacklist_passwords()
    result_strength =  count_password_strength(password, silly_passwords)
    print("Сложность Вашего пароля:", result_strength)


if __name__ == '__main__':
    main()
