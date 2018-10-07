#най - вероятно е грешна задачата
#дейба нейната мама

import math

distance = 20
deviation_north = math.radians(60)
deviation_east = math.radians(30)

north_distance = math.sin(deviation_north) * distance
east_distance = math.sin(deviation_east) * distance

print(f'North distance: {round(north_distance, 2)}\nEast Distance: {round(east_distance, 2)}')