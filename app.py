from flask import Flask, jsonify, render_template
from sqlalchemy import text

from database import engine

app = Flask(__name__)



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select *from jobs;"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))


@app.route("/")
def hello_jovian():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS, company_name='My-Careers')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
