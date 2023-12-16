import requests
import os
import base64

ip = os.environ.get('ip')
port = os.environ.get('port')
user = os.environ.get('user')
password = os.environ.get('password')

baseurl = f"http://{ip}:{port}/api/v1"
encoded_auth = base64.b64encode(f"{user}:{password}".encode())

headers = {
    'authorization': f"Basic {encoded_auth.decode()}"
    }

def get_system_version():
    url = baseurl + "/system/version"
    return requests.request("GET", url, headers=headers).json()

def get_users():
    url = baseurl + "/users"
    return requests.request("GET", url, headers=headers).json()

def get_tty():
    url = baseurl + "/serial/tty"
    return requests.request("GET", url, headers=headers).json()