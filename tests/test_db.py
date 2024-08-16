# tests/test_db.py

import unittest
from peewee import *
from app import TimelinePost

'''
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()

    class Meta:
        database = SqliteDatabase(':memory:')
'''

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    @classmethod
    def tearDownClass(cls):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        self.assertEqual(second_post.id, 2)

        posts = list(TimelinePost.select().order_by(TimelinePost.id))
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].name, 'John Doe')
        self.assertEqual(posts[1].name, 'Jane Doe')

if __name__ == '__main__':
    unittest.main()
