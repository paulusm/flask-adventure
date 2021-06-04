from flask import Flask
from flask import render_template
from adventuredata import data

app = Flask(__name__)

@app.route("/<name>")
def choice(name):
    return render_template('step.html', step=name, data=data[name])

if __name__ == '__main__':
  app.run(debug=True)