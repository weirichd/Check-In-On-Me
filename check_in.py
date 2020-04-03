from flask import Flask
from flask import render_template
from flask import request

import pandas as pd

app = Flask(__name__)


df = pd.DataFrame(
    {
        "Name": ["David Weirich", "Edward", "Weirich"],
        "Last Contacted": ["2020-01-01", "2020-01-02", "2020-02-19"],
    }
)

df["Last Contacted"] = pd.to_datetime(df["Last Contacted"])


@app.route("/", methods=["GET", "POST"])
def home():
    global df

    if request.method == 'POST':
        print('Clicked on', request.form.get('update'))

    return render_template("check_in.html", df=df)


if __name__ == "__main__":
    app.run(debug=True)
