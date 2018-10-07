#5-та зада
money_leva = int(input('Amount in Leva: '))

money_euro = money_leva * 0.5

print(f'Amount in Euro: {int(money_euro)}')

#6-та задача

fifty_euro_notes = money_euro / 50
twenty_euro_notes = money_euro / 20
ten_euro_notes = money_euro / 10
five_euro_notes = money_euro / 5

print(f'Fifty euro notes: {int(fifty_euro_notes)} \nTwenty euro notes: {int(twenty_euro_notes)} \nTen euro notes: {int(ten_euro_notes)} \nFive euro notes: {int(five_euro_notes)}')
