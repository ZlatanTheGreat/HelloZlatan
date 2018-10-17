sentence = input('Enter sentence: ')
lower_letters = 0
upper_letters = 0

for item in range(len(sentence)):
    if sentence[item].islower():
        lower_letters += 1
    elif sentence[item].isupper():
        upper_letters += 1

print(lower_letters,upper_letters)