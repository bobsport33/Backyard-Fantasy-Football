from target_share import season_target_share
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    table_df = season_target_share()
    return render_template('index.html', tables=[table_df.to_html(classes='table table-striped text-center').replace('border="1"','border="0"')])


if __name__ == "__main__": 
    app.run()