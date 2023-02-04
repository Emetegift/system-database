from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

# instantiate the flask imported from flask
app = Flask(__name__)

#The configuration of URI of the database
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///' + os.path.join(base_dir, 'users.db')
#The configuration of track modification 
app.config["SQLALCHEMY_TRACK_MODIFICATION"] =False

# instantiate the SQLAlchemy to inherit from flask
db= SQLAlchemy(app)
# initialize the database
db.init_app(app)

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    
    def __repr__(self):
        return f"User {self.username}"


@app.route('/')
def index():
    users =User.query.all()
    
    context = {
        'users':users
    }
    
    return render_template('models.html', **context)
# creating a user
@app.route('/users', methods=['POST'])
def create_user():
    username = request.form.get('username')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')
    
    new_user = User(username=username, email=email, age= age, gender=gender)
    with app.app_context():
        db.session.add(new_user)
    with app.app_context():
         db.session.commit()
    
    return redirect(url_for('index'))
    


if __name__=="__main__":
    app.run(debug=True)