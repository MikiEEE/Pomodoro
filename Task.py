

class Task(object):
    name = None
    numOfIntervals = 0

    def __init__(self, name):
        self.name = name

    def  __str__(self):
        return {self.name, self.numOfIntervals}

    def completedInterval(self):
        self.numOfIntervals += 1
        return

    def toCSV(self):
         return self.name +','+ str(self.numOfIntervals * 25) + ','
