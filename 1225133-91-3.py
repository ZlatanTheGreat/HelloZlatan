#class American:
#    def __init__(self):
#
#class NewYourker(American):


num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class convert:
    def __init__(self, number):
        convert.number = number

    @classmethod
    def to_roman(cls, number):
        roman = ''
        while number > 0:
            for a, b in num_map:
                while number >= a:
                    roman += b
                    number -= a
        print(f'Roman is {roman}')


convert.to_roman(235)