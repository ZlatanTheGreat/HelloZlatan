# 1-ва задача:
accepted_str = input("Input string:")

def count_numbers_letters(a):
    count_letter = 0
    count_numbers = 0
    splitter_a = a.split()
    for i in range(len(splitter_a)):
        if splitter_a[i].isdigit():
            count_numbers += 1
        else:
            count_letter += 1
    return count_letter, count_numbers


print(count_numbers_letters(accepted_str))