#sophiapinkston

def encode(original_password):
    if len(original_password) == 8:
        original_password_list = []
        encoded_password = ""
        original_password_list[:] = original_password
        for digit in original_password_list:
            digit = int(digit)
            digit +=3
            digit = str(digit)
            encoded_password += digit
        return encoded_password

def decode(encoded_password):
    encoded_password_digit_list = []
    og_password_string = ""
    encoded_password_digit_list[:] = encoded_password
    for digit in encoded_password_digit_list:
        digit = int(digit)
        digit -= 3
        digit = str(digit)
        og_password_string += digit
    return og_password_string

def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode ")
    print("2. Decode")
    print("3. Quit")
    print()


if __name__ == "__main__":
    while True:
        display_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!")
            print()
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()
        elif option == 3:
            break
