number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = 0

odd_numbers = 0

for item in range(len(number_list)):
    if number_list[item] % 2 == 0 :
        even_numbers += 1
    else:
        odd_numbers += 1

print(f"Even numbers: {even_numbers}\nOdd numbers: {odd_numbers}")