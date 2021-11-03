from dao.model.movie import Movie


class MovieDao:
    def __init__(self,session):
        self.session = session

    def get_one(self,aid):
        entity_list = self.session.query(Movie).get(aid)
        return entity_list

    def get_all(self):
        entity_list = self.session.query(Movie).all()
        return entity_list

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie, 204


    def delete(self,aid):
        movie = self.get_one(aid)
        self.session.delete(movie)
        self.session.commit()