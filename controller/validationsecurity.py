from controller.exceptions.unauthorized import Unauthorized


def validaton_token(token):
    if(token != None):
        if(valid_token(token)):
            return True
        else:
            raise Unauthorized("Invalid or expired token")
    else:
        raise Unauthorized("token is required")

def valid_token(token):
    return True