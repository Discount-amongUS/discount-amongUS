from .index import db

class Restaurant(db.Model):
    restaurantID = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Restaurant %r>' % self.restaurantID
