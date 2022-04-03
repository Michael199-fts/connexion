from rest_framework import status

from api.models import Participant
from api.service import Service


class ParticipantsListService(Service):
    custom_validations = []
    def process(self):
        if 'sort_by' not in self.cleaned_data:
            query = Participant.objects.all()
            query = query.order_by('username')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'username':
            query = Participant.objects.all()
            query = query.order_by('username')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'username_reversed':
            query = Participant.objects.all()
            query = query.order_by('-username')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'first_name':
            query = Participant.objects.all()
            query = query.order_by('first_name')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'first_name_reversed':
            query = Participant.objects.all()
            query = query.order_by('-first_name')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'last_name':
            query = Participant.objects.all()
            query = query.order_by('last_name')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'last_name_reversed':
            query = Participant.objects.all()
            query = query.order_by('-last_name')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'sex':
            query = Participant.objects.all()
            query = query.order_by('sex')
            self.result = query
            self.response_status = status.HTTP_200_OK
        elif self.cleaned_data.get('sort_by') == 'sex_reversed':
            query = Participant.objects.all()
            query = query.order_by('-sex')
            self.result = query
            self.response_status = status.HTTP_200_OK
        return self