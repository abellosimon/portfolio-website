from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/work")
def work():
  return render_template('home.html')

@app.route("/resume")
def resume():
  return render_template('resume.html')

@app.route("/about")
def about():
  return render_template('about.html')
#DONE: Learn to change favicon icon

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)