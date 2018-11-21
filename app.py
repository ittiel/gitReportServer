from flask import Flask, request, jsonify, render_template, redirect
import os
import json
from database import db_session
from models import GitMsg
import logging

app = Flask(__name__)

# display the report
@app.route('/')
def index():
    gitMsg = GitMsg.query.all()
    return render_template('index.html', gitMsg=gitMsg)

# get the data from the clients
@app.route('/backend', methods=["POST", "GET"])
def backend():
    app.logger.info(json.dumps(request.get_json(force=True)))
    content = json.loads(json.dumps(request.get_json(force=True)))


    # gitMsg = content["gitMsg"]
    user = content["user"]
    branch = content["branch"]
    repository = content["repository"]
    files = content["files"]
    diff = content["diff"]
    commitMsg = content["commitMsg"]
    new_gitMsg = GitMsg(user, branch, repository, files, diff, commitMsg)

    db_session.add(new_gitMsg)
    db_session.commit()

    render_template('index.html', data=new_gitMsg)
    return redirect("/backend", code=302)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

 #todo: allow different ports?
# run Flask app
if __name__ == "__main__":
    file_handler = logging.FileHandler('app.log')
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    
    app.run(debug=True, host='0.0.0.0')