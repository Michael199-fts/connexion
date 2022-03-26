from PIL import Image, ImageDraw, ImageFont
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Sympaty, Participant
from api.serializers import RegistrationSerializer, MatchSerializer, ParticipantSerializer
from api.service import ServiceOutcome
from api.services.users.auth import AuthUserService
from api.services.users.registrated import RegisterUserService


class RegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(RegisterUserService, {**dict(request.data.items())}, request.FILES.dict())
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(ParticipantSerializer(service_outcome.result).data, status=status.HTTP_201_CREATED)

class MatchAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MatchSerializer
    queryset = Sympaty.objects.all()

    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        try:
            if request.data['sender'] == Sympaty.objects.get(sender = request.data['sender'])\
                and request.data['addressee'] == Sympaty.objects.get(addressee = request.data['addressee']):
                return Response('Вы уже отправляли симпатию!')
            else:
                return self.create(request, *args, **kwargs)
        except:
            return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        try:
            msgs_from_addressee = Sympaty.objects.get(addressee = request.data['sender'])
            if request.data['sender'] == str(msgs_from_addressee.addressee.id):
                username = Participant.objects.get(pk=request.data['addressee']).username
                email = Participant.objects.get(pk=request.data['addressee']).email
                return Response('Вы понравились '+username+'! Почта участника: '+email,
                                headers=headers)
            else:
                return Response('Симпатия отправлена! Ждите ответной симпатии от участника else',
                                headers=headers)
        except:
            return Response('Симпатия отправлена! Ждите ответной симпатии от участника, exp',
                            headers=headers)

class AuthenticationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(AuthUserService, request.data)
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(service_outcome.result, status=status.HTTP_200_OK)