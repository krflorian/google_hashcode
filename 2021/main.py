

#%%

filename = 'a'


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

cars[1].__dict__

for car in cars:
    car.total_duration = sum([streets[idx].time_needed for idx in streets])


cars[0].__dict__

# %%


class Intersection():
    def __init__(self, id, schedule):
        self.id = id
        self.schedule = [] # (street_name, time)


#%%

intersections = []
for i in range(n_intersections):
    intersections.append(
        Intersection(i, []))


#%%

for idx in streets:
    streets[idx].start


#%%


[i for i in intersections ]


for step in range(total_duration):


#%%

intersections = {}
for i in range(n_intersections):
    intersections[i] = {
        'incoming': 0,
        'outgoing': 0}

for street in streets: 
    intersections[street.start]['outgoing'] += 1
    intersections[street.end]['incoming'].append()

intersections

#%%

schedule = []

for idx in intersections: 
    if intersections[idx]['incoming'] == 1:
        schedule.append()
