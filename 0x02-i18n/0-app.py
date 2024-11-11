#!/usr/bin/env python3
"""
Basic Flask application for i18n project
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ Render the index page. """
    return render_template('0-index.html')

if _name_ == '__main__':
    app.run(host='0.0.0.0', port=5000)
