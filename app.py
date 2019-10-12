#!/usr/bin/env python3

import os
from github import Github
from flask import Flask
from flask import jsonify

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
gh_access_token = os.environ['GH_ACCESS_TOKEN']
g = Github(gh_access_token)

@app.route('/v1/<gh_user>/<repo>/<branch>')
def head_sha(gh_user, repo, branch):
    try:
        branch = g.get_repo("{}/{}".format(gh_user, repo)).get_branch(branch)
        return jsonify({'commit': branch.commit.sha })
    except:
        return jsonify({'commit': '' })


if __name__ == '__main__':
    app.run()
