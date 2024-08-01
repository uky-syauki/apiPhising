from app import db

class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    def __repr__(self) -> str:
        return f"<Data {self.username}>"
    def data_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }