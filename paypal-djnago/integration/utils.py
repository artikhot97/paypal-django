import base64
import os
import requests
from dotenv import load_dotenv
load_dotenv()


def get_paypal_token():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    payload = 'grant_type=client_credentials'
    encoded_auth = base64.b64encode((client_id + ':' + client_secret).encode())
    headers = {
        'Authorization': f'Basic {encoded_auth.decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.request("POST", url, headers=headers, data=payload)
    return r.json()["access_token"]


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
