import random
import string

def generate_password(length):
    # Define character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine character sets based on user preferences
    character_sets = []
    include_lowercase = input("Include lowercase letters? (y/n): ").lower()
    if include_lowercase == 'y':
        character_sets.append(lowercase_letters)

    include_uppercase = input("Include uppercase letters? (y/n): ").lower()
    if include_uppercase == 'y':
        character_sets.append(uppercase_letters)

    include_digits = input("Include digits? (y/n): ").lower()
    if include_digits == 'y':
        character_sets.append(digits)

    include_punctuation = input("Include punctuation? (y/n): ").lower()
    if include_punctuation == 'y':
        character_sets.append(punctuation)

    if not character_sets:
        print("Please select at least one character set.")
        return None

    # Generate the password using the selected character sets
    password_characters = [random.choice(char_set) for char_set in character_sets]
    if len(password_characters) >= length:
        password = ''.join(password_characters[:length])
    else:
        remaining_length = length - len(password_characters)
        additional_characters = [
            random.choice(random.choice(character_sets)) for _ in range(remaining_length)
        ]
        password = ''.join(password_characters + additional_characters)

    return password

# Prompt the user for the desired password length
while True:
    length_str = input("Enter the desired password length: ")
    if length_str.isdigit():
        length = int(length_str)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

# Generate and print the password
password = generate_password(length)
if password:
    print("Generated password:", password)