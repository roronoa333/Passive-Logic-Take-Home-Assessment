import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Components import storageTank
def test_HeatLostInStorage():
    heatLost = 123.24088
    assert storageTank.HeatLostInStorage(400) == heatLost