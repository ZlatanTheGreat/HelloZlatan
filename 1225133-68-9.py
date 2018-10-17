#8-ма задача

import random
import statistics

random_numbers = []

for item in range(0,1001):
    random_numbers.append(random.randint(0, 101))


def avg_vrc_dvt(a):
    avg_vrc_dvt.average = statistics.mean(a)
    avg_vrc_dvt.variance = statistics.variance(a)
    avg_vrc_dvt.std_deviation = statistics.stdev(a)
    print(f'Average: {round(avg_vrc_dvt.average, 2)}\nVariance: {round(avg_vrc_dvt.variance, 2)}\nStandard Deviation: {round(avg_vrc_dvt.std_deviation, 2)}')

#9-та задача
avg_vrc_dvt(random_numbers)

for i in range(5):
    print(f"\n{round(random.normalvariate(avg_vrc_dvt.average,avg_vrc_dvt.std_deviation), 2)}")
