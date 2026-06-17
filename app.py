from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/learn_more")
def learn_more():
    return render_template("learn_more.html")


@app.route("/search")
def search():
    query = request.args.get("q", "")  # Gets the search query from URL ?q=...
    # Add your search logic here
    results = [
        {"title": "Home", "url": "/"},
        {"title": "Contact", "url": "/contact"},
        {"title": "Learn More", "url": "/learn_more"},
    ]
    # Replace with actual search results
    results = [p for p in pages if query in p["title"].lower()]

    return render_template("search.html", query=query, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
