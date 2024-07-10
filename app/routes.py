from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    user_data = {}
    if request.method == "POST":
        user_data = {
            "name": request.form.get("name"),
            "city": request.form.get("city"),
            "hobby": request.form.get("hobby"),
            "age": request.form.get("age")
        }
    return render_template("blog.html", user_data=user_data)
