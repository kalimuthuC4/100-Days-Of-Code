import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-']


nr_letters = int(input("enter the letters you want in your password\n"))
nr_numbers = int(input("enter the numbers you want in your password\n"))
nr_symbols = int(input("enter the symbols you want in your password\n"))


password_list = []

for passletter in range(1,nr_letters + 1):
    password_list += random.choice(letters)

for passletter in range(1,nr_numbers + 1):
    password_list += random.choice(numbers)

for passletter in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)


password = " "
for char in password_list:
    password += char

print(password)