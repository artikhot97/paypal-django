import base64
import os
import requests
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

print(client_id)
print(client_secret)
url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"


def paypal_token():
    data = {
                "client_id":client_id,
                "client_secret":client_secret,
                "grant_type":"client_credentials"
            }
    headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic {0}".format(base64.b64encode((client_id + ":" + client_secret).encode()).decode())
            }

    print(headers)
    token = requests.post(url, data, headers=headers,  )
    print(token, "token")
    return token.json()['access_token']


class ResponseInfo(object):
    """
    Class for setting how API should send response.
    """

    def __init__(self, user=None, **args):
        self.response = {
            "status_code": args.get('status', 200),
            "error": args.get('error', None),
            "data": args.get('data', []),
            "message": [args.get('message', 'Success')]
        }

def return_response(data, error, code, message=None):
    response_format = ResponseInfo().response
    response_format["data"] = data
    response_format["error"] = error
    response_format["status_code"] = code
    if message:
        response_format["message"] = [message]
    return response_format