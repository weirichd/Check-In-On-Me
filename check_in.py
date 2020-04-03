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


def update_df():
    global df

    df = df.sort_values('Last Contacted')
    df["Last Contacted"] = pd.to_datetime(df["Last Contacted"])
    df["Days Since"] = (pd.Timestamp.now() - df['Last Contacted']).apply(lambda x: x.days)


@app.route("/", methods=["GET", "POST"])
def home():
    global df

    if request.method == 'POST':
        idx = int(request.form.get('update'))

        print('Clicked on', idx)

        df.loc[idx, 'Last Contacted'] = pd.Timestamp.now()

        update_df()

    return render_template("check_in.html", df=df)


if __name__ == "__main__":
    update_df()

    app.run(debug=True)
