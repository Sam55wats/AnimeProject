import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import constants as const
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import glob
import json
import os
from collections import Counter
import string
import glob
import os

class Analyzer():
    def get_word_frequencies(self, summary, count):
        summary = summary.translate(str.maketrans('','', string.punctuation))

        split_summary = summary.split() 

        split_summary = [x.lower() for x in split_summary]

        counter = Counter(split_summary)

        frequencies = counter.most_common(count)

        return frequencies

    def character_appearances(directory):
        character_appearances = {}

        for filename in glob.glob(os.path.join(directory, '*.json')):
            with open(filename, 'r') as f:
                data = json.load(f)

                number = data['number']

                for character in data.get('characters', []):
                    if character not in character_appearances:
                        character_appearances[character] = []
                    character_appearances[character].append(number)
        
        return character_appearances
    
    def preprocessor(self, summary):
        summary = summary.lower()
        #removes all characters that are not letters and num, sub replaces occurences of pattern with replacement
        summary = re.sub("[^a-zA-Z0-9]", " ", summary) # ^ is negation
        tokens = word_tokenize(summary) #splits text into individual words

        #filters out words that are considered stopwords
        tokens = [w for w in tokens if w not in stopwords.words('english')]

        lemmatizer = WordNetLemmatizer() 

        clean_tokens = []
        for tok in tokens:
            clean_tok = lemmatizer.lemmatize(tok).strip()
            clean_tokens.append(clean_tok)

        return clean_tokens
    
    def load_summaries(self, directory, count = 10):
        summaries = []

        for filename in glob.glob(os.path.join(directory, '*.json'))[:count]:
            with open(filename, 'r') as f:
                data = json.load(f)
                summaries.append(data['long_summary'])

        return summaries
        
    def preprocess_summaries(self, summaries):
        preprocessed = []

        for summary in summaries:
            preprocessed.append(' '.join(self.preprocessor(summary)))
                                
        return preprocessed

    def vectorize_summaries(self, summaries):
        vectorizer = TfidfVectorizer()
        return vectorizer.fit_transform(summaries)
    
    def cosine_sim(self, anime_summaries, manga_summaries, anime_labels, manga_labels):
        combined_summaries = anime_summaries + manga_summaries
        
        vectors = self.vectorize_summaries(combined_summaries)

        anime_vect = vectors[:len(anime_summaries)]
        manga_vect = vectors[len(anime_summaries):]

        similarity_matrix = cosine_similarity(anime_vect, manga_vect)

        similarity_table = pd.DataFrame(
            similarity_matrix, 
            index=anime_labels,  
            columns=manga_labels
        )

        return similarity_table
    
def main():
    analyzer = Analyzer()

    anime_summaries = analyzer.load_summaries('AnimeEpisodes')
    manga_summaries = analyzer.load_summaries('MangaChapters')

    preprocessed_anime = analyzer.preprocess_summaries(anime_summaries)
    preprocessed_manga = analyzer.preprocess_summaries(manga_summaries)


    anime_labels = [f"Episode {i+1}" for i in range(10)]
    manga_labels = [f"Chapter {i+1}" for i in range(10)]

    similarity_table = analyzer.cosine_sim(preprocessed_anime, preprocessed_manga, anime_labels, manga_labels)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    print(similarity_table)

if __name__ == "__main__":
    main()