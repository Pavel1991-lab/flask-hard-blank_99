from dao.director import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        aid = data.get('id')
        director = self.get_one(aid)
        director.id = data.get('id')
        director.name = data.get('name')
        return self.dao.update(director)

    def delete(self, aid):
        return self.dao.delete(aid)