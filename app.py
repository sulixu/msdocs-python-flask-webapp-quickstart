import os
import requests
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

#
# to test: curl -X GET -H "access-token: $accessToken" http://127.0.0.1:5000/


# api_endpoint = 'https://graph.microsoft.com/v1.0/users'
# headers = {'Authorization': f'Bearer {bearer_token}'}
#
# # Make a request to the API
# response = requests.get(api_endpoint, headers=headers).json()
#
# # Print the response
# print(json.dumps(response, indent=2))

@app.before_request
def authenticate():
    # Get the token from the request headers
    access_token = request.headers.get("access-token")
    api_endpoint = 'https://graph.microsoft.com/v1.0/users'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_endpoint, headers=headers)
    print(response)
    if response.status_code != 200:
        return "login failed"


@app.route('/')
def index():
   print('login succeeded! Request for index page received')
   return "hi, you are logged in!"


# Backend URI
@app.route("/backend")
def backend():
    return "Authenticated User - Backend Content"


if __name__ == '__main__':
   app.run(debug=True)
