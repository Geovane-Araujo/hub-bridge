import json

from flask import Blueprint, request


hubBridge = Blueprint("hubbridge",__name__,template_folder="controller")

@hubBridge.route('/hub/<string:service>/<string:method>/<string:route>', methods=['GET', 'POST'])
#@hubBridge.route('/hub', methods=['GET', 'POST'])
def bridge(service,method,route):
    print(request.headers.get("Authorization"))
    print(service)
    print(method)
    print(route)
    return json.dumps('deuboa')

def authorization():
    return ''

