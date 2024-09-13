from flask import *
from datetime import timedelta
from flask_sqlalchemy import *

app = Flask(__name__)
app.secret_key = "YouShouldGetSomeRest"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)


# ========================= Models --------------------------
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password



# ========================= APP URL Routing --------------------------

# ****************** HOME 
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


# ****************** Register / Login

# REG -----
@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")


# ****************** LOG 
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


# ****************** Run APP 
if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)

