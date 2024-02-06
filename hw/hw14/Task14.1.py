import json

with open("cars.json", "r") as file_cars:
    cars_data = json.load(file_cars)

with open("cars2.json", "r") as file_cars2:
    car2_data = json.load(file_cars2)

cars_data.append(car2_data)

sorted_cars = sorted(cars_data, key=lambda x: x["max_speed"])

with open("result.json", "w") as result_file:
    json.dump(sorted_cars, result_file, indent=4)