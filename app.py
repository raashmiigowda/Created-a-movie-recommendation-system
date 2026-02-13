from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend, movies

app = Flask(__name__)
CORS(app)

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(list(movies['title'].values))

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.json
    movie = data['movie']
    result = recommend(movie)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
