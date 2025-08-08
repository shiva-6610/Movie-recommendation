import pandas as pd
import streamlit as st

st.title("🎬 Genre-Based Movie Recommender")

# Load dataset
movies = pd.read_csv('movies.csv')
movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

# Dropdown to select genre
all_genres = sorted(set(g for sublist in movies['genres'] for g in sublist))
selected_genre = st.selectbox("Choose a Genre:", all_genres)

# Recommend top 5 movies
if selected_genre:
    recommended = movies[movies['genres'].apply(lambda x: selected_genre in x)].head(5)
    st.write("Top 5 Recommended Movies:")
    for title in recommended['title']:
        st.write("🎥", title)
