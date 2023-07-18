def getfluidSpecs(fluid):

    ''' Inputs  : Takes the name of the fluid 
        Returns : Properties/Specs of the fluid, currently limited to water '''


    fluidSpecs = {}
    if fluid.lower() == 'water':
        fluidSpecs['density'] = 988         #kg/m^3
        fluidSpecs['specificHeat'] = 4.18   #Watt-second
    return fluidSpecs