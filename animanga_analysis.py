import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import Pipeline, FeatureUnion
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import constants as const
import glob
import json
import os

class Analyzer:
    def preprocessor(self, summary):
        summary = summary.lower()
        #removes all characters that are not letters and num, sub replaces occurences of pattern with replacement
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
    
    def load_summaries(self, directory):
        summaries = []
        for filename in glob.glob(os.path.join(directory, '*.json')):
            with open(filename, 'r') as f:
                data = json.load(f)
                summaries.append(data['short_summary'])
        return summaries

    def preprocess_summaries(self, summaries):
        preprocessed = []
        for summary in summaries:
            preprocessed

    def build_model(self):
        """Build the model

        Returns
        -------
        sklearn.pipeline.Pipeline
            The model
        """
        pipeline = Pipeline([
            (const.FEATURES, FeatureUnion([

                (const.TEXT_PIPELINE, Pipeline([
                    (const.VECT, CountVectorizer(tokenizer=self.preprocessor)),
                    (const.TFIDF, TfidfTransformer())
                ]))
            ]))
        ])
        
        return pipeline
 
