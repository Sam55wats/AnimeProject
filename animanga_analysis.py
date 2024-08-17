import re
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import constants as const

class Analyzer:
    def preprocessor(summary):
        summary = summary.lower()
        #removes all characters that are not letters and num, sub replaces occurences of pattern in string with replacement
        summary = re.sub("[^a-zA-Z0-9]", " ", summary) # ^ is negation
        tokens = word_tokenize(summary) #splits text into individual words

        #filters out words that are considered stopwords
        tokens = [w for w in tokens if w not in stopwords.words(const.ENGLISH)]

        lemmatizer = WordNetLemmatizer() 
        stemmer = PorterStemmer()

        clean_tokens = []
        for tok in tokens:
            lemmatizer_tok = lemmatizer.lemmatize(tok).strip()
            clean_tok = stemmer.stem(lemmatizer_tok)
            clean_tokens.append(clean_tok)

        return clean_tokens

