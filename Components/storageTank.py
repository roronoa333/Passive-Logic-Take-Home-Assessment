def HeatLostInStorage(internalTemp):

    ''' Inputs : Temperature of the fluid inside the storage tank 
        Returns : Heat lost/dessipated by the stprage tank over a time step '''
    
    Radius = 0.5                                                                        # in meters
    Height = 0.5                                                                        # in meters
    Heat_Transfer_Coefficient = 0.8                                                     # A well thermally insulated storage tank has lower heat transfer coeffecients
    ExternalTemp = 302                                                                  # Kelvin      
    SurfaceArea = Height*3.1439*Radius*2                                                # square meters 
    heatLost = Heat_Transfer_Coefficient*SurfaceArea*(internalTemp - ExternalTemp)
    return heatLost

