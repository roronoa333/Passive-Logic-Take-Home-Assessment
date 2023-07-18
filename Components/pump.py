def EnergyForPump(pipeSpecs,time):
    pipeLength = pipeSpecs[0]["length"]
    pipeDiameter = pipeSpecs[0]["diameter"]
    frictionFactor = 0.025
    density = 998
    flowVelocity = pipeLength/time
    pressureDelta = pipeLength*frictionFactor*density*flowVelocity**2/(2*pipeDiameter)
    energyRequired = pressureDelta*(0.25*3.14159*pipeDiameter**2)*pipeLength
    return energyRequired