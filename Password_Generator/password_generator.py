"""
date: 14th February 2024
@author: fafali
"""


import random
import string


# Function to exclude specific character types
def exclude_types(exclude_type, password_length):
    if exclude_type == 'all' or exclude_type == '':
        return generate_random_password(password_length)
    else:
        return generate_password_without_excluded_types(exclude_type)


# Function to generate a random password without excluding any types
def generate_random_password(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))


# Function to generate a password without the excluded types
def generate_password_without_excluded_types(exclude_type):
    if 'letters' in exclude_type:
        characters = string.digits + string.punctuation
    elif 'numbers' in exclude_type:
        characters = string.ascii_letters + string.punctuation
    elif 'symbols' in exclude_type:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))


# Main function to interact with the user and generate the password
def main():
    # Variables
    passcode = ""

    while True:
        try:
            print('________________________________________P A S S W O R D__________________________________________\n')
            password_length = int(input("Please enter the length: "))
            if password_length <=  0:
                raise ValueError("Length must be a positive integer.")
            exclude_type = input("What should I exclude? : ").lower()
            passcode = exclude_types(exclude_type, password_length)
            print(f"\nPassword ---> {passcode}")
            break
        except ValueError as e:
            print(e)
            continue



# Call the main function to run the program
if __name__ == "__main__":
    main()