from dao.model.genre import Genre


class GenreDao:
    def __init__(self,session):
        self.session = session

    def get_one(self,aid):
        entity_list = self.session.query(Genre).get(aid)
        return entity_list

    def get_all(self):
        entity_list = self.session.query(Genre).all()
        return entity_list

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre, 204


    def delete(self,aid):
        genre = self.get_one(aid)
        self.session.delete(genre)
        self.session.commit()