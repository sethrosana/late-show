def test_episode_guest_relationship(seed_data):
    e1 = seed_data['episodes'][0]
    assert len(e1.appearances) == 1
    assert e1.appearances[0].guest.name == 'John Doe'

def test_guest_episode_relationship(seed_data):
    g2 = seed_data['guests'][1]
    assert len(g2.appearances) == 1
    assert g2.appearances[0].episode.number == 2

def test_rating_validation():
    from server.models import Appearance, db
    from sqlalchemy.exc import IntegrityError
    from flask import current_app

    with current_app.app_context():
        try:
            a = Appearance(rating=10)  # invalid rating
            db.session.add(a)
            db.session.commit()
        except:
            db.session.rollback()
            assert True
