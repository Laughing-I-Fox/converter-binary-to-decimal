from colorama import init, Fore, Back, Style
init(autoreset=True)


number = int(input(Style.BRIGHT + Back.YELLOW + Fore.RED + "Please enter your binary number: "))
dec_number = 0
i = 1

while number != 0:
    rem = number % 10
    dec_number = dec_number + (rem * i)
    i = i * 2
    number = int(number / 10)

print(Style.BRIGHT + Back.YELLOW + Fore.GREEN + "Your decimal is:", Fore.GREEN, dec_number)
