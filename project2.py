import modsim
import csv
import matplotlib.pyplot as plt
coeffile = 'project 2\coefficientofthermalexpansion.csv'

def step(params,state):
    '''one step of the simulation'''
    delta_temp = params['delta_energy']/(params['mass']*params['c'])
    state['energy'] += params['delta_energy']
    state['temp'] += delta_temp
    sal = 0
    tem = 0
    for i in range(len(salinity)):
        if i == params['salinity']:
            sal = i
    for i in range(len(temperatures)):
        if i == params['salinity']:
            tem = i
    state['beta'] = coefficients[sal][tem]#THIS NEEDS TO TAKE IN THE STUFF FROM THE CSV, PROB NEED TO ORGANIZE IT BETTER
    state['volume'] += state['volume'] * state['beta'] * delta_temp
    return(state)

def find_initial_density(salinity):
    '''gives the initial density of the water based on its salinity'''
    return .9999030511*1.000801967**salinity

'''gets the coefficients and stores them'''
temperatures = []
salinity = []
coefficients = [] #rows - salinity, columns - temperatures
initialRow = True
with open(coeffile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row_not_float in reader:
        row_not_float = row_not_float[0].split(',')
        row = []
        for i in row_not_float:
            row.append(float(i))
        if initialRow == False:
            salinity.append(row[0])
            coefficients.append(row[1:])
        else:
            temperatures = row
            initialRow = False 

if __name__ == '__main__':
    '''sets up the parameters'''
    params = {}
    params['salinity'] = 10 #salinity in percentage
    params['start_temp'] = -2 #temperature in degrees celcius
    params['mass'] = 10 #mass in kg
    params['delta_energy'] = 1 #energy added in each step
    params['length_of_simulation'] = 20 #number of steps to run
    params['c'] = 3.5   #CONSTANT

    '''sets up variables'''
    state = {}
    state['energy'] = 0
    state['temp'] = params['start_temp']
    state['volume'] = 0
    state['beta'] = 0

    '''actually running the simulation, not in a function for ease of aquiring and graphing stuff'''
    state['volume'] = params['mass']/find_initial_density(params['salinity'])
    energy = []
    temp = []
    volume = []
    for i in range(params['length_of_simulation']):
        state = step(params,state)
        energy.append(state['energy'])
        temp.append(state['temp'])
        volume.append(state['volume'])

    plt.plot(energy,volume)
    plt.ylabel('temperature (degrees celcius)')
    plt.xlabel('energy (joules)')
    plt.show()
