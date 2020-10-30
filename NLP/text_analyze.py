import nltk, sys
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

class CleanData:
    def __init__(self, fname):
        """ Read the input text to an file-stream obj """
        with open(fname) as inf:
            self.read_text = inf.read()
    
    def break_into_sentences(self):
        """ Break text into sentences, outouts a list of sentences """
        self.sentences = sent_tokenize(self.read_text)

        return self.sentences

    def break_into_words(self):
        """ Breaks sententes in word tokens, outputs a list of words """
        self.break_into_sentences()
        # Tokenize to words
        self.words = list(map(word_tokenize, self.sentences))

        #print(self.words)

        return self.words
    
    def break_into_words_punct(self):
        """ Breaks sententes in word tokens, but separates punctuations, outputs a list of words """
        self.break_into_sentences()
        self.punct_words = list(map(wordpunct_tokenize, self.sentences))

        return self.punct_words
    
    def get_stopwords(self):
        """ Get the list of words that are not very useful in the analysis  """
        return stopwords.words("english")

    def clean_coll(self):
        """ Clean the tokens from stopwords and punctuations """
        # Get all tokens
        _temp = self.break_into_sentences()
        _temp = self.break_into_words()

        #Get the stop words
        stopword = self.get_stopwords()

        # Filter the data
        self.cleaned_data = []
        # Remove punctuations and stopwords
        for word in self.words:
            self.cleaned_data += list(filter(lambda w: w.isalpha() and w.lower() not in stopword, word))

        return self.cleaned_data

class AnalyzeData:
    def analyzer(self, dataset1, dataset2):
        """ Takes 2 lists and prints them side by side """
        for w1, w2 in zip(dataset1, dataset2):
            print('{0} => {1}'.format(w1, w2))
    
    def stem_data(self, data_list: list):
        """ Normalizes the word by truncating the word to its stem word """
        porter = PorterStemmer()
        stemmed_words = []
        #for set_of_words in self.words:
        stemmed_words += list(map(porter.stem, data_list))
        
        return stemmed_words
    
    def lemmatize_data(self, data_list: list, pos_val='n'):
        """ Similar to stemming, but it tries to return dictionary words """
        lemmatizer = WordNetLemmatizer()

        dict_words = list(map(lambda word: lemmatizer.lemmatize(word, pos=pos_val), data_list))
        return dict_words
    
    def tag_pos(self, data_list):
        """ Parts of speech(PoS) tagging """
        pos_tagger = nltk.pos_tag(data_list)

        return pos_tagger

    def chunk(self, data, draw = True):
        """extract meaningful phrases from unstructured text"""
        # ? -> Optional Word/character
        # * -> 0 or more
        grammer = "NP: {<DT>?<JJ>*<NN>}"

        parser = nltk.RegexpParser(grammer)
        tagged_words = self.tag_pos(data)

        output = parser.parse(tagged_words)

        if draw:
            output.draw()

        return output
    
    def chink(self, ):
        """ Chinking excludes a part from the chunk. """
        pass

if __name__ == "__main__":
    CD = CleanData(sys.argv[1])
    words = CD.break_into_words()
    clean_data = CD.clean_coll()

    AD = AnalyzeData()
    #stemmed = AD.stem_data(words)

    # Lemmatize for each sentence
    for set_of_words in words:
        lemmatized_words = AD.lemmatize_data(set_of_words, 'v')
        tagged_words = AD.tag_pos(set_of_words)
        pos_tagged = AD.chunk(set_of_words)

        #AD.analyzer(clean_data, stemmed)
        #AD.analyzer(set_of_words, lemmatized_words)

        print(pos_tagged)
    
    





    

