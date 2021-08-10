import requests 
import os 
import argparse
from pprint import pprint

#get command line args 
parser = argparse.ArgumentParser()
parser.add_argument("--user", "-u", type = str, dest = "user", required = True)
parser.add_argument("--name", "-n", type = str, dest = "name", required = True)
parser.add_argument("--private", "-p", dest = "is_private", action = "store_true")
args = parser.parse_args()

user_name = args.user
repo_name = args.name
is_private = args.is_private


GITHUB_TOKEN = os.environ['GIT_TOKEN']

API_URL = "https://api.github.com"
if is_private:
    payload = '{"name": "' + repo_name + '", "private": true}'
else:
    payload = '{"name": "' + repo_name + '", "private": false}'

print(payload)

headers = {
        "Authorization": "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
}

try:
    r = requests.post(API_URL+"/user/repos", data=payload, headers=headers)
    #r.raise_for_status()
    #pprint(r.json())

except requests.exceptions.RequestException as err:
    raise SystemExit(err)


try:

    REPO_PATH = os.getcwd() + '/' + repo_name
    os.mkdir(REPO_PATH)
    os.chdir(REPO_PATH)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + user_name +'/' + repo_name +'.git')
    os.system("echo '#" + repo_name +"' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
    raise SystemExit(err)

