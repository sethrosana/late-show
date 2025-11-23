import pytest
from server.app import app, db
from server.models import Episode, Guest, Appearance

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(test_app):
    return test_app.test_client()

@pytest.fixture
def seed_data(test_app):
    from server.models import Episode, Guest, Appearance
    e1 = Episode(date='2025-11-01', number=1)
    e2 = Episode(date='2025-11-02', number=2)
    g1 = Guest(name='John Doe', occupation='Comedian')
    g2 = Guest(name='Jane Smith', occupation='Musician')
    a1 = Appearance(rating=5, episode=e1, guest=g1)
    a2 = Appearance(rating=4, episode=e2, guest=g2)
    db.session.add_all([e1, e2, g1, g2, a1, a2])
    db.session.commit()
    return {'episodes': [e1, e2], 'guests': [g1, g2], 'appearances': [a1, a2]}
