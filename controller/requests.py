import json

import requests

from services.services import Services


def request_post(token, service, route,json_data):

    services = Services()
    port = services.services[service]

    url = f"http://localhost:{port}/{service}/{route}"

    payload = json.dumps(json_data)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text