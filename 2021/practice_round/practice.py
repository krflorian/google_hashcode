
#%%


def write_output(filename, output):
    """
    writes a list of strings to a .out file

    parameters: 
        - output: list of strings 
        - filename: string
    """
    
    filepath = 'data/output_{}.out'.format(filename)
    print('saving file to {}'.format(filepath))
    print(output)

    with open(filepath, "w") as outfile:
        outfile.write("\n".join(output))

    return 



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


#%%

# read data

filename = 'b_little_bit_of_everything.in'
problem = read_data(filename)


# %%
# setup problem 


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


#%%
import pandas as pd 

pizzas = pd.DataFrame(pizza_stack)

pizzas.set_index('id')
pizzas

#%%

ingredient_dummies =  pd.get_dummies(pizzas['ingredients'].apply(pd.Series).stack()).sum(level=0)
pizzas = pizzas.merge(ingredient_dummies, left_index=True, right_index=True)

pizzas['n_ingredients'] = pizzas.apply(lambda x: len(x['ingredients']), axis = 1) 

pizzas


#%%

pizza_stack = []

for pizza in problem['pizzas']:
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

# danach eventuell alle teams nicht satt
# --> nimm random pizzen so viel wie geht
# --> nimm teams pizzen weg falls keine mehr da

for team in team_stack:
    initial_need = team['needs']
    temp_pizza_stack = [pizza for pizza in pizza_stack]
    while team['needs'] > 0:
        pizza = temp_pizza_stack.pop(0)
        team['pizzas'].append(pizza)
        team['needs'] -= 1
        temp_pizza_stack = [p for p in temp_pizza_stack if p['ingredients'] != pizza['ingredients']]
        if len(temp_pizza_stack) == 0:
            print("temp leer")
            break

    if(team['needs'] > 0):
        team['needs'] = initial_need
        team['pizzen'] = []
    else:
        pizza_stack = [p for p in pizza_stack if p not in team['pizzas']]
        if not pizza_stack:
            print("keine pizzen mehr")
            break
       

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


write_output(filename, output)

#%%


  