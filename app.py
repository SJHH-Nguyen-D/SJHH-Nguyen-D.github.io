from flask import Flask, render_template
from model import Model
from constants import PARAMS

app = Flask(__name__)


@app.route("/<date:%Y>/<date:%m>/<slug>.html")
def sharpest_minds_project_part_9(data):
    model = Model()
    model.set_params(PARAMS)
    model.fit(data)
    job_score_prediction = model.predict(data) 
    return render_template(f"{date:%Y}/{date:%m}/{slug}.html", score=job_score_prediction)


if __name__ == "__main__":
    app.run()



# "/2019/10/3/sharpestminds-project-part-9.html"
# {% block job_score_prediction %}
    # <input>
# {% endblock %}
# Your estimated job performance score is : {{ job_score_prediction }}
# {{ plotly.plots }}