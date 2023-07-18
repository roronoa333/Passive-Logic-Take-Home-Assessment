def pipeSystem():

    ''' Helps the user by creating pipe objects to facilitate fluid transfer '''

    PanelToPump = {}
    PumpToStorage = {}
    StorageToPanel = {}
    GenericPipes = input("Shall we use default pipe dimensions for all pipe components?(y/n)")
    if GenericPipes == 'Y' or GenericPipes == 'y':
        PanelToPump['diameter'] = 0.1       # meters
        PanelToPump['length'] = 2           # meters
        PumpToStorage['diameter'] = 0.1     # meters
        PumpToStorage['length'] = 2         # meters
        StorageToPanel['diameter'] = 0.1    # meters
        StorageToPanel['length'] = 4        # meters
    else:
        print("For simplicity, let us assume all pipes are made of steel")
        PanelToPump['length'] = input("Please enter the length of the pipe that run from the panel to the pump in meters")
        PumpToStorage['length'] = input("Please enter the length of the pipe that run from the pump to storage in meters")
        StorageToPanel['length'] = input("Please enter the length of the pipe that run from the pump to storage in meters")

    pipeSpecs = [PanelToPump,PumpToStorage,StorageToPanel]                                                                  

    return pipeSpecs

def getHeatLossFromPipes(pipeSpecs, internalTemp):

    ''' Takes in pipeSpecs and internal temperature to return 
        heat lost to the environment over a time step 
        NOTE : This ignores all the bends / turns in the pipes '''

    h = 4                                                                                                       #Heat coeffecient
    externalTemp = 302                                                                                          #For simplicity, let us consider external temperature to be 302 Kelvin and heat transfer coefficient is 4 and there is no heat loss from the pipe connecting storage outlet to the Panel")

    totalSurfaceArea = (pipeSpecs[0]['length'] + pipeSpecs[1]['length'])*(pipeSpecs[0]['diameter']*3.14159)

    HeatLossFromPipes = h*totalSurfaceArea*(internalTemp-externalTemp)

    return HeatLossFromPipes
        