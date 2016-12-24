class Move:


    def __init__(self, name, power, accuracy, critrate):

        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.critrate = critrate



    def __str__(self):
        return '%s' % (self.name)

    def __repr__(self):
        return '%s' % (self.name)