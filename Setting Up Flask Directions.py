from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

#RUN THIS IN TERMINAL:
# export FLASK_APP=app.py
# flask run
## SHOULD RETURN A "Running on" folled by adress and port #
### A port number is essentially the endpoint of a given program or service. 
### Any Flask application you create can have whatever port number you would like, but the most common is 5000.
### Copy and paste your localhost address into your web browser. Generally, a localhost will look something like this, for context.
##RETURNS SOMETHING LIKE THIS--- localhost:5000
