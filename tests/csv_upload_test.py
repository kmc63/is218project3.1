import csv

from app.db import db
from app.db.models import User, Song

def test_login(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0

        user = User('keith@webizly.com', 'testtest', is_admin=1)
        db.session.add(user)

        list_of_songs = []
        file = open('../../uploads/music.csv')
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list_of_songs.append(Song(row['Name'], row['Artist'], row['Genre'], row['Year']))

        user.songs = list_of_songs
        db.session.commit()

        assert db.session.query(Song).count() == 457

        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0

