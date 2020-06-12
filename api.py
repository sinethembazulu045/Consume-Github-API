import requests
import datetime as dt



def PR(repo_name, start_date, end_date):
    pull_request = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=453")     
    my_data = pull_request.json()
    return my_data
# print(PR('Umuzi-org','1-12-2019','5-6-2020'))