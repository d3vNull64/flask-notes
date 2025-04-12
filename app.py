from flask import Flask

from instance.db import init_db
from models.notes import Notes
from routes.index import index_bp
from routes.notes import notes_bp

app = Flask(__name__)

init_db()

app.register_blueprint(index_bp)
app.register_blueprint(notes_bp)
app.secret_key = "d291ee40325c5ae886d72b726df9c7db60f44b75f6a654e40e777da4bf4923bb"

Notes.selected_false_all()

if "__main__" == __name__:
    app.run(debug=True)
