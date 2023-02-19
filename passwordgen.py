import random
import string

def generate_password(length, complexity):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Define sets of characters based on selected complexity
    if complexity == 1:  # Only lowercase letters
        char_set = lowercase
    elif complexity == 2:  # Lowercase letters and digits
        char_set = lowercase + digits
    elif complexity == 3:  # Lowercase letters, uppercase letters, and digits
        char_set = lowercase + uppercase + digits
    elif complexity == 4:  # Lowercase letters, uppercase letters, digits, and symbols
        char_set = lowercase + uppercase + digits + symbols
    else:
        raise ValueError("Invalid complexity level")

    # Generate password
    password = ''.join(random.SystemRandom().choice(char_set) for i in range(length))
    return password

print(generate_password(int(input("Enter desired length of password: ")), int(input("Complexities: \n1. Only lowercase letters\n2. Lowercase letters and digits\n3. Lowercase letters, uppercase letters, and digits\n4. Lowercase letters, uppercase letters, digits, and symbols\n"))))
