import pdb

import numpy as np
from django.core.exceptions import ObjectDoesNotExist
from numpy import arccos, sin, cos
from rest_framework import status

from api.models import Participant
from api.service import Service


class ParticipantsListService(Service):
    custom_validations = []

    def process(self):
        pdb.set_trace()
        if 'sort_by' not in self.cleaned_data:
            query = Participant.objects.all()
            query = query.order_by('username')
            self.result = query
        if self.cleaned_data.get('sort_by') == 'username':
            query = Participant.objects.all()
            query = query.order_by('username')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'username_reversed':
            query = Participant.objects.all()
            query = query.order_by('-username')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'first_name':
            query = Participant.objects.all()
            query = query.order_by('first_name')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'first_name_reversed':
            query = Participant.objects.all()
            query = query.order_by('-first_name')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'last_name':
            query = Participant.objects.all()
            query = query.order_by('last_name')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'last_name_reversed':
            query = Participant.objects.all()
            query = query.order_by('-last_name')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'sex':
            query = Participant.objects.all()
            query = query.order_by('sex')
            self.result = query
        elif self.cleaned_data.get('sort_by') == 'sex_reversed':
            query = Participant.objects.all()
            query = query.order_by('-sex')
            self.result = query
        else:
            query = Participant.objects.all()
            query = query.order_by('username')
            self.result = query
        self.response_status = status.HTTP_200_OK
        return self


def cum(x1, y1, x2, y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    S = 6371 * arccos(sin(x1 * np.pi / 180) * sin(x2 * np.pi / 180) + cos(x1 * np.pi / 180) * cos(x2 * np.pi / 180) *
                      cos(y1 * np.pi / 180 - y2 * np.pi / 180))
    return S
