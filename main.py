from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():

    stats = {
        "traffic": 9996,
        "normal": 7957,
        "threats": 2039,
        "accuracy": "99.8%"
    }

    return render_template(
        "dashboard.html",
        stats=stats
    )


if __name__ == "__main__":
    print("=" * 55)
    print("🛡️ NIDS WEB DASHBOARD")
    print("=" * 55)
    print("🌐 Starting security dashboard...")
    print("➡️ Open: http://127.0.0.1:5000")
    print("=" * 55)

    app.run(
        debug=True
    )