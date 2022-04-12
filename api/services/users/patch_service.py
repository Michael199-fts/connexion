from django.contrib.auth.hashers import make_password

from api.models import Participant
from api.service import Service


class PatchUserService(Service):
    custom_validations = []
    participant_fields = ['username', 'first_name', 'last_name', 'sex',
                          'photo', 'email', 'latitude', 'longitude', 'password']

    def process(self):
        instance = Participant.objects.get(id=self.cleaned_data['user'].id)
        update_fields = []
        for el, val in self.cleaned_data.items():
            if el == 'user':
                continue
            if el == 'password':
                instance.password = make_password(self.cleaned_data.get('password'))
                update_fields.append('password')
                continue
            else:
                if el in self.participant_fields:
                    setattr(instance, el, val)
                    update_fields.append(el)
        instance.save(update_fields=update_fields)
        self.result = self._user
        return self

    @property
    def _user(self):
        user = Participant.objects.get(id=self.cleaned_data['user'].id)
        return user
