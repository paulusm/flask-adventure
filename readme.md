# Code Club Choose Your Own Adventure

![fork](images/forkinroad.jpg)

## A Python, Flask and HTML Project


This is a simple web application for creating an interactive adventure. To get started make a new folder, then open that in Visual Studio Code

1. Create a file in your project called adventuredata.py. This is the data for your adventure and includes the choices for the player at each step. It is "nested" dictionary, so has dictionaries inside other dictionaries.

```python
data = {
    "start": {
        "text": "You are at a junction in the road, you have two choices, which way do you want to go?",
        "choices" : {
            "left" : "hole",
            "right" : "wonderland"
        }
    },
    "hole": {
        "text": "You fell down a hole and knocked yourself out!",
        "choices" : {
            "next" : "end"
        }
    },
    "wonderland": {
        "text": "You have found the paradise of wonderland, congratulations!",
        "choices" : {
            "next" : "end"
        }
    },
    "end": {
        "text": "Your adventure is over :(",
        "choices" : {
            "Try again" : "start"
        }
    }
}
```
2. Here is your app.py file, which sets up the Flask application. It imports the data and has a flexible route for each adventure step.

```python

from flask import Flask
from flask import render_template
from adventuredata import data

app = Flask(__name__)

@app.route("/<name>")
def choice(name):
    return render_template('step.html', step=name, data=data[name])

if __name__ == '__main__':
  app.run(debug=True)

```
3. This won't work yet, as we need a "template" that will for them HTML displayed to the user, Call this step.html:

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/style.css">
    <title>Adventure</title>
</head>
<body>
   <h1>My Adventure Game</h1>
   <h2>{{step}}</h2>
   <p>{{data.text}}</p>
   <ol>
    {% for choice, destination in data.choices.items() %}
     <li><a href="{{ destination }}">{{ choice }}</a></li>
    {% endfor %}
   </ol>
</body>
</html>

```

4. In the above, you will notice a stylesheet link. This needs to be created, so add a new subfolder called "static" and create the file style.css in there.

```css

body{
    font-family: Helvetica;
    margin: 3em;
}

```