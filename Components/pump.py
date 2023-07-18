def EnergyForPump(pipeSpecs,time):

    ''' Takes in the pipe specifications and duration of the time step and returns the 
        energy required to pump water horizontally from the panel to the storage tank '''

    pipeLength = pipeSpecs[0]["length"]
    pipeDiameter = pipeSpecs[0]["diameter"]
    frictionFactor = 0.025                                                                  # unit less
    density = 998                                                                           # Kg/m^3
    flowVelocity = pipeLength/time                                                          # m/s
    pressureDelta = pipeLength*frictionFactor*density*flowVelocity**2/(2*pipeDiameter)      # N/m^2
    energyRequired = pressureDelta*(0.25*3.14159*pipeDiameter**2)*pipeLength
    return energyRequired