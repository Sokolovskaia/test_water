import sqlite3
import waitress


from flask import Flask, render_template, request, redirect, url_for, session, flash


# from app import db
import os

from app import db


def start():
    app = Flask(__name__)
    db_url = 'db.sqlite'


    @app.route('/', methods=('GET', 'POST'))
    def hello():
        hello = db.show_all(db.open_db(db_url))
        return render_template('index.html', hello=hello)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))

    else:
        app.run(port=9879, debug=True)


if __name__ == '__main__':
    start()