from flask import render_template, Flask, redirect, url_for, request
from gevent.pywsgi import WSGIServer
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Axess.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM bloggers')
    blogger = cursor.fetchall()
    conn.close()
    return render_template("index.html", blogger=blogger)


@app.route("/web_development")
def web_development():
    return render_template("web_development.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tables")
def tables():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM project_status')
    project_status = cursor.fetchall()
    conn.close()
    return render_template('table.html', project_status=project_status)



@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        project_name = request.form["project_name"]
        budget = request.form["budget"]
        status = request.form["status"]
        users = request.form["users"]
        completion = request.form["completion"]
        action = request.form["action"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO project_status (Project, Budget, Status, Users, Completion, Action) VALUES (?, ?, ?, ?, ?, ?)",
            (project_name, budget, status, users, completion, action)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("tables"))
    else:
        return render_template("add_project.html")


@app.route("/contact",  methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        mobile_number = request.form["mobile_number"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO contact (first_name, last_name, email, mobile_number) VALUES (?, ?, ?, ?)",
            (first_name, last_name, email, mobile_number)
        )
        conn.commit()
        conn.close()

        return render_template("index")
    else:
        return render_template("contact.html")










if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app).serve_forever()


