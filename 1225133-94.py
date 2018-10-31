class Power:
    def __init__(self, number, power):
        Power.number = number
        Power.power = power

    @classmethod
    def to_Power(cls, number, power):
        result = pow(number, power)
        print(f'{number} to the power of {power} is  -> {result}')


Power.to_Power(2,4)