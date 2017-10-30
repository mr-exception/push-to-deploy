from flask import Flask
from flask import request
import os
import json
app = Flask(__name__)

def get_repository_informations(repo_name):
  config = json.loads(open('config.json', 'r').read())
  for repo in config['repos']:
    if repo['code'] == repo_name:
      return repo
  return None
  

@app.route("/", methods=['POST', 'GET'])
def pull():
    json_input = request.json
    repo = get_repository_informations(json_input['repository']['name'])
    if repo != None:
      print("new push from repo: {0}".format(repo['title']))
      for command in repo['script']:
        os.system(command)
      return 'its ok!'
    else:
      return 'repo not found!'

app.run(port=5445)