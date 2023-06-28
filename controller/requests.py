import http
import json

import requests

from services.services import Services


def request_post(token, service, route,json_data,local):

    services = Services()
    port = services.services[service]
    host = ""
    if(local > 1):
        host = services.host["local"]
    else:
        host = services.host["server"]

    url = f"https://{host}:{port}/{service}/{route}"

    payload = json.dumps(json_data)
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
def request_post_sob(token, service, route, json_data, local):

    services = Services()
    port = services.services[service]

    host = ""
    if(local > 1):
        host = services.host["local"]
    else:
        host = services.host["server"]

    conn = http.client.HTTPConnection(host,port)
    payload = json.dumps(json_data)
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", f"/{service}/{route}", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode()

def request_bridge(request, any_path):

    data = None
    if request.method ==  'POST' or request.method == 'PUT':
        data = request.get_json()

    token = request.headers.get("Authorization")

    payload = json.dumps(data)
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    url = "f{}"

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text