from conteiner import genre_service
from dao.model.genre import GenreSchema
from flask import request
from flask_restx import Resource, Namespace


genres_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = genre_service.get_all()
        return genres_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201



@genres_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid:int):
        genre = genre_service.get_one(uid)
        if not genre:
            return 'Такого жанра нету', 404
        return genre_schema.dump(genre), 200

    def put(self,uid):
        req_json = request.json
        req_json['uid'] = uid
        genre = genre_service.update(req_json)
        return '', 204

    def delete(self, uid:int):
        genre_service.delete(uid)
        return ""

