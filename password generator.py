import random
import string

def generate_password(min_length, include_numbers=True, include_special_characters=True):
    """
    Generates a random password based on the provided criteria.
    
    Args:
        min_length (int): The minimum length of the password.
        include_numbers (bool): Whether to include numbers in the password.
        include_special_characters (bool): Whether to include special characters.
    
    Returns:
        str: The generated password.
    """
    letters = string.ascii_letters  # A-Z and a-z
    digits = string.digits          # 0-9
    special = string.punctuation    # Special characters

    # Start with just letters
    characters = letters

    if include_numbers:
        characters += digits  # Add digits if required

    if include_special_characters:
        characters += special  # Add special characters if required

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # Track if the password contains numbers or special characters
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Determine if the password meets all criteria
        meets_criteria = True

        if include_numbers and not has_number:
            meets_criteria = False  # Must contain at least one number
        if include_special_characters and not has_special:
            meets_criteria = False  # Must contain at least one special character

    return pwd

def main():
    """
    Main function to get user input and generate the password.
    """
    try:
        # Get user input for password requirements
        min_length = int(input("Enter the minimum length of the password: "))
        has_numbers = input("Do you want to have numbers (y/n): ").lower() == 'y'
        has_special = input("Do you want to have special characters (y/n): ").lower() == 'y'

        # Generate the password
        pwd = generate_password(min_length, has_numbers, has_special)
        print(f"The generated password is: {pwd}")

    except ValueError:
        print("Please enter a valid number for the minimum length.")

# Call the main function
if __name__ == "__main__":
    main()
