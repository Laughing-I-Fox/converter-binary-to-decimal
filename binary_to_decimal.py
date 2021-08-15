number = int(input("Please enter your binary number: "))
dec_number = 0
i = 1

while number != 0:
    rem = number % 10
    dec_number = dec_number + (rem * i)
    i = i * 2
    number = int(number / 10)

print("Your decimal is:", dec_number)
