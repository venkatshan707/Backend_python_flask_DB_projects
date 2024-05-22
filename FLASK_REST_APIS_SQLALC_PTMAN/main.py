from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy #Its a library and database toolkit for python. used to interact with SQL DATABASE. Its extension of SQLAlchemy.
from flask_marshmallow import Marshmallow# using it for data serialization
import os

app = Flask(__name__)
"""
@app.route('/', methods=['GET'])
def home():
    return jsonify(
        {   "name": "venkat",
            "msg":"hello world"
            })


"""
basedir = os.path.abspath(os.path.dirname(__file__))  # we are getting current file's directory and copying it to the variable as string. 
print(f"Type:  {type(basedir)}  and  path : {(basedir)}")

# Set the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir, 'db.sqlite') # we are going to create a database in our current working directory. I am passing 
# Disable modification tracking as it's not needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

db=SQLAlchemy(app) # creating object for sqlalchemy
ma=Marshmallow(app)# creating object for marshmallow for data serialization

#db.Model is the base class from which your User model inherits, providing functionalities like defining columns (db.Column) and primary keys (primary_key=True).
#Model Definition: Defined the User model inheriting from db.Model
class User (db.Model):
    id =db.Column(db.Integer, primary_key =True)
    name =db.Column(db.String (100))
    contact =db.Column(db.String (100), unique = True)

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'contact')

userSchema = UserSchema()
usersSchema= UserSchema(many=True)
    
# Set up an application context
with app.app_context():
    # Create all database tables based on defined models
    db.create_all()

#add new user
@app.route('/user/', methods= ['POST'])
def add_user():
    name = request.json['name']
    contact = request.json['contact']
    new_user = User(name,contact)
    db.session.add(new_user)
    db.session.commit()
    return userSchema.jsonify(new_user)

#Show all user 
@app.route('/user/', methods= ['GET'])
def getallusers():
    allusers = User.query.all() #  retrieves all users from the User table
    result=usersSchema.dump(allusers)
    """In Flask, when you retrieve data from the database using SQLAlchemy, the data is typically returned as SQLAlchemy objects
      or query result objects. These objects are not directly JSON serializable, meaning they cannot be directly converted to JSON 
      format using jsonify.

    The purpose of using usersSchema.dump(allusers) in your code is to serialize the SQLAlchemy query result (allusers)
    into a JSON-serializable format. This serialization process converts the SQLAlchemy objects into a format that can be
    represented as JSON. The dump method provided by Marshmallow is used for this serialization task.
    """
    return jsonify(result) # The jsonify function from Flask converts the serialized data into a JSON response that can be sent back to the client.

#show user by ID
@app.route('/user/<id>', methods= ['GET'])
def getuserById(id):
    user = User.query.get(id)
    
    #return userSchema.jsonify(user)
    result=userSchema.dump(user) # we can return without dumping too in the above way
    return jsonify(result)

#update by user by id
@app.route('/user/<id>', methods= ['PUT'])
def updateUser(id):
    user=User.query.get(id) # getting user record with id
    user.name = request.json['name'] # Assigning new name on the record with id received
    user.contact = request.json['contact']
    db.session.commit()
    return userSchema.jsonify(user)

#delete record by user id
@app.route('/user/<id>', methods= ['DELETE'])
def deleteUserById(id):
    user=User.query.get(id) # getting user record with id
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully", "deleted_user": userSchema.dump(user)}) # passing multiple items in dictionary

if __name__ == '__main__':
    app.run(debug=True, port =5000)

