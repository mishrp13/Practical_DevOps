Github_Jira Integration

“I integrated GitHub with Jira using a Python Flask REST API. I created a Flask endpoint /createJira that receives a POST request and uses Jira Cloud’s REST API to create a Jira issue programmatically.

In the integration, I configured the Jira project key, issue type, summary, and description in the request payload. The description follows Jira’s Atlassian Document Format (ADF), which is required by Jira Cloud.

For authentication, I used Jira Cloud API-token-based authentication with HTTPBasicAuth, where the Jira account email is used as the username and the API token is used as the password.

The Python application sends a POST request to Jira’s /rest/api/3/issue endpoint using the requests library. Jira then creates the issue and returns the issue details, including the Jira issue key.

This Flask service can then be triggered from GitHub—for example, through a GitHub webhook when a particular GitHub event occurs. So the overall flow is GitHub event → Flask API → Jira REST API → Jira issue creation.”

----so when anyone comments /jira github webhook triggers and  it sends post request to flask api and from the the request goes to Jira to create a jira ticket .



--------------------------------------------------------------------------------