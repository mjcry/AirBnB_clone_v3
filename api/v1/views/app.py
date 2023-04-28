#!/usr/bin/python3
"""
This module starts a Flask web application for the REST API of the AirBnB Clone v3
"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

# declare a method to handle app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    # run your Flask server (variable app)
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)

