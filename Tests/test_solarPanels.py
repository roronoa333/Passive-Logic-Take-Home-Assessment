import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import datetime
from unittest.mock import patch
from Components.solarPanels import simulateSolarPanels
from numpy import mean
import resources
def test_solarPanels():
    with patch('resources.getCityInfo') as mockFunction:
        mockFunction.return_value = {datetime.date(2023, 6, 18): 5379, datetime.date(2023, 6, 19): 13105, datetime.date(2023, 6, 20): 13708, datetime.date(2023, 6, 21): 17623, datetime.date(2023, 6, 22): 15722, datetime.date(2023, 6, 23): 14988, datetime.date(2023, 6, 24): 16996, datetime.date(2023, 6, 25): 17006, datetime.date(2023, 6, 26): 17565, datetime.date(2023, 6, 27): 14907, datetime.date(2023, 6, 28): 11129, datetime.date(2023, 6, 29): 14469, datetime.date(2023, 6, 30): 16630, datetime.date(2023, 7, 1): 17517, datetime.date(2023, 7, 2): 17457, datetime.date(2023, 7, 3): 16007, datetime.date(2023, 7, 4): 11851, datetime.date(2023, 7, 5): 17272, datetime.date(2023, 7, 6): 11196, datetime.date(2023, 7, 7): 15161, datetime.date(2023, 7, 8): 15746, datetime.date(2023, 7, 9): 17574, datetime.date(2023, 7, 10): 17597, datetime.date(2023, 7, 11): 17690, datetime.date(2023, 7, 12): 17265, datetime.date(2023, 7, 13): 17447, datetime.date(2023, 7, 14): 17326, datetime.date(2023, 7, 15): 17297, datetime.date(2023, 7, 16): 17230, datetime.date(2023, 7, 17): 15344, datetime.date(2023, 7, 18): 518}
        globalHorizontalIrradiance = resources.getCityInfo()
        numberOfpanels = 1
        panelEffeciency = 0.2
        totalSurfaceArea = 2
        AverageGHI = mean(list(globalHorizontalIrradiance.values())[:-1])
        AverageEnergybyTimeStep = AverageGHI*int(numberOfpanels)*totalSurfaceArea*panelEffeciency*6/24
        assert simulateSolarPanels('salt lake city',1,2,'n') == AverageEnergybyTimeStep