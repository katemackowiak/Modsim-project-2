import modsim
import csv
coeffile = 'coefficientofthermalexpansion.csv'

def step(params,state):
    '''one step of the simulation'''
    c = "SOMETHING" #need to figure out if this can just be a constant or we need to also have different ones for different salinities
    delta_temp = params[delta_energy]/(params[mass]*c)
    state['energy'] += params[delta_energy]
    state['temp'] += delta_temp
    state['beta'] = 0#THIS NEEDS TO TAKE IN THE STUFF FROM THE CSV, PROB NEED TO ORGANIZE IT BETTER
    state['volume'] += state['volume'] * state['beta'] * delta_temp
    return(state)

'''gets the coefficients and stores them'''
temperatures = []
salinity = []
coefficients = [] #rows - salinity, columns - temperatures
initialRow = True
with open(coeffile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        row = row[0].split(',')
        if initialRow == False:
            salinity.append(row[0])
            coefficients.append(row[1:])
        else:
            temperatures = row
            initialRow = False 

'''sets up the parameters'''
params = {}
params['salinity'] = 10 #salinity in percentage
params['start_temp'] = -2 #temperature in degrees celcius
params['mass'] = 10 #mass in kg
params['delta_energy'] = 1 #energy added in each step
params['length_of_simulation'] = 20 #number of steps to run

'''sets up variables'''
state = {}
state['energy'] = 0
state['temp'] = params['start_temp']
state['volume'] = 0
state['beta'] = 0

'''actually running the simulation, not in a function for ease of aquiring and graphing stuff'''
state['volume'] = 'how tf does one find the inital density??>?>?>?????' #the internet is not helpful
energy = []
temp = []
volume = []
for i in range(params[length_of_simulation]):
    state = step(params,state)
    energy.append(state['energy'])
    temp.append(energy['temp'])
    volume.append(energy['volume'])

plt.plot(energy,temp)
plt.y_label('temperature (degrees celcius)')
plt.x_label('energy (joules)')
