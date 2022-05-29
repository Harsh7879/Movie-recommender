import pandas as pd 
import ast
import numpy as np

from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, NMF
from surprise.model_selection import cross_validate
dataframe = pd.read_csv("tmdb_5000_movies.csv")

from ast import literal_eval
dataframe['genres'] = dataframe['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

dataframe['tagline'] = dataframe['tagline'].fillna('')
dataframe['description'] =  dataframe['tagline']+dataframe['genres'].map(str)+ dataframe['overview']
dataframe['description'] = dataframe['description'].fillna('')
from sklearn.feature_extraction.text import TfidfVectorizer
tf_v = TfidfVectorizer(analyzer='word',ngram_range=(1, 3),min_df=0)
tfidf_matrix = tf_v.fit_transform(dataframe['description'])
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
dataframe = dataframe.reset_index()
titles = dataframe['title']
indices = pd.Series(dataframe.index, index=dataframe['title'])
print(indices)
reader = Reader()
ratings = pd.read_csv('ratings_small.csv')
ratings.head()
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

nmf = NMF()

trainset = data.build_full_trainset()
nmf.fit(trainset)
import numpy as np
def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan
    
id_map = pd.read_csv('rating_small_new2.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(dataframe[['title', 'id']], on='id').set_index('title')
indices_map = id_map.set_index('id')
def collaborative_recommends(userId, title):
    try: 
        idx = indices[title]
        tmdbId = id_map.loc[title]['id']
        movie_id = id_map.loc[title]['movieId']
        sim_scores = list(enumerate(cosine_sim[int(idx)]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:26]
        movie_indices = [i[0] for i in sim_scores]
        movies = dataframe.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'id']]
        
        movies['est'] = movies['id'].apply(lambda x: nmf.predict(userId, indices_map.loc[x]['movieId']).est)
        movies = movies.sort_values('est', ascending=False)
        return list(movies.head(10)['title'])
    except:
        raise "not found"

print(collaborative_recommends(1,'Charlie St. Cloud'))
