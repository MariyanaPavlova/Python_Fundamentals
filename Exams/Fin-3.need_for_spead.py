car_num = int(input())

cars = {}

for i in range(car_num):
    car_input_args = input().split("|")

    # key -> Audi A6 value -> [3800, 62]
    cars[car_input_args[0]] = [int(car_input_args[1]), int(car_input_args[2])]

while True:
    input_command = input()

    if input_command == "Stop":
        break

    command_arg = input_command.split(" : ")
    command_name = command_arg[0]
    car_name = command_arg[1]
    car_data = cars[car_name]

    if command_name == "Drive":
        distance = int(command_arg[2])
        fuel = int(command_arg[3])

        # 50 - > 40
        # 50 - > 50
        # 20 - > 50
        if car_data[1] < fuel:
            print(f"Not enough fuel to make that ride")
            continue
        car_data[0] += distance
        car_data[1] -= fuel
        print(f'{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if car_data[0] >= 100000:
            print(f"Time to sell the {car_name}!")
            cars.pop(car_name)

    elif command_name == "Refuel":
        fuel = int(command_arg[2])
        fuel_to_show = fuel
        old_fuel = car_data[1]
        car_data[1] += fuel
        max_fuel_capacity = 75
        #max 75
        #60+20 = 80 - 75 [15]
        #60+15 = 75 - 75 [15]
        #60+10 = 70 - 70 [10]

        if car_data[1] > max_fuel_capacity:
            car_data[1] = max_fuel_capacity -  car_data[1]
            fuel_to_show = max_fuel_capacity
        print(f'{car_name} refueled with {fuel} liters"')

    elif command_name == "Revert":
        km = int(command_arg[2])
        car_data[0] -= km
        if car_data[0] < 10000:
            car_data[0] = 10000
            continue
        print(f'{car_name} mileage decreased by {km} kilometers')

for name, data in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{name} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.')

