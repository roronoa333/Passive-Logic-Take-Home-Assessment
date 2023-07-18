from resources import getCityInfo
from simulate import simulate
from Components.pipes import pipeSystem
import Components.solarPanels as solarPanels


def main():

    city_name = input("Enter the city where you want to install the Solar Panel, at this time the system only supports cities in the US : ")
    numberOfpanels = input("Enter Number of Panels you want to Simulate? ")
    numberOfpanels = int(numberOfpanels)
    totalSurfaceArea = 0
    for i in range(numberOfpanels):
        AreaOfthePanel = input("Enter the surface area of panel number " + str(i+1) + " in square meters ")
        AreaOfthePanel = float(AreaOfthePanel)
        totalSurfaceArea = totalSurfaceArea + AreaOfthePanel
    OptToPlot = input("Would you like to plot how the irradience looks like over the span of last month?(y/n)")
    energyGeneartedByTheSystem = solarPanels.simulateSolarPanels(city_name,numberOfpanels,totalSurfaceArea,OptToPlot)

    simulationTime = int(input("Enter the simulation Time in Hours : "))
    if simulationTime < 0:
        print("Time cannot be negetive please enter a valid time ( whole number in hours)")

    simulate(energyGeneartedByTheSystem,simulationTime)

if __name__ == '__main__':
    main()
