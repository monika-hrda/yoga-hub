import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
cached_query = ""


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/classes")
def get_classes():

    # get the page parameter from the query string in the url
    page = request.args.get('page', type=int, default=1)

    per_page = 9

    # get the clases only for the page requested, since results start at 0,
    # and the page is 1, we need to reset the skip to page - 1 
    # and then mutltiply by the classes per page
    classes = mongo.db.classes.find({}).skip((page-1)*per_page).limit(per_page)

    # count total number of classes / documents
    total = mongo.db.classes.count_documents({})

    # set the page parameters
    pagination = Pagination(
        per_page=per_page, page=page, total=total, record_name='classes'
    )

    return render_template(
        "classes.html", classes=list(classes),  pagination=pagination
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get form inputs
        username = request.form.get("username").lower()
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if both entered passwords match
        if password != password_confirm:
            flash("Your passwords don't match. Try again!")
            return redirect(url_for("register"))

        register = {
            "username": username,
            "password": generate_password_hash(password),
            "is_teacher": "no"
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = username
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    try:
        # grab the session user's username from db
        username_in_session = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    except BaseException:
        # if the user is not logged in
        return redirect(url_for("login"))

    try:
        # grab the url username from db
        username_url = mongo.db.users.find_one(
            {"username": username})["username"]
    except BaseException:
        # if the url username does not exist
        flash(f"Oops, that is not your username!")
        return redirect(url_for("home"))

    if username_url != username_in_session:
        flash(f"Oops, you are not logged in as {username_url}!")
        return redirect(url_for("home"))

    profile_classes = list(mongo.db.classes.find(
        {"created_by": username_in_session}))

    return render_template(
            "profile.html", 
            username=username_in_session, 
            profile_classes=profile_classes
        )


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_class", methods=["GET", "POST"])
def add_class():
    if request.method == "POST":
        is_online = "yes" if request.form.get("is_online") else "no"
        new_class = {
            "class_name": request.form.get("class_name"),
            "class_style": request.form.get("class_style"),
            "description": request.form.get("description"),
            "date": request.form.get("date"),
            "is_online": is_online,
            "location": request.form.get("location"),
            "price": request.form.get("price"),
            "contact": request.form.get("contact"),
            "created_by": session["user"]
        }

        mongo.db.classes.insert_one(new_class)
        flash("Class Added Successfully")
        return redirect(url_for("get_classes"))

    styles = mongo.db.styles.find().sort("class_style", 1)
    return render_template("add_class.html", styles=styles)


@app.route("/edit_class/<class_id>", methods=["GET", "POST"])
def edit_class(class_id):
    if request.method == "POST":
        is_online = "yes" if request.form.get("is_online") else "no"
        submit = {
            "class_name": request.form.get("class_name"),
            "class_style": request.form.get("class_style"),
            "description": request.form.get("description"),
            "date": request.form.get("date"),
            "is_online": is_online,
            "location": request.form.get("location"),
            "price": request.form.get("price"),
            "contact": request.form.get("contact"),
            "created_by": session["user"]
        }
        mongo.db.classes.update_one(
            {"_id": ObjectId(class_id)}, {"$set": submit})
        flash("Class Successfully Updated")

    edited_class = mongo.db.classes.find_one({"_id": ObjectId(class_id)})
    styles = mongo.db.styles.find().sort("class_style", 1)
    return render_template(
            "edit_class.html",
            edited_class=edited_class,
            styles=styles
        )


@app.route("/delete_class/<class_id>")
def delete_class(class_id):
    mongo.db.classes.delete_one({"_id": ObjectId(class_id)})
    flash("Class Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/search", methods=["GET", "POST"])
def search():
    global cached_query
    query = request.form.get("query")

    if query:
        cached_query = query
    else:
        query = cached_query

    page = request.args.get('page', type=int, default=1)

    per_page = 9

    classes = list(mongo.db.classes.find(
        {"$text": {"$search": query}}).skip((page-1)*per_page).limit(per_page))
    total = len(list(mongo.db.classes.find({"$text": {"$search": query}})))

    pagination = Pagination(
        per_page=per_page, page=page, total=total, record_name='classes'
    )

    return render_template(
        "classes.html", classes=classes,  pagination=pagination
    )


# 404 error (page not found)
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html", error=error), 404


# 500 error (internal server error)
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
