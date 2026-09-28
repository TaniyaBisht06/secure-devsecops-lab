from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Secure DevSecOps Lab</h1>
    <p>This application is used for security testing.</p>

    <form action="/search" method="GET">
        <input name="q" placeholder="Search">
        <button type="submit">Search</button>
    </form>
    """


@app.route("/search")
def search():
    query = request.args.get("q", "")

    # Escape user input to prevent reflected XSS
    safe_query = escape(query)

    return f"<h2>Search Result</h2><p>You searched for: {safe_query}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
