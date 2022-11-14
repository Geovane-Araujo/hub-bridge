import json

from flask import Blueprint, request

from controller.requests import request_post, request_post_sob
from controller.validationsecurity import validaton_token

hubBridge = Blueprint("hubbridge",__name__,template_folder="controller")

@hubBridge.route('/rest/<string:service>/<string:method>/<string:route>', methods=['GET', 'POST'])
def bridge(service,method,route):
    token = request.headers.get("Authorization")
    data = request.get_json()
    validaton_token(token)
    index = request.base_url.index("localhost")
    request_post(token, service, route,data,index)
    return json.dumps('deu boa')

@hubBridge.route('/rest/anonymous/<string:service>/<string:method>/<string:route>', methods=['GET', 'POST'])
def bridge_anonimous(service,method,route):
    data = request.get_json()
    try:
        index = request.base_url.index("localhost")
    except Exception as ix:
        index = 0
    ret = request_post_sob("", service, route, data,index)
    return json.dumps(ret)

def authorization():
    return ''

