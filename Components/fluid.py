def getfluidSpecs(fluid):
    fluidSpecs = {}
    if fluid.lower() == 'water':
        fluidSpecs['density'] = 988 #kg/L
        fluidSpecs['specificHeat'] = 4.18 #Watt-second
    return fluidSpecs