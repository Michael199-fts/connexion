from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from api.models import Sympaty
from api.service import Service

class MatchService(Service):
    custom_validations = ['self_sympaty']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            if not check(self.cleaned_data.get('user').id, self.cleaned_data['addressee']):
                if check_match(self.cleaned_data.get('user').id, self.cleaned_data['addressee']) == 1:
                    self.result = self.sympaty
                    self.response_status = status.HTTP_201_CREATED
                elif check_match(self.cleaned_data.get('user').id, self.cleaned_data['addressee']) == 2:
                    self.result = self.sympaty
                    self.response_status = status.HTTP_200_OK
            else:
                self.response_status = status.HTTP_400_BAD_REQUEST
        return self

    @property
    def sympaty(self):
        return Sympaty.objects.create(
            sender_id = self.cleaned_data.get('user').id,
            addressee_id = self.cleaned_data.get('addressee')
        )

    def self_sympaty(self):
        if str(self.cleaned_data.get('user').id) == str(self.cleaned_data.get('addressee')):
            self.add_error(
                "addressee",
                f"You tried to like yourself"
                )


def check(sender, addressee):
        try:
            Sympaty.objects.get(sender_id=sender, addressee_id=addressee)
            return True
        except ObjectDoesNotExist:
            return None

def check_match(sender, addressee):
        try:
            msgs_from_addressee = Sympaty.objects.get(sender_id=addressee, addressee_id=sender)
            if msgs_from_addressee:
                return 1
        except ObjectDoesNotExist:
            return 2