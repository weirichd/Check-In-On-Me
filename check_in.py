from flask import Flask
from flask import render_template
from flask import request

import pandas as pd

app = Flask(__name__)

df = pd.read_csv('people.csv')


def update_df():
    global df

    df = df.sort_values('Last Contacted')
    df["Last Contacted"] = pd.to_datetime(df["Last Contacted"])
    df["Days Since"] = (pd.Timestamp.now() - df['Last Contacted']).apply(lambda x: x.days)

    df.drop('Days Since', axis=1).to_csv('people.csv', index=False)


@app.route("/", methods=["GET", "POST"])
def home():
    global df

    if request.method == 'POST':
        idx = int(request.form.get('update'))

        print('Clicked on', df.loc[idx, 'Name'])

        df.loc[idx, 'Last Contacted'] = pd.Timestamp.now()

        update_df()

    return render_template("check_in.html", df=df)


if __name__ == "__main__":
    update_df()

    app.run(debug=True)
