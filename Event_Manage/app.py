from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        location TEXT,
        description TEXT,
        image TEXT
    )
    """)
    conn.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    event_id INTEGER
)
""")

    conn.commit()
    conn.close()


@app.route("/")
def index():

    conn = get_db()
    events = conn.execute("SELECT * FROM events").fetchall()
    conn.close()

    return render_template("index.html", events=events)


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()

        conn.execute(
        "INSERT INTO users(username,password,role) VALUES(?,?,?)",
        (username,password,"user")
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
        ).fetchone()

        conn.close()

        if user:

            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "admin":
                return redirect("/admin")

            return redirect("/")

        return "Invalid Login"

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():

    if "role" not in session or session["role"] != "admin":
        return redirect("/")

    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        location = request.form["location"]
        description = request.form["description"]
        image = request.files["image"]

        filename = image.filename
        image.save("static/uploads/" + filename)

        conn = get_db()
        conn.execute(
            "INSERT INTO events(name,date,location,description,image) VALUES(?,?,?,?,?)",
            (name, date, location, description, filename)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_event.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):

    conn = get_db()

    if request.method == "POST":

        name = request.form["name"]
        date = request.form["date"]
        location = request.form["location"]
        description = request.form["description"]

        conn.execute(
        "UPDATE events SET name=?,date=?,location=?,description=? WHERE id=?",
        (name,date,location,description,id)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    event = conn.execute(
    "SELECT * FROM events WHERE id=?",
    (id,)
    ).fetchone()

    conn.close()

    return render_template("edit_event.html", event=event)


@app.route("/delete/<int:id>")
def delete(id):

    conn = get_db()

    conn.execute(
    "DELETE FROM events WHERE id=?",
    (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/admin")
def admin():

    if session.get("role") != "admin":
        return redirect("/")

    conn = get_db()

    events = conn.execute("SELECT * FROM events").fetchall()
    users = conn.execute("SELECT * FROM users").fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        events=events,
        users=users
    )

@app.route("/book/<int:event_id>")
def book(event_id):

    if "user_id" not in session:
        return redirect("/login")

    conn = get_db()

    conn.execute(
        "INSERT INTO bookings(user_id,event_id) VALUES(?,?)",
        (session["user_id"], event_id)
    )

    conn.commit()
    conn.close()

    return "Event booked successfully!"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)