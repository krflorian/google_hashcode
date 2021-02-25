

#%%

filename = 'e'


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
"""

for car in cars:
    car.total_duration = sum([streets[idx].time_needed for idx in streets])

cars[1].__dict__
"""

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
            (idx, intersections[idx]['incoming'][0].name, 1))

schedule


#%%

output = []
output.append(
    str(len(schedule)))

for s in schedule: 
    output.append(str(s[0]))
    output.append('1')
    output.append(' '.join(map(str, s[1:])))

output


#%%

out_filepath = filename + '_out'

with open('{}.txt'.format(out_filepath), "w") as outfile:
    outfile.write("\n".join(output))

