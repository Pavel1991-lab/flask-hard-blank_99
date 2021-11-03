from dao.genre import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        aid = data.get('id')
        genre = self.get_one(aid)
        genre.id = data.get('id')
        genre.name = data.get('name')
        return self.dao.update(genre)


    def delete(self, aid):
        return self.dao.delete(aid)