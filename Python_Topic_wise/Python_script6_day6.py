# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://veeramallaabhishek.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

# study Readme.md
#  “I integrated GitHub with Jira using a Python Flask REST API. I created a Flask endpoint /createJira that receives a POST request and uses Jira Cloud’s REST API to create a Jira issue programmatically.

# In the integration, I configured the Jira project key, issue type, summary, and description in the request payload. The description follows Jira’s Atlassian Document Format (ADF), which is required by Jira Cloud.

# For authentication, I used Jira Cloud API-token-based authentication with HTTPBasicAuth, where the Jira account email is used as the username and the API token is used as the password.

# The Python application sends a POST request to Jira’s /rest/api/3/issue endpoint using the requests library. Jira then creates the issue and returns the issue details, including the Jira issue key.

# This Flask service can then be triggered from GitHub—for example, through a GitHub webhook when a particular GitHub event occurs. So the overall flow is GitHub event → Flask API → Jira REST API → Jira issue creation.”