from github import Github

import urllib3
import requests

from credentials import Token_access
#from credentials import PASSWORD


g = Github(Token_access)

repos = g.get_user().get_repos()


  
repos_information =[]
for repo in repos:
    data=[]
    data.append(repo.name)
    data.append(repo.startdate)
    print(repos_information)