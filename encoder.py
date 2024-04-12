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

