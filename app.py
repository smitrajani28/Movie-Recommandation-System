import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommand(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x : x[1])[1:6]

    recommanded_movies = []
    recommanded_movies_posters = []
    for i in movies_list:
        recommanded_movies.append(movies.iloc[i[0]].title)              
        recommanded_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))              
    return recommanded_movies, recommanded_movies_posters

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
    names,posters = recommand(selected_movie)
    cols = st.columns(len(names))
    for i in range(len(names)):
        with cols[i]:
            txt = st.text_area(names[i],height=2)
            st.write(txt)
            st.image(posters[i])