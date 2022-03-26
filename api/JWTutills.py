from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework_jwt.views import jwt_response_payload_handler

from api.models import Participant

def authorization(username, password):
    user = find_user(username, password)
    if user:
        payload = jwt_payload_handler(user)
        response = jwt_response_payload_handler(jwt_encode_handler(payload), user)


        return response

def find_user(username, password):
    import pdb
    pdb.set_trace()
    try:
        user = Participant.objects.get(username=username)
        check = user.check_password(password)
        if check:
            return user
    except:
        pass
