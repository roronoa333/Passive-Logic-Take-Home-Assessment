def pipeSystem():
    PanelToPump = {}
    PumpToStorage = {}
    StorageToPanel = {}
    GenericPipes = input("Shall we use default pipe dimensions for all pipe components?(y/n)")
    if GenericPipes == 'Y' or GenericPipes == 'y':
        PanelToPump['diameter'] = 0.1
        PanelToPump['length'] = 2
        PumpToStorage['diameter'] = 0.1
        PumpToStorage['length'] = 2
        StorageToPanel['diameter'] = 0.1
        StorageToPanel['length'] = 4
    else:
        print("For simplicity, let us assume all pipes are made of steel")
        PanelToPump['length'] = input("Please enter the length of the pipe that run from the panel to the pump in meters")
        PumpToStorage['length'] = input("Please enter the length of the pipe that run from the pump to storage in meters")
        StorageToPanel['length'] = input("Please enter the length of the pipe that run from the pump to storage in meters")

    pipeSpecs = [PanelToPump,PumpToStorage,StorageToPanel]                                                                  #Fix This

    return pipeSpecs

def getHeatLossFromPipes(pipeSpecs, internalTemp):

    #For simplicity, let us consider ambient temperature to be 272 Kelvin and heat transfer coefficient is 4 and there is nbo heat loss from the pipe connecting storage outlet to the Panel")
    h = 4                                                                                                                   #Heat coeffecient
    externalTemp = 302
    totalSurfaceArea = (pipeSpecs[0]['length'] + pipeSpecs[1]['length'])*(pipeSpecs[0]['diameter']*3.14159)

    HeatLossFromPipes = h*totalSurfaceArea*(internalTemp-externalTemp)

    return HeatLossFromPipes
        