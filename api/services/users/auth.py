from rest_framework import status

from api.JWTutills import authorization
from api.service import Service


class AuthUserService(Service):
    custom_validations = []

    def process(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        response = authorization(username, password)
        if response:
            self.result = response
            return self
        else:
            self.add_error(username, 'ты еблан')
            self.response_status = status.HTTP_401_UNAUTHORIZED
            return self