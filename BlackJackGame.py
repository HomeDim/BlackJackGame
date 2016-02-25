class Card(object):
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def getRank(self):
        return self.rank

    def getSuite(self):
        return self.suite

    def __str__(self):
        return '{0} of {1}'.format(self.rank, self.suite)