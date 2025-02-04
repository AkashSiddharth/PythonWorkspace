from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from text_analyze import CleanData
import sys

class FreqencyDistribution:
    def __init__(self, fname):
        # Get clean data
        CD = CleanData(fname)
        self.cleaned_data = CD.clean_coll()

    def get_most_common(self, rtype='obj'):
        fdist = FreqDist(self.cleaned_data)
        mc = fdist.most_common()
        if rtype == 'obj':
            return fdist
        elif rtype == 'list':
            return mc
    
    def plot_most_common(self, data_points):
        common_data = self.get_most_common()

        # Plot the graph
        common_data.plot(data_points)

if __name__ == "__main__":
    FD = FreqencyDistribution(sys.argv[1])
    print(FD.get_most_common('list'))
    FD.plot_most_common(20)
