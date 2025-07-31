import random
import string

def gen_password(lenght , numbers , letters , symbols):
    char = ''

    if numbers:
        char += string.digits
    if letters:
        char += string.ascii_letters
    if symbols:
        char += string.punctuation

    if not char:
        return "Select at least 1 type of symbols"

    password=("".join(random.choice(char)for _ in range (lenght)))

    return password


try:
    length=int(input("Write length of your password: "))
    if length<=0 or not length.is_integer():
        print("Error")
    else:
        letters = input("Include letters?yes/no: ").lower() == "yes"
        numbers = input("Include numbers?yes/no: ").lower() == "yes"
        symbols = input("Include symbols?yes/no: ").lower() == "yes"

        password=gen_password(length, numbers ,  letters , symbols)
        print(f"Your password: {password}")
except ValueError:
    print("Error!")

