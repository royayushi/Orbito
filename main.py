#To-do: 1.Use flask to connect twilio to the webapp. 2. Store the ph no and name inserted in json or database, and send messages using twilio. 3. Connect flask with the html page developed.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
