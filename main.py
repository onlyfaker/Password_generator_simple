#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sum_of_characters = nr_numbers+nr_symbols+nr_letters

while sum_of_characters>0:
    choice = random.randint(0, 2)
    if choice==0:
        if nr_letters>0:
            random_letter = random.choice(letters)
            password.append(random_letter)
            nr_letters-=1
            sum_of_characters-=1
    elif choice==1:
        if nr_numbers>0:
            random_num = random.choice(numbers)
            password.append(random_num)
            nr_numbers-=1
            sum_of_characters-=1

    elif choice==2:
        if nr_symbols>0:
            random_sym = random.choice(symbols)
            password.append(random_sym)
            nr_symbols-=1
            sum_of_characters-=1

string_pass = ''.join(password)
print(f"Your pasword is: {string_pass}")