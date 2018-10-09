score = float(input('Enter a score between 0.0 and 1.0: '))

if score <= 1:
    if score >= 0.9:
        print('Score: A')
    elif score >= 0.8:
        print('Score: B')
    elif score >= 0.7:
        print('Score: C')
    elif score >= 0.6:
        print('Score: D')
    else:
        print('Score: F')