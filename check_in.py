from flask import Flask
from flask import render_template
from flask import request

import pandas as pd

app = Flask(__name__)

# The CSV needs to have columns Name, Last Contacted, Cadence
df = pd.read_csv('people.csv')


def update_df():
    global df

    df["Last Contacted"] = pd.to_datetime(df["Last Contacted"])
    df["Days Since"] = (pd.Timestamp.now() - df['Last Contacted']).apply(lambda x: x.days)
    df['Days Remaining'] = df['Cadence'] - df['Days Since']

    df = df.sort_values(['Days Remaining', 'Last Contacted'])

    df.drop(['Days Since', 'Days Remaining'], axis=1).to_csv('people.csv', index=False)


@app.route("/", methods=["GET", "POST"])
def home():
    global df

    if request.method == 'POST':
        if request.form.get('update') is not None:
            idx = int(request.form.get('update'))
            print('Clicked on', df.loc[idx, 'Name'])
            df.loc[idx, 'Last Contacted'] = pd.Timestamp.now()
        elif request.form.get('reload') is not None:
            print('Reloading Page')
            df = pd.read_csv('people.csv')

        update_df()

    return render_template("check_in.html", df=df)


if __name__ == "__main__":
    update_df()

    app.run(debug=True)
