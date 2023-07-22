from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
  {
    'id':'1',
    'title':'Web developer',
    'location':'Egypt',
    'salary':'10000 LE'
  },
  {
    'id':'2',
    'title':'Front end developer',
    'location':'Dubai',
  
  },
  {
    'id':'3',
    'title':'Full stack developer',
    'location':'KSA',
    'salary':'8000 SR'
  },
    {
    'id':'4',
    'title':'Software developer',
    'location':'KSA',
    'salary':'8000 SR'
  },
    {
    'id':'5',
    'title':'Cloud Engineer',
    'location':'KSA',
    'salary':'8000 SR'
  },
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS, company_name="Tech")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
  