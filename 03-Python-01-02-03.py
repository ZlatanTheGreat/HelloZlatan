# 1 Задача от Стринговете-------------------------------------------------------------------------
quote = input()

print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(f'{quote.title()}\n')

# 2 Задача от Стрингове--------------------------------------------------------------------------
replaceable_quote = quote.split()

chose_replacement = int(input("Please choose the number of the word you want to replace: ")) - 1
write_replacement = input("Choose the new word: ")

if chose_replacement > len(replaceable_quote):
    print('Sorry Quote is shorter')
else:
    replaceable_quote[chose_replacement] = write_replacement

print(' '.join(replaceable_quote))

# 3 Задача от Стрингове--------------------------------------------------------------------------
print_size = int(input('Write to where you want to print: '))
print(' '.join(replaceable_quote[:print_size]))