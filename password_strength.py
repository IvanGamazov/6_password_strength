def get_blacklist_passwords(file_path):
    bad_passwords = []
    with open(file_path) as blacklist:
        for line in blacklist:
            bad_passwords.append(line.strip())
        return bad_passwords


def get_password():
    return input("Enter password to know it's strength --> ")


def password_contains_letters(password):
    letters_amount = 0
    for char in password:
        if char.isalpha():
            letters_amount += 1
    if not letters_amount:
        return -2
    if letters_amount >= 2:
        return 0
    else:
        return -1


def password_contains_digits(password):
    digits_amount = 0
    for char in password:
        if char.isdigit():
            digits_amount += 1
    if not digits_amount:
        return -2
    if digits_amount >= 2:
        return 0
    else:
        return -1


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
            return -2
        else:
            return 0
    else:
        return 0


def check_password_length(password):
    if len(password) < 6:
        return -5
    if len(password) < 8:
        return -3
    else:
        return 0


def password_contains_special_symbols(password):
    special_symbols_count = 0
    for char in password:
        if char.isalnum():
            pass
        else:
            special_symbols_count += 1
    if not special_symbols_count:
        return -1
    else:
        return 0


def is_password_silly(password, silly_passwords, strength):
    is_silly = strength
    for bad_password in silly_passwords:
        if password.find(bad_password)!=-1:
            is_silly = 1
        else:
            if bad_password.find(password)!=-1:
                is_silly = 1
    return is_silly


def main():
    password = get_password()
    file_path = input("Enter path to blacklist passwords file --> ")
    silly_passwords = get_blacklist_passwords(file_path)
    strength = 10
    strength += password_is_of_different_case(password)
    strength += password_contains_digits(password)
    strength += password_contains_letters(password)
    strength += check_password_length(password)
    strength += password_contains_special_symbols(password)
    result_strength = is_password_silly(password, silly_passwords, strength)
    print("The strength of your password is ", result_strength)


if __name__ == '__main__':
    main()
