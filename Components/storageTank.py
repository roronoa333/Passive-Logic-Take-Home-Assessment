def HeatLostInStorage(internalTemp):
    Radius = 0.5            # in meters
    Height = 0.5            # in meters
    Heat_Transfer_Coefficient = 0.8     #A well thermally insulated storage tank has lower heat transfer coeffecients
    ExternalTemp = 302
    SurfaceArea = Height*3.1439*Radius*2
    heatLost = Heat_Transfer_Coefficient*SurfaceArea*(internalTemp - ExternalTemp)
    return heatLost

