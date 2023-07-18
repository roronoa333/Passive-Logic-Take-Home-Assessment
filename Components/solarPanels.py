import matplotlib.pyplot as plt
from resources import getCityInfo
from numpy import mean

def simulateSolarPanels(city_name, numberOfpanels, totalSurfaceArea,OptToPlot):
    globalHorizontalIrradiance = getCityInfo(city_name)
    panelEffeciency = 0.2                                                                                       # The panel effeicency of modern day solar panels range from 19 to 23 %
    AverageGHI = mean(list(globalHorizontalIrradiance.values())[:-1])
    AverageEnergybyTimeStep = AverageGHI*int(numberOfpanels)*totalSurfaceArea*panelEffeciency*6/24
    energy_generated = {}
    for date, ghi in globalHorizontalIrradiance.items():
        energy_generated[date] = int(ghi)*numberOfpanels*totalSurfaceArea*panelEffeciency
    
    if OptToPlot == 'Y' or OptToPlot == 'y':
        days = list(energy_generated.keys())[:-1]
        energy = list(energy_generated.values())[:-1]
        plt.figure(figsize=(10, 6))  
        plt.plot(days, energy, marker='o')
        plt.xlabel('Day')
        plt.ylabel('Eneregy Generated')
        plt.title('Simulation of Energy Generated by the Solar Panel System over 30 Days')
        plt.xticks(rotation=45)  
        plt.grid(True)
        plt.tight_layout()  
        plt.savefig('Energy Generated by the Solar Panel System.png') 

    return AverageEnergybyTimeStep
