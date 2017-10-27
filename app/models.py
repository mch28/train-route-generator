from app import db
#
class StationName(db.Model):

    __tablename__ = 'station_names'
    first_part = db.Column(db.String(24))
    link_part = db.Column(db.String(12))
    second_part = db.Column(db.String(24))
    id = db.Column(db.Integer, primary_key=True)

# class Member(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     random = db.Column(db.Integer)


