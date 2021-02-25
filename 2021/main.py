

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
        streets.append(Street(start, end, name, time_needed))
    for i in range(n_cars):
        car_data = infile.readline().split()
        cars.append(
            Car(i, car_data[1:])
        )



cars

#%%

cars[1].__dict__


# %%


streets[0].__dict__


# %%
