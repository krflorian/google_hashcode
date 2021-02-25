

#%%

filename = 'c'


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
popularity = {}


def add_to_dict(name: str):
    global popularity
    if name in popularity:
        popularity[name]+=1
    else:
        popularity[name] = 1


def get_most_popular_street(streets):
    global popularity
    for street in streets:
        [add_to_dict(street.name) for car in cars if street.name in car.path]

    return popularity

#%%

schedule = []


for idx in intersections: 
    if len(intersections[idx]['incoming']) == 1:
        schedule.append(
            (idx, [(intersections[idx]['incoming'][0].name, 1)]))
    else:
        popularity = get_most_popular_street(intersections[idx]['incoming'])
        verhaeltnis_koeff = total_duration/(sum(popularity.values())*10)
        # Raphael explains later
        multi_streets = []
        for thing in intersections[idx]['incoming']:
            if thing.name in popularity:
                dauer_thing = max(1,int(popularity[thing.name]*verhaeltnis_koeff))
                multi_streets.append((thing.name, dauer_thing))

        schedule.append((idx, multi_streets))

schedule


#%%

output = []
# output.append(
#     str(len(schedule)))
counter = 0
for s in schedule:
    if len(s[1]) != 0:
        counter+=1
        output.append(str(s[0]))
        output.append(str(len(s[1])))
        for beautiful_street in s[1]:
            output.append(' '.join(map(str, beautiful_street)))
output.insert(0, str(counter))

output


#%%

out_filepath = filename + '_out'

with open('{}.txt'.format(out_filepath), "w") as outfile:
    outfile.write("\n".join(output))

