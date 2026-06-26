from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    if request.method == "POST":
        # Optional: read form fields
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # TODO: save/send message here

        flash("Thank you! Your message has been sent.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.route("/learn_more")
def learn_more():
    return render_template("learn_more.html")


@app.route("/content")
def content():
    return render_template("content.html")


@app.route("/stage-3")
def stage_3():
    return render_template("content pages/stage_3.html")


@app.route("/stage-4")
def stage_4():
    return render_template("content pages/stage_4.html")


@app.route("/stage-5")
def stage_5():
    return render_template("content pages/stage_5.html")


@app.route("/stage-6")
def stage_6():
    return render_template("content pages/stage_6.html")


@app.route("/stage-3/questions")
def stage_3_questions():
    return render_template("practice pages/stage_3_questions.html")


@app.route("/stage-4/questions")
def stage_4_questions():
    return render_template("practice pages/stage_4_questions.html")


@app.route("/stage-5/questions")
def stage_5_questions():
    return render_template("practice pages/stage_5_questions.html")


@app.route("/stage-6/questions")
def stage_6_questions():
    return render_template("practice pages/stage_6_questions.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    username = ""

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        message = f"Demo only: login submitted for '{username or 'guest'}'."

    return render_template("login.html", message=message, username=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
