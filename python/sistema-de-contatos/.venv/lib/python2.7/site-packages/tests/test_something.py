import sqlalchemy as sa
from .tests import TestCase


class TestSomething(TestCase):
    def create_models(self):
        friends = Table('friends', self.Base.metadata,
            Column(
                'monkey_id',
                sa.Integer,
                sa.ForeignKey('monkey.id', ondelete='CASCADE'),
                primary_key=True
            ),
            Column(
                'friend_id',
                sa.Integer,
                sa.ForeignKey('monkey.id', ondelete='CASCADE'),
                primary_key=True
            )
        )

        class Monkey(self.Base):
            __tablename__ = 'node'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.Unicode(255))
            friends = sa.orm.relationship('Monkey',
                secondary= m,
                primaryjoin=id == friends.c.left_node_id,
                secondaryjoin=id == friends.c.right_node_id,
            )
            best_friend_id = sa.Column(
                sa.Integer,
                sa.ForeignKey('monkey.id', ondelete='SET NULL')
            )
