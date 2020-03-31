from flask import Flask, flash, redirect
from flask import render_template, url_for


from forms import RegistarationForm, LogInForm

app = Flask(__name__)


app.config["SECRET_KEY"] = "f41bf24bfa655c8933936c47db1bdf1f"

posts = [
    {
        "author": "David Weirich",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 1, 2020",
    },
    {
        "author": "Emily Huang",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 2, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistarationForm()
    if form.validate_on_submit():
        flash(f"Account Created For {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LogInForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
