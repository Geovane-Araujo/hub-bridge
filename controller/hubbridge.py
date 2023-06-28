import json

from flask import Blueprint, request, make_response

from controller.requests import request_post, request_post_sob, request_bridge


hubBridge = Blueprint("hubbridge",__name__,template_folder="controller")

@hubBridge.route('/rest/<string:service>/<string:method>/<string:route>', methods=['GET', 'POST'])
def bridge(service,method,route):
    token = request.headers.get("Authorization")
    data = request.get_json()
    #validaton_token(token)
    index = request.base_url.index("localhost")
    request_post_sob(token, service, route,data,index)
    return json.dumps('deu boa')


@hubBridge.route('/rest/<path:any_path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def bridge_services(any_path):
    response = make_response(request_bridge(request, any_path))
    response.headers['Content-Type'] = 'application/json'
    return response


def authorization():
    return ''

