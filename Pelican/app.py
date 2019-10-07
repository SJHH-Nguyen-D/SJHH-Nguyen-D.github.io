from flask import Flask, render_template, redirect
from model import Model
from constants import PARAMS
import dash
from werkzeug.wsgi import DispatcherMiddleware
import os
import dash_app

flask_app = Flask(__name__)

dash_app = dash_app(__name__, 
server=flask_app, 
url_base_pathname=os.getcwd()
)

application = DispatcherMiddleware(flask_app, {'/dash': dash_app.server})


@flask_app.route("/<date:%Y>/<date:%m>/sharpestminds-project-part-9.html")
def sharpest_minds_project_part_9(data):
    model = Model()
    model.set_params(PARAMS) # params are model parameters and maybe weights
    model.fit(data)
    job_score_prediction = model.predict(data) 
    return render_template(f"{date:%Y}/{date:%m}/{slug}.html", score=job_score_prediction)

@flask_app.route('/plotly_dashboard') 
def render_dashboard():
    return redirect(os.getcwd())

if __name__ == "__main__":
    flask_app.run()



# "/2019/10/3/sharpestminds-project-part-9.html"
# {% block job_score_prediction %}
    # <input>
# {% endblock %}
# Your estimated job performance score is : {{ job_score_prediction }}
# {{ plotly.plots }}