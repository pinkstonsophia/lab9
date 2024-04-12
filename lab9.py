from encoder import encode
from decoder import decode

def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode ")
    print("2. Decode")
    print("3. Quit")
    print()

if __name__ == "__main__":
    while(True):
        display_menu()
        option = int(input("Please enter an option:"))
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

