from conteiner import director_service
from dao.model.director import DirectorSchema
from flask import request
from flask_restx import Resource, Namespace


directors_ns = Namespace('director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201




@directors_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid:int):
        director = director_service.get_one(uid)
        if not director:
            return 'Такого фильма нету', 404
        return director_schema.dump(director), 200

    def put(self,uid):
        req_json = request.json
        req_json['id'] = uid
        director_service.update(req_json)
        return '', 204

    def delete(self, uid:int):
        director_service.delete(uid)
        return ""

