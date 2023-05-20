from flask import render_template

from . import app
from models import Movie


@app.route('/')
def index():
    movies = Movie.query.order_by(Movie.id.desc()).all()
    return render_template('index.html', movies=movies)


@app.route('/movie/<int:id>')
def movie_detail(id):
    pass


@app.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    pass


@app.route('/reviews/')
def reviews():
    pass


@app.route('/delete_reviews/<int:id>')
def delete_reviews(id):
    pass
