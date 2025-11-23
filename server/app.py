from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Episode, Guest, Appearance


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://late_show_user:sethmorara@localhost:5432/late_show_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

@app.route("/")
def index():
    return {"message": "Late Show API running"}, 200

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ep.to_dict(rules=("-appearances",)) for ep in episodes], 200

class EpisodeByID(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        db.session.delete(episode)
        db.session.commit()
        return {}, 204

class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict(rules=("-appearances",)) for g in guests], 200

class Appearances(Resource):
    def post(self):
        data = request.get_json()
        try:
            app = Appearance(
                rating=data.get("rating"),
                episode_id=data.get("episode_id"),
                guest_id=data.get("guest_id"),
            )
            db.session.add(app)
            db.session.commit()
            return app.to_dict(), 201
        except:
            return {"errors": ["validation errors"]}, 400

api.add_resource(Episodes, "/episodes")
api.add_resource(EpisodeByID, "/episodes/<int:id>")
api.add_resource(Guests, "/guests")
api.add_resource(Appearances, "/appearances")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
