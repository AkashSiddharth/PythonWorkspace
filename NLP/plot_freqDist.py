from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from clean_text import CleanData
import sys

class FreqencyDistribution:
    def __init__(self, fname):
        # Get clean data
        CD = CleanData(fname)
        self.cleaned_data = CD.clean_coll()
    
    def draw_frame_most_common(self, data_points):
        fdist = FreqDist(self.cleaned_data)
        fdist.most_common(data_points)

        # Plot the graph
        fdist.plot(data_points)

if __name__ == "__main__":
    FD = FreqencyDistribution(sys.argv[1])
    FD.draw_frame_most_common(20)
