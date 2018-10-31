# 1-ва
list_numbers = [1, 2, 3, 4]

list_sum = sum(list_numbers)

print(list_sum)

# 2-ра

num_multiplied = 1

for item in range(len(list_numbers)):
    num_multiplied *= list_numbers[item]

print(num_multiplied)

# 3-та

for item in range(len(list_numbers)):
    largest = list_numbers[0]
    if list_numbers[item] > largest:
        largest = list_numbers[item]

print(largest)

# 4-та

letter_list = ['abc', 'xyz', 'aba', '1221']
right_strings = 0
for item in range(len(letter_list)):
    letter_list_item = list(letter_list[item])
    if letter_list_item[0] == letter_list_item[-1]:
        right_strings += 1

print(f'List items that are okay -> {right_strings}')

