from flask_restx import Resource, Namespace
from flask import request

from conteiner import movie_service
from dao.model.movie import MovieSchema, Movie

movies_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        st = Movie.query
        st = Movie.query
        if director_id:
            st = st.filter(Movie.director_id == director_id)
        if genre_id:
            st = st.filter(Movie.genre_id == genre_id)
        movies = st.all()
        return movies_schema.dump(movies), 200



    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201




@movies_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid:int):
        movie = movie_service.get_one(uid)
        if not movie:
            return 'Такого фильма нету', 404
        return movie_schema.dump(movie), 200

    def put(self,uid):
        req_json = request.json
        req_json['id'] = uid
        movie_service.update(req_json)
        return '', 204

    def delete(self, uid:int):
        movie_service.delete(uid)
        return ""






