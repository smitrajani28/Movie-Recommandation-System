import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

def fetch_poster(movie_id):
    pass

def recommand(movie):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x : x[1])[1:6]

    recommanded_movies = []
    for i in movies_list:
        recommanded_movies.append(movies.iloc[i[0]].title)              
        recommanded_movies.append(movies.iloc[i[0]])              
    return recommanded_movies

similarity = pickle.load(open("similarity.pkl","rb"))
movies = pickle.load(open("movies.pkl","rb"))
movies_list = movies["title"].values
st.title('Movie Recommander System')

load_dotenv("D:/codes/API_Keys/.env")
api_key = os.getenv("THEMOVIEDB")
if api_key is None:
    api_key = st.text_input("Enter your API_key:", type="password")



selected_movie = st.selectbox('Choose a movie',movies_list)

if st.button("Recommand"):
    recommandations = recommand(selected_movie)
    for i in recommandations:
        st.write(i)