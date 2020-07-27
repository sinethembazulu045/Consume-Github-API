import requests
import datetime as dt
import os
from requests.auth import HTTPBasicAuth


GITHUB_NAME = os.environ.get('githubname')
GITHUB_PASS = os.environ.get('git_password')


def PullRequest(repo_owner, repo_name, start_date, end_date):
    url = "https://api.github.com/repos/{repo_owner}/{repo_name}/pulls" 
    pull_request = requests.get(url, auth=HTTPBasicAuth(GITHUB_NAME, GITHUB_PASS))
    print(pull_request.status_code)    
    pull_request_data = pull_request.json()
    return pull_request_data
    
print(PullRequest('Umuzi-org','tech-department',"2020-03-30T08:39:32Z", "2020-04-10T08:39:32Z"))

