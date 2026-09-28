from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Secure DevSecOps Lab</h1>
    <p>Security testing demonstration application.</p>

    <form action="/search" method="GET">
        <input name="q" placeholder="Search">
        <button type="submit">Search</button>
    </form>
    """

@app.route("/search")
def search():
    query = request.args.get("q", "")

    # Intentionally vulnerable for DAST demonstration
    return render_template_string(
        "<h2>Search Result</h2><p>You searched for: " + query + "</p>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
