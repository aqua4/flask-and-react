from app import db
from sqlalchemy.sql import func


class Value(db.Model):

    __tablename__ = 'values'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    value = db.Column(db.String(128), index=True)

    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'value': self.value
        }

    @classmethod
    def get_values(cls):
        return cls.query.all()

    @classmethod
    def add_value(cls, value):
        if not value:
            return False
        new_value = Value()
        new_value.value = value
        db.session.add(new_value)
        db.session.commit()
        return True
