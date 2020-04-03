from flask import Flask
from flask import render_template

import pandas as pd

app = Flask(__name__)


df = pd.DataFrame({"Name": ["David", "Edward", "Weirich"], "Number": [1, 2, 10],})

df["Button"] = '<button type="button" class="btn btn-primary">Click Me</button>'


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("check_in.html", df=df)


if __name__ == "__main__":
    app.run(debug=True)
