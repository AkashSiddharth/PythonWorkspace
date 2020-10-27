import nltk, sys
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

class CleanData:
    def __init__(self, fname):
        with open(fname) as inf:
            self.read_text = inf.read()
    
    def break_into_sentences(self):
        self.sentences = sent_tokenize(self.read_text)

    def break_into_words(self):
        self.words = []
        # Tokenize to words
        for sentence in self.sentences:
            self.words += word_tokenize(sentence)

    def clean_coll(self):
        # Get all tokens
        self.break_into_sentences()
        self.break_into_words()

        #Get the stop words
        stopword = stopwords.words("english")

        # Filter the data
        # Remove punctuations and stopwords
        self.cleaned_data = list(filter(lambda w: w.isalpha() and w.lower() not in stopword, self.words))

        return self.cleaned_data

if __name__ == "__main__":
    CD = CleanData(sys.argv[1])
    clean_data = CD.clean_coll()
    print(clean_data)





    

