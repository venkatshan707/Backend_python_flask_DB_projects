from flask import Flask, request, jsonify # jsonify used to create a json response

app = Flask(__name__)# Creating a flask app which is onject to the Flask Class
# Unique Application Name: __name__ is a special Python variable that represents the name of the current module. 
# When you pass __name__ to Flask, it helps Flask determine the root path of the application. 
# This is important for Flask to locate resources such as templates, static files, and other modules related to your application.



# we are going to create root. root is easentially a end point, this is kind of location on our API
#To create a root I am going to define a function
# @app.route("/")   # Now to make root  is accessible, we are adding decorator. "app" name of our flask application. routing to path we need to access 
# def home():
#     #Inside this function we will just return some data that we want the user to have  access to when they reach this root
#     return "Home" 

# As like demo route above, we can create multiple routes and we can mark them with diff methods (Methods: GET, POST,PUT, DELETE)
# GET: used to retrive the data from the server. 
# POST: POST is more commonly used for creating new resources or updating existing resources with partial data
# PUT :  PUT is used to update existing resources with a complete representation or to create a new resource if it doesn't exist
# DELETE : delete a resource from where we are accessing


# Creating GET Route 
@app.route("/get-user/<user_id>")   # <user_id> is placeholder for passing a dynamic value which can be accessible inside our route
def get_user(user_id):
    user_data = {
        "user_id": user_id, 
        "name": "john doe",
        "email": "abc@gmail.com" 

    }
# Qurery Parameters: which is essentially a extra value that's included after the main path 
#"/get-user/1237?extra= hello world" #
    extra = request.args.get("extra")
    if extra :
        user_data ["extra"] = extra
        
    return jsonify(user_data), 200 # 200 is a default code for successful

if __name__ == '__main__':
    app.run(debug=True)# This will run our flask server
