#Q

'''Salt water makes up 97.5% of the total water concentration on Earth. It is hit by every factor that affects the Earth, from heat, to pollution, to invasive species affecting an existing ecosystem. We chose to study how heat added to the ocean impacts its volume, with particular regards to how the density changes as water temperature does. Our question was how much does salt water expand as it absorbs heat, and how does that expansion impact sea level rise?     

M

For our model parameters we had salinity, starting temperature, mass, surface area, and the net power put into each square meter of water. We found values for the surface area, mass and average salinity and temperature of the upper 2000m ocean since that layer changes temperature the most drastically, thus its density changes the most as well. '''


import modsim
import csv
coeffile = 'coefficientofthermalexpansion.csv'


'''In each step of the model we update the time and energy based on the parameters from the beginning. We found the change in temperature based on the equation ΔU = mcΔt and using the change in energy calculated from before. Then, we found the coefficient of thermal expansion for the specific salinity and temperature of the water, which is represented by the value ‘beta’. Using the beta value we calculate the change in volume and change in density of the sea water.

We keep track of the temperature, volume, and density changes over time throughout the hundred year span of our model. We used the volume changes and an approximate value to correlate the volume change to sea level rise. '''


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

'''R 

We decided to have separate graphs for volume, temperature, density, and sea level rise, with all our dependant variables being accounted for in relation to time. We accounted for time in years, and with time increasing, our model showed volume, ocean temperature, and sea level rising at a close to linear rate, while density decreased at a similar rate. 



I


In general, our results seem to align with the goal of our model fairly well. Volume, temperature, and sea level all rise with respect to time, while density decreases. Some of our values are slightly deviated from what we expected, such as our temperature value being so high, but we have to take human error into account. We used multiple different websites with multiple values to get the data for our project, which is a very plausible solution to our weird values.'''
