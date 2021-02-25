

#%%

filename = 'b'


class Street():
    def __init__(self, start, end, name, time_needed):
        self.start =start
        self.end = end
        self.name = name
        self.time_needed = time_needed

class Car():
    def __init__(self, id, path):
        self.id = id
        self.path = path

streets = []
cars = []


#%%

with open('{}.txt'.format(filename), 'r') as infile: 

    total_duration, n_intersections, n_streets, n_cars, bonus_points = map(int, infile.readline().split())

    for _ in range(n_streets):
        start, end, name, time_needed = infile.readline().split()
        streets.append(Street(int(start), int(end), name, int(time_needed)))
    for i in range(n_cars):
        car_data = infile.readline().split()
        cars.append(
            Car(i, car_data[1:])
        )

cars

#%%

streets_dict = {}

for street in streets: 
    streets_dict[street.name] = street.time_needed
streets_dict


#%%

for car in cars:
    car.total_duration = sum([streets_dict[street] for street in car.path[1:]])

cars[1].__dict__

#%%

import pandas as pd 

car_values = pd.DataFrame()

for car in cars:
    car_values = car_values.append(pd.DataFrame({
        'id': car.id, 
        'total_duration': car.total_duration
    }, index = [car.id]))

car_values

#%%

car_values = car_values.loc[car_values['total_duration'] <= total_duration]

car_values = car_values.sort_values('total_duration', ascending = True)

if len(cars) > 100:
    car_values = car_values.iloc[:int(len(cars)/10)]

car_values

#%%

high_value_streets = set()

for car in cars: 
    if car.id in list(car_values.index):
        for street in car.path: 
            high_value_streets.add(street)

high_value_streets

#%%

intersections = {}
for i in range(n_intersections):
    intersections[i] = {
        'incoming': [],
        'outgoing': []}

for street in streets: 
    intersections[street.start]['outgoing'].append(street)
    intersections[street.end]['incoming'].append(street)

intersections

#%%

schedule = []


for idx in intersections: 
    if len(intersections[idx]['incoming']) == 1:
        schedule.append(
            (idx, [(intersections[idx]['incoming'][0].name, 1)]))
    else:
        # Raphael explains later
        multi_streets = []
        for thing in intersections[idx]['incoming']:
            multi_streets.append((thing.name, 1))
        schedule.append((idx, multi_streets))

schedule


#%%

output = []
output.append(
    str(len(schedule)))

for s in schedule: 
    output.append(str(s[0]))
    output.append(str(len(s[1])))
    for beautiful_street in s[1]:
        output.append(' '.join(map(str, beautiful_street)))

output


#%%

out_filepath = filename + '_out'

with open('{}.txt'.format(out_filepath), "w") as outfile:
    outfile.write("\n".join(output))

