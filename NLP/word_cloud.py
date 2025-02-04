from wordcloud import WordCloud
from matplotlib import pyplot as plt
from text_analyze import CleanData
from PIL import Image
import numpy as np
import sys

class WCloud:
    """ This class will generate word cloud from any tet file passed to it """
    def __init__(self, fname):
        # get cleaned data
        CD = CleanData(fname)
        self.cleaned_data = CD.clean_coll()
    
    def generate_wordcloud(self, shape='default'):
        if shape == 'circle':
            char_mask = np.array(Image.open("images/circle.png"))
        else:
            char_mask = None

        wc = WordCloud(background_color='black', mask=char_mask).generate(' '.join(self.cleaned_data))

        plt.figure(figsize = (10, 10))
        plt.imshow(wc)
        
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    WC = WCloud(sys.argv[1])
    WC.generate_wordcloud('circle')

        



