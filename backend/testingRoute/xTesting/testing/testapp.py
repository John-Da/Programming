from flask import *
from datetime import timedelta
from flask_sqlalchemy import *

app = Flask(__name__)
app.secret_key = "YouShouldGetSomeRest"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)
class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    user_booked = db.relationship('Court', backref='user', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Court(db.Model):
    court_id = db.Column("court_id", db.Integer, primary_key=True)
    court_name = db.Column(db.String(100))
    aviable_time = db.Column(db.String(100))






@app.route("/")
def home():
    return render_template("index.html")



@app.route("/register", methods=["POST", "GET"])
def register():
    email = None
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["username"]
        password = request.form["password"]
        session["user"] = username
        session["email"] = email
        session["password"] = password
        
        if email in session:
            flash("Account has already exited!")
            return redirect(url_for("login"))
        else:
            flash("Account created successfully!")
            return redirect(url_for("user"))
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("dashboard.html", values=Users.query.all())
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)



# delete
# found_user = users.query.filter_by(name=user).delete()
# for user in found_user:
#   user.delete()