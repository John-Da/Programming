from flask import *
from datetime import timedelta
from flask_sqlalchemy import *
from sqlalchemy.orm import *

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py", silent=True)
app.config.from_mapping(SECRET_KEY="dev")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///event_database.db"


# ========================= Data Base / Models --------------------------
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
db.init_app(app)


class Event(db.Model):
    date = mapped_column(db.String, primary_key=True)
    event = mapped_column(db.String)


# ========================= APP URL Routing --------------------------


# ****************** HOME ------------------------
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


# ****************** Register / Login ------------------------


# REG -----
@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")


# ****************** LOG ------------------------
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


# ****************** Run APP ------------------------
if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
