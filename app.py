
import email
from enum import unique
from operator import index
from io import BytesIO

from pickle import dump
from flask import Flask, Request,render_template,request,redirect,flash,send_file,Response
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, Table, select, true
from flask_login import UserMixin
from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user
import requests
import json
from wtforms import TextField, Form
from ast import literal_eval
import ast


#my database connection
local_server = True
app = Flask(__name__)
app.secret_key = "harsh"


#unique user access
#login_manager = LoginManager(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.2:3307/newdata_user"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Test( db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.column(db.String(50))           
    filename = db.column(db.String(1000))
    data = db.Column(db.LargeBinary)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    uname = db.Column(db.String(25))
    umail = db.Column(db.String(25), unique=True)
    uphone = db.Column(db.String(14), unique=True)
    upass =  db.Column(db.String(30))
    cupass =  db.Column(db.String(30))
   
																	

class Likedmovie(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    moviename = db.Column(db.String(100))

class User_rating(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.column(db.String(11))           
    movieid = db.column(db.Integer)
    rating = db.Column(db.Integer)
    email = db.Column(db.String(100))


class Search_history(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)         
    movieid = db.column(db.Integer)
    moviename = db.Column(db.String(100))
    email = db.Column(db.String(100))
    



cities = []


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(cities), mimetype='application/json')




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

suggestion = list(dataframe['title'])

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
        return movie_recommender(title.lower())

    
dataset = pd.read_csv('tmdb2.csv')
dataset['genre'] = dataset['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
def all_detail(movie_id):
  
    lis = []

    poster_path = list(dataset[dataset['id']==movie_id]['movie_posters'])[0]
    lis.append(poster_path)

    # adding genre 1
    

    poster_genre = (dataset[dataset['id']==movie_id]['genre'].values)[0]
    # genrelist = ast.literal_eval(poster_genre)
    lis.append(poster_genre)

    # addding rating 2
    rating = (dataset[dataset['id']==movie_id]['vote_average'].values)[0]
    lis.append(rating)

    #runtime 3
    run = (dataset[dataset['id']==movie_id]['runtime'].values)[0]
    lis.append(run)

    #overview 4
    over = (dataset[dataset['id']==movie_id]['overview'].values)[0]
    lis.append(over)

    #name 5

    name = (dataset[dataset['id']==movie_id]['title'].values)[0]
    lis.append(name)

    #rating 6
    vote = (dataset[dataset['id']==movie_id]['vote_average'].values)[0]
    lis.append(vote)

    return lis

def get_cast(movie_name):
    cast_details = []
    movie_id = get_movie_id(movie_name)
    url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=cd109cb98c90d3020a252e6f524b8d63&language=en-US".format(movie_id)
    cast_data_detail = requests.get(url)
    cast_data_detail = cast_data_detail.json()
    cast_data_detail
    for i in range(len(cast_data_detail['cast'])):
        single_cast_detail = []
        single_cast_detail.append(cast_data_detail['cast'][i]["name"])
        single_cast_detail.append(cast_data_detail['cast'][i]["character"])
        single_cast_detail.append("https://image.tmdb.org/t/p/w500"+ str(cast_data_detail['cast'][i]["profile_path"]))
        cast_details.append(single_cast_detail)
    
    return cast_details[:8]

data = pd.read_csv("tmdb_5000_movies.csv")
def get_movie_id(movie):
    
    data['title'] = data['title'].str.lower()
    first = data[["id","title"]]
    second = first[data['title']== movie]
    rt = list(second['id'])
   
    return rt[0]


def movie_detail(moviel):

    doc = []

    for m in moviel:
        
        id = get_movie_id(m)
        l1 = all_detail(id)
        doc.append(l1)
    return doc

def movie_detail_by_id(moviel):

    doc = []

    for m in moviel:
        
        l1 = all_detail(m)
        doc.append(l1)
    return doc




import nltk
import pandas as pd
df = pd.read_csv('tmdb_5000_movies.csv')
df["title"] = df["title"].str.lower()
df.tagline.fillna('', inplace=True)
df['description'] = df['tagline'].map(str) + ' ' + df['overview']
df.dropna(inplace=True)
import re
import numpy as np
import contractions
stop_words = nltk.corpus.stopwords.words('english')
def normalize_document(doc):
    # doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    doc = contractions.fix(doc)
    tokens = nltk.word_tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    doc = ' '.join(filtered_tokens)
    return doc
normalize_corpus = np.vectorize(normalize_document)
norm_corpus = normalize_corpus(list(df['description']))
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
tfidf_matrix = tf.fit_transform(norm_corpus)
tfidf_matrix.shape
from sklearn.metrics.pairwise import cosine_similarity
doc_sim = cosine_similarity(tfidf_matrix)
doc_sim_df = pd.DataFrame(doc_sim)
movies_list = df['title'].values
def movie_recommender(movie_title, movies=movies_list, doc_sims=doc_sim_df):
    movie_idx = np.where(movies == movie_title)[0][0]
    movie_similarities = doc_sims.iloc[movie_idx].values
    similar_movie_idxs = np.argsort(-movie_similarities)[1:9]
    similar_movies = movies[similar_movie_idxs]
    return similar_movies







@app.route("/", methods=['POST','GET'])
def home():

    try:

        new_data  = pd.read_csv('tmdb_5000_movies.csv')
        new_data['title'] = new_data['title'].str.lower()
        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)

        d_pop = new_data.sort_values(by=['revenue'],ascending=False)
        nd_pop = d_pop.iloc[:12,:]
        nd_pop = nd_pop['title'].to_list()
        data_by_pop = movie_detail(nd_pop)
        postsdata.append(data_by_pop)
        return render_template("index2.html", postsdata= postsdata, suggestion = suggestion)

    except:
        return render_template("notfound.html")    


@app.route("/trending", methods=['POST','GET'])
def trending():

    try:
        new_data  = pd.read_csv('tmdb_5000_movies.csv')
        new_data['title'] = new_data['title'].str.lower()
        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)

        d_pop = new_data.sort_values(by=['vote_count'],ascending=False)
        nd_pop = d_pop.iloc[10:23,:]
        nd_pop = nd_pop['title'].to_list()
        data_by_pop = movie_detail(nd_pop)
        postsdata.append(data_by_pop)
        return render_template("Trending.html", postsdata= postsdata, suggestion = suggestion)

    except:
        return render_template("notfound.html")    


@app.route("/popular", methods=['POST','GET'])
def popular():

    try:
   
        new_data  = pd.read_csv('tmdb_5000_movies.csv')
        new_data['title'] = new_data['title'].str.lower()
        l = new_data['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        nl = []
        for i in l:
            try:
                nl.append(i[0])
            except:
                nl.append('Movie')
        new_data['single_genre'] = nl
        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)

        d_pop = new_data[new_data['single_genre']=='Action']
        nd_pop = d_pop.iloc[10:23,:]
        nd_pop = nd_pop['title'].to_list()
        data_by_pop = movie_detail(nd_pop)

        postsdata.append(data_by_pop)
        

        return render_template("popular.html", postsdata= postsdata , suggestion = suggestion)

    except:
        return render_template("notfound.html")    


@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method == "POST":
        funame = request.form.get('name') 
        fumail = request.form.get('email')
        fuphone = request.form.get('mobile')
        fupass = request.form.get('pass')
        fcupass = request.form.get('cpass')
        user = User.query.filter_by(umail = fumail).first()
        if user :
            flash("E-mail Already Exist", "info")
            return redirect(url_for('signup'))
        new_user = db.engine.execute(f"INSERT INTO `user` (`id`, `uname`, `umail`, `uphone`, `upass`, `cupass`)  VALUES (NULL, '{funame}','{fumail}','{fuphone}','{fupass}','{fcupass}');")

        # flash("Registration Successful enter Credential for Account Access", "success")
        return redirect(url_for('home'))
    return render_template("signup.html")




@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == "POST":
        try: 
        
            email = request.form.get('email') 
            upass = request.form.get('pass')
            # dl  = request.form.get('ulabel')
            user = User.query.filter_by(umail = email).first_or_404(description='There is no data with {}'.format(email))

            if user and user.upass == upass:
                login_user(user)

                collection  = Likedmovie.query.filter_by(email = email).all()
                if collection:
                    moviename = collection[-1].moviename
                    
                    list_input = collaborative_recommends(current_user.id, moviename.title())
                
                    
                    postsdata = []
                    data_by_vote = []
                    postsdata.append(data_by_vote)
                    list_input = [x.lower() for x in list_input]
                    data_by_pop = movie_detail(list_input)

                    postsdata.append(data_by_pop)
                    flash("Login Successfully", "info")
                    return render_template("dashboard.html", postsdata= postsdata , suggestion = suggestion)


                
                new_data  = pd.read_csv('tmdb_5000_movies.csv')
                new_data['title'] = new_data['title'].str.lower()

                postsdata = []
                data_by_vote = []
                postsdata.append(data_by_vote)

                d_pop = new_data.sort_values(by=['revenue'],ascending=False)
                nd_pop = d_pop.iloc[:8,:]
                nd_pop = nd_pop['title'].to_list()
                data_by_pop = movie_detail(nd_pop)

                postsdata.append(data_by_pop)
                flash("Login Successfully", "info")
                return render_template("dashboard.html", postsdata= postsdata , suggestion = suggestion)
                return redirect(url_for('profilehome'))

            else:
                flash("Invalide Credential", "info")
                return redirect(url_for('login'))
        except:
             flash("User Not Exist", "info")
             return redirect(url_for('login'))

        
    return render_template("login.html" , suggestion = suggestion)




@app.route("/search", methods=['POST','GET'])
def search():
    try:

        if request.method=="POST":
            moviename = request.form.get("movie")
            moviename = moviename.lower()
            list_input = movie_recommender(moviename)
            
            list_input = np.insert (list_input,0,moviename)
            recommended = movie_detail(list_input)
            postsdata = []

            cast = get_cast(moviename)



            postsdata.append(cast)
            postsdata.append(recommended)
            
            
            return render_template("normal_search.html", postsdata = postsdata , suggestion = suggestion)
            # return "search.html"+movie

            

        return render_template("index.html" , suggestion = suggestion)
    except:
        return render_template("notfound.html" , suggestion = suggestion)

@app.route("/like", methods=['POST','GET'])
@login_required
def like():
    try: 
        if request.method=="POST":
            moviename = request.form.get("movie")
            moviename = moviename.lower()
            usermail = current_user.umail

            llist  = Likedmovie.query.filter_by(email = usermail).all()
            liked = []
            for i in llist:
                liked.append(i.moviename)

            if liked.__contains__(moviename):
                list_input = movie_recommender(moviename)
                list_input = np.insert (list_input,0,moviename)
                recommended = movie_detail(list_input)
                postsdata = []

                cast = get_cast(moviename)



                postsdata.append(cast)
                postsdata.append(recommended)
                
                flash("Already Liked ", "success")
                return render_template("profile_search.html", postsdata = postsdata , suggestion = suggestion)


            new_user = db.engine.execute(f"INSERT INTO `likedmovie` (`id`, `email`, `moviename`)  VALUES (NULL, '{usermail}','{moviename}');")

            list_input = movie_recommender(moviename)
            list_input = np.insert (list_input,0,moviename)
            recommended = movie_detail(list_input)
            postsdata = []

            cast = get_cast(moviename)



            postsdata.append(cast)
            postsdata.append(recommended)
            
            flash("added to liked movies", "success")
            return render_template("profile_search.html", postsdata = postsdata , suggestion = suggestion)
    except:
        return render_template("notfound_profile.html")



@app.route("/likedmovie", methods=['POST','GET'])
@login_required
def likedmovie():

    try:
    
        email = current_user.umail

        likeddata  = Likedmovie.query.filter_by(email = email).all()
        # return email

        if likeddata:
            movies_list = []
            for i in likeddata:
                movies_list.append(i.moviename)

            postsdata = []
            data_by_vote = []
            postsdata.append(data_by_vote)
            liked_data = movie_detail(movies_list)

            postsdata.append(liked_data)

            return render_template("liked_movies.html", postsdata= postsdata , suggestion = suggestion)
        
        return render_template("liked_movies.html" , suggestion = suggestion)

    except:
         return render_template("notfound.html")


            
@app.route("/rated_movie_detail", methods=['POST','GET'])
@login_required
def rated_movie_detail():
    try:
        email = current_user.umail

        # rated_data  = Likedmovie.query.filter_by(email = email).all()
        cemail = current_user.umail
        rated_data  = User_rating.query.filter_by(email = cemail).all()
        

        if rated_data:
            movie_rated = []
            for k in rated_data:
                movie_rated.append(k.rating)

            postsdata = []
            data_by_vote = []
            postsdata.append(data_by_vote)
            liked_data = movie_detail_by_id(movie_rated)

            postsdata.append(liked_data)

            return render_template("ratedmovies.html", postsdata= postsdata , suggestion = suggestion)


        return render_template("ratedmovies.html" , suggestion = suggestion)

    except:
       return render_template("notfound.html")     





@app.route("/searchprofile", methods=['POST','GET'])
@login_required
def searchprofile():
    try: 
        if request.method=="POST":
            moviename = request.form.get("movie")
            moviename = moviename.lower()

            new_data = db.engine.execute(f"INSERT INTO `search_history` (`id`, `movieid`, `moviename`, `email`)  VALUES (NULL,'{get_movie_id(moviename)}','{moviename}','{current_user.umail}');")

            
            # list_input = movie_recommender(moviename)
            list_input = collaborative_recommends(current_user.id, moviename.title())
            




            
            list_input = np.insert (list_input,0,moviename)
            list_input = [x.lower() for x in list_input]
            recommended = movie_detail(list_input)
            postsdata = []
            
            cast = get_cast(moviename)



            postsdata.append(cast)
            postsdata.append(recommended)
            
            
            return render_template("profile_search.html", postsdata = postsdata , suggestion = suggestion)
            

        return render_template("dashboard.html" , suggestion = suggestion)
    except:
        return render_template("notfound_profile.html" , suggestion = suggestion)

@app.route("/search_history", methods=['POST','GET'])
@login_required
def search_history():
    try:

        cemail = current_user.umail
        searched  = Search_history.query.filter_by(email = cemail).all()

        movie_list = []
        for element in  searched:
            movie_list.append(element.moviename)
        if len(movie_list)>16:
            movie_list = movie_list[-15:]
        movie_list = list(set(movie_list))

        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)
        liked_data = movie_detail(movie_list)

        postsdata.append(liked_data)

        return render_template("search_history.html", postsdata= postsdata , suggestion = suggestion)

    except:
        return render_template("notfound.html")    



@app.route('/profilehome')
@login_required
def profilehome():
    try:
    

        email = current_user.umail
            

        collection  = Likedmovie.query.filter_by(email = email).all()
        if collection:
            moviename = collection[-1].moviename
            list_input = collaborative_recommends(current_user.id, moviename.title())
            
            postsdata = []
            data_by_vote = []
            postsdata.append(data_by_vote)
            list_input = [x.lower() for x in list_input]
            data_by_pop = movie_detail(list_input)

            postsdata.append(data_by_pop)
            return render_template("dashboard.html", postsdata= postsdata , suggestion = suggestion)
        
        new_data  = pd.read_csv('tmdb_5000_movies.csv')
        new_data['title'] = new_data['title'].str.lower()

        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)

        d_pop = new_data.sort_values(by=['revenue'],ascending=False)
        nd_pop = d_pop.iloc[:8,:]
        nd_pop = nd_pop['title'].to_list()
        data_by_pop = movie_detail(nd_pop)

        postsdata.append(data_by_pop)
        

        return render_template("dashboard.html", postsdata= postsdata , suggestion = suggestion)

    except:
        return render_template("notfound.html")    

@app.route('/genres', methods=['POST','GET'])
@login_required
def genres():

    try:

        new_data  = pd.read_csv('tmdb_5000_movies.csv')
        new_data['title'] = new_data['title'].str.lower()
        l = new_data['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
        nl = []
        for i in l:
            try:
                nl.append(i[0])
            except:
                nl.append('Movie')
        new_data['single_genre'] = nl

        postsdata = []
        data_by_vote = []
        postsdata.append(data_by_vote)

        # Action 1
        action_data = new_data[new_data['single_genre']=='Action']
        nd_pop = action_data.iloc[0:4,:]
        nd_pop = nd_pop['title'].to_list()
        data_by_action = movie_detail(nd_pop)
        postsdata.append(data_by_action)

        # Thriller 2
        Thriller_data = new_data[new_data['single_genre']=='Thriller']
        tnd_pop = Thriller_data.iloc[0:4,:]
        tnd_pop = tnd_pop['title'].to_list()
        data_by_Thriller = movie_detail(tnd_pop)
        postsdata.append(data_by_Thriller)

        # Adventure 3
        Adventure_data = new_data[new_data['single_genre']=='Adventure']
        Adventure_pop = Adventure_data.iloc[0:4,:]
        Adventure_pop = Adventure_pop['title'].to_list()
        data_by_Adventure = movie_detail(Adventure_pop)
        postsdata.append(data_by_Adventure)

        #Drama 4
        Drama_data = new_data[new_data['single_genre']=='Drama']
        Drama_pop = Drama_data.iloc[0:4,:]
        Drama_pop = Drama_pop['title'].to_list()
        data_by_Drama = movie_detail(Drama_pop)
        postsdata.append(data_by_Drama)


        return render_template('genre.html', postsdata  = postsdata , suggestion = suggestion)

    except:
        return render_template("notfound.html")    




@app.route('/movie_rating', methods=['POST','GET'])
@login_required
def movie_rating():
    try:


        if request.method=="POST":
            moviename = request.form.get("movie")
            rated = request.form.get("rated")
            moviename = moviename.lower()
            movie_id = int(get_movie_id(moviename))

            id_user = str(current_user.id)
            cemail = current_user.umail
            rate_list  = User_rating.query.filter_by(email = cemail).all()
            movie_rated = []
            for k in rate_list:
                if k.rating == movie_id:
                    movie_rated.append(k.rating)

            if movie_rated:
                list_input = movie_recommender(moviename)
                list_input = np.insert (list_input,0,moviename)
                recommended = movie_detail(list_input)
                postsdata = []

                cast = get_cast(moviename)



                postsdata.append(cast)
                postsdata.append(recommended)
                
                flash("Already Rated ", "success")
                return render_template("profile_search.html", postsdata = postsdata , suggestion = suggestion)

            
            new_data = db.engine.execute(f"INSERT INTO `user_rating` (`id`, `id_user`, `movieid`, `rating`, `email`)  VALUES (NULL, '{id_user}','{rated}','{movie_id}','{cemail}');")

            list_input = movie_recommender(moviename)
            list_input = np.insert (list_input,0,moviename)
            recommended = movie_detail(list_input)
            postsdata = []

            cast = get_cast(moviename)
            postsdata.append(cast)
            postsdata.append(recommended)
            
            flash("Thanks for Rating", "success")
            return render_template("profile_search.html", postsdata = postsdata , suggestion = suggestion)

    except:
        return render_template("notfound.html")        
    






@app.route('/logout')
@login_required
def logout():

    try:
        logout_user()
        
        return redirect(url_for('home'))

    except:
        return render_template("notfound.html")    



app.run(debug = True)