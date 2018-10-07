elevator = list(map(int, input('Input elevator depths, width, height in that order : ').split()))
fridge = list(map(int, input('Input fridge depths, width, height in that order : ').split()))

depths_elevator= elevator[0]
width_elevator = elevator[1]
height_elevator = elevator[2]

depths_fridge = fridge[0]
width_fridge = fridge[1]
height_fridge = fridge[2]

volume_elevator = depths_elevator * width_elevator * height_elevator
volume_fridge = depths_fridge * width_fridge * height_fridge

if volume_fridge > volume_elevator:
    print("Error - Fridge can't be bigger that the elevator")
else:
    space_left = volume_elevator - volume_fridge
    print(f'Volume left: {space_left}')
    