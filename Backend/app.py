from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="../frontend")

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        raise Exception("This is a test error")

        student = {
            "name": name,
            "email": email,
            "age": int(age)
        }

        collection.insert_one(student)

        return render_template("success.html")

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(port=9000, debug=True)