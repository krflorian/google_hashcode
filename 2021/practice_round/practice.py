
#%%

def read_data(filename):
    
    pizzas = []
    with open('data/{}'.format(filename), 'r') as infile: 

        number_of_pizzas, teams_of_two, teams_of_three, teams_of_four = map(int, infile.readline().split())

        for _ in range(number_of_pizzas):
            pizza = list(infile.readline().split())
            pizzas.append(pizza)

    problem = {
        'team_2': teams_of_two,
        'team_3': teams_of_three,
        'team_4': teams_of_four,
        'pizzas': pizzas
    }

    return problem 


filename = 'a_example'
problem = read_data(filename)


# %%

problem

problem['pizzas_formated'] = []
for i, data in enumerate(problem['pizzas']):

    problem['pizzas_formated'].append({
        'number_of_pizzas': int(data[0]),
        'ingredients': data[1:],
        'id': i
    })

problem['pizzas'] = problem['pizzas_formated']
del problem['pizzas_formated']
problem

# %%


pizza_count = 0
for pizza in problem['pizzas']:
    pizza_count += pizza['number_of_pizzas']
pizza_count

#%%

pizza_stack = []

for pizza in problem['pizzas']:
    for _ in range(pizza['number_of_pizzas']):
        pizza_stack.append({
            'id': pizza['id'],
            'ingredients': pizza['ingredients']})


pizza_stack = sorted(pizza_stack, key=len, reverse=True)
pizza_stack

#%%

team_stack = []

for _ in range(problem['team_2']):
    team_stack.append({
        'needs': 2,
        'pizzas': []
    })

for _ in range(problem['team_3']):
    team_stack.append({
        'needs': 3,
        'pizzas': []
    })

for _ in range(problem['team_4']):
    team_stack.append({
        'needs': 4,
        'pizzas': []
    })


team_stack

#%%


for team in team_stack:
    while team['needs'] > 0:
        pizza = pizza_stack.pop(0)
        team['pizzas'].append(pizza)
        team['needs'] -= 1

team_stack


#%%

# output

teams_served = [team for team in team_stack if team['needs'] == 0]

output = []
output.append(str(len(teams_served)))
for team in teams_served:
    line = str(len(team['pizzas'])) + ' '
    line += ' '.join([str(pizza['id']) for pizza in team['pizzas']])
    output.append(line)


output

#%%


with open('data/output_{}.out'.format(filename), "w") as outfile:
  outfile.writelines(output)


  