from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../frontend")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    return {
        "message": "To-Do item submitted successfully",
        "itemName": item_name,
        "itemDescription": item_description
    }


if __name__ == "__main__":
    app.run(port=9000, debug=True)