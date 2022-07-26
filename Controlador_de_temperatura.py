import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#input
cloth_dirtiness =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_dirtiness') 
cloth_mass =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_mass') 
cloth_sensitivity =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_sensitivity') 

#output
temperatura = ctrl.Consequent(np.arange(0, 81, 1), 'temperatura')
time_process = ctrl.Consequent(np.arange(0, 151, 1), 'time_process')

#degree of dirt
cloth_dirtiness['low'] = fuzz.trimf(cloth_dirtiness.universe, [0, 0, 4])
cloth_dirtiness['medium'] = fuzz.trimf(cloth_dirtiness.universe, [3, 6, 8])
cloth_dirtiness['high'] = fuzz.trimf(cloth_dirtiness.universe, [6, 10, 10])

#clothes weight
cloth_mass['light'] = fuzz.trimf(cloth_mass.universe, [0, 0, 4])
cloth_mass['medium'] = fuzz.trimf(cloth_mass.universe, [3, 6, 8])
cloth_mass['heavy'] = fuzz.trimf(cloth_mass.universe, [6, 10, 10])

#degree of sensitivity
cloth_sensitivity['sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [0, 0, 4])
cloth_sensitivity['pouco sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [3, 5, 8])
cloth_sensitivity['resistente'] = fuzz.trimf(cloth_sensitivity.universe, [6, 10, 10])

#temperature
temperatura['low'] = fuzz.trimf(temperatura.universe, [0, 0, 27])
temperatura['medium'] = fuzz.trimf(temperatura.universe, [20, 34, 45])
temperatura['high'] = fuzz.trimf(temperatura.universe, [40, 55, 70])

#cycle time
time_process['fast'] = fuzz.trimf(time_process.universe, [0, 0, 50])
time_process['normal'] = fuzz.trimf(time_process.universe, [40, 80, 95])
time_process['slow'] = fuzz.trimf(time_process.universe, [80, 120, 130])

#fuzzy set graphics
temperatura.view()
time_process.view()
cloth_dirtiness.view()
cloth_mass.view()
cloth_sensitivity.view()

# if-then rules
rule1 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistente'], temperatura['high'])
rule2 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_mass['heavy'] | cloth_sensitivity['pouco sensivel'], temperatura['medium'])
rule3 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['sensivel'] | cloth_mass['heavy'], temperatura['low'])
rule4 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['pouco sensivel'] & cloth_mass['light'], time_process['fast'])
rule5 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['pouco sensivel'] | cloth_mass['light'], time_process['fast'])
rule6 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['sensivel'] & cloth_mass['heavy'], time_process['slow'])
rule7 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['pouco sensivel'] & cloth_mass['medium'], time_process['normal'])
rule8 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['slow'])
rule9 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['normal'])
rule10 =ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistente'] & cloth_mass['light'], time_process['fast'])
rule11 =ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['fast'])
rule12 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['sensivel'] & cloth_mass['heavy'], time_process['slow'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
tipping.input['cloth_dirtiness'] = 9
tipping.input['cloth_mass'] = 1
tipping.input['cloth_sensitivity']= 4

#temperature output plot
print(tipping.output['temperatura'])
temperatura.view(sim=tipping)
plt.show()

#cycle time output plot
print(tipping.output['time_process'])
time_process.view(sim=tipping)
plt.show()