import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Components import pipes
def test_getHeatLossFromPipes():
        # Define test inputs and expected output
        pipeSpecs = [
            {'length': 2, 'diameter': 0.1},
            {'length': 2, 'diameter': 0.1}
        ]
        internalTemp = 304
        expectedHeatLoss = 10.053088
    
        # Call the function and check the output
        assert pipes.getHeatLossFromPipes(pipeSpecs, internalTemp) == expectedHeatLoss