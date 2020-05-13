"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <p>Hi! This is the home page.</p>
      <p>Click <a href="/hello">here</a> for some fun.</p>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div>What's your name? <input type="text" name="person"></div>
          <div>Choose a compliment:<br />
            <select name="compliment">
              <option value="awesome">awesome</option>
              <option value="terrific">terrific</option>
              <option value="fantastic">fantastic</option>
              <option value="neato">neato</option>
              <option value="fantabulous">fantabulous</option>
              <option value="wowza">wowza</option>
          </div>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          <div>Want a diss instead?<br />
          <select name="diss">
            <option value="grody">grody</option>
            <option value="snotty">snotty</option>
          </div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name and compliment them."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
  """Get user by name and diss them."""

  player = request.args.get("person")

  diss = request.args.get("diss")

  return """
  <!doctype html>
  <html>
    <head>
      <title>A Diss</title>
    </head>
    <body>
      Ugh, you're {}!
    </body>
  </html>
  """.format(diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
