from api.models import Participant
from api.serializers import RegistrationSerializer
from api.service import Service
from django.contrib.auth.hashers import make_password


class RegisterUserService(Service):
    custom_validations = ["check"]


    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._user
        return self

    @property
    def _user(self):
        return Participant.objects.create(
            username=self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            sex=self.cleaned_data.get('sex'),
            email=self.cleaned_data.get('email'),
            password=make_password(self.cleaned_data.get('password')),
            photo=self.cleaned_data.get('photo')
        )

    def check(self):
        for field in RegistrationSerializer.Meta.fields:
            if field not in self.cleaned_data.keys():
                self.add_error(
                    field,
                    f"Required field"
                )