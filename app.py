import streamlit as st
import pickle

def recommand(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x : x[1])[1:6]

    recommanded_movies = []
    for i in movies_list:
        recommanded_movies.append(movies.iloc[i[0]].title)
    return recommanded_movies

similarity = pickle.load(open("similarity.pkl","rb"))
movies = pickle.load(open("movies.pkl","rb"))
movies_list = movies["title"].values
st.title('Movie Recommander System')

selected_movie = st.selectbox('Choose a movie',movies_list)

if st.button("Recommand"):
    recommandations = recommand(selected_movie)
    for i in recommandations:
        st.write(i)