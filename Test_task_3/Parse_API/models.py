from sqlalchemy.orm import  declarative_base
import sqlalchemy as sq
Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'
    id = sq.Column(sq.Integer, primary_key=True)
    list = sq.Column(sq.String(length=256), nullable=False)
    created_at = sq.Column(sq.DateTime, nullable=False)
    changed_at = sq.Column(sq.DateTime, nullable=False)
    completed = sq.Column(sq.Boolean, nullable=False)

    def __repr__(self):
        return (f'id: {self.id}, list: {self.list}, completed: {self.completed}')

