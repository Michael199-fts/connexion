import numpy as np
from numpy import arccos, sin, cos

from api.models import Participant
from api.service import Service


class ParticipantsListService(Service):
    sorting_values = ["username", "first_name", "last_name", "sex", "distance",
                      "-username", "-first_name", "-last_name", "-sex", "-distance"]
    custom_validations = []

    def process(self):
        self.result = self._participants
        return self

    @property
    def _participants(self):
        latitude, longitude = self.cleaned_data.get('user').latitude, self.cleaned_data.get('user').longitude,
        query = Participant.objects.all().exclude(id=self.cleaned_data.get('user').id).order_by('username')
        if self.cleaned_data.get('sort_by') and self.cleaned_data.get('sort_by') in self.sorting_values:
            data = {el: count_dist(latitude, longitude, el.latitude, el.longitude) for el in query}
            if self.cleaned_data.get('sort_by') == "distance":
                return [{"user": el, "distance": di} for el, di in
                        dict(sorted(data.items(), key=lambda x: x[1])).items()]
            elif self.cleaned_data.get('sort_by') == "-distance":
                return [{"user": el, "distance": di} for el, di in
                        dict(sorted(data.items(), key=lambda x: x[1], reverse=True)).items()]
            return query.order_by(self.cleaned_data.get('sort_by'))
        return [{"user": el, "distance": 0.0} for el in query]

def count_dist(latitude_user, longitude_user, latitude_sec_user, longitude_sec_user):
    x1, x2, y1, y2 = float(latitude_user), float(longitude_user), float(latitude_sec_user), float(longitude_sec_user)
    distance = 6371 * arccos(sin(x1 * np.pi / 180) * sin(x2 * np.pi / 180) + cos(x1 * np.pi / 180) *
                             cos(x2 * np.pi / 180) * cos(y1 * np.pi / 180 - y2 * np.pi / 180))
    return distance
