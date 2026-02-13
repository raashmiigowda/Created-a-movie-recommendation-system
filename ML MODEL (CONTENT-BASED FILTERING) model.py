import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Combine features
movies['tags'] = movies['genres'] + " " + movies['overview']

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]

    idx = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended
