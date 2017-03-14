import math
import random
import sys

from samplebase import Sample

class ThreeDimensionalSample(Sample):
        """ Sample of using simulated annealing to optimize a two-dimensional data set """
        
        def __init__(self):
                super(ThreeDimensionalSample, self).__init__()
                self.reportPeriod = 500
                self.reportFunction = self.printStatus
                self.alpha = 0.6
                self.initialTemp = 1
                self.maxCount = 10000
                self.minEnergy = 0
                self.setState([(random.randint(0,500), random.randint(0,500), random.randint(0,500)) for i in range(100)])

        def calcDistance(self, left, right):
                """ Simple implementation of calculating the distance between two 2D points
                overrides implementation in parent class to work with 2D distances"""
                
                xDiff = right[0]-left[0]
                yDiff = right[1]-left[1]
                zDiff = right[2]-left[2]
                return math.sqrt((xDiff*xDiff)+(yDiff*yDiff)+(zDiff*zDiff))

if __name__ == '__main__':
        sample = ThreeDimensionalSample()
        if '--show-state' in sys.argv:
                sample.show_state = True
        sample.run()
