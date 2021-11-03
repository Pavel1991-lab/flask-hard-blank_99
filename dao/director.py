from dao.model.director import Director



class DirectorDao:
    def __init__(self,session):
        self.session = session

    def get_one(self, aid):
        entity_list = self.session.query(Director).get(aid)
        return entity_list

    def get_all(self):
        entity_list = self.session.query(Director).all()
        return entity_list

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self,  director):
        self.session.add(director)
        self.session.commit()
        return  director, 204


    def delete(self,aid):
        director = self.get_one(aid)
        self.session.delete(director)
        self.session.commit()