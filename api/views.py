import pdb
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models import Sympaty, Participant
from api.serializers import RegistrationSerializer, MatchSerializer

class RegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        #avatar = Image.open(request.data['photo'])
        #draw = ImageDraw.Draw(avatar)
        #font = ImageFont.truetype("arial.ttf", size=60)
        #draw.text((40, 40), 'connexionWM', font=font)
        #avatar.save('photos/'+request.FILES['photo'].name)
        #request.data['photo'] = 'photos/'+request.FILES['photo'].name
        return self.create(request, *args, **kwargs)

class MatchAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MatchSerializer
    queryset = Sympaty.objects.all()

    def post(self, request, *args, **kwargs):
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