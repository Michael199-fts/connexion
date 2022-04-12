from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import MatchSerializer, ParticipantSerializer, ParticipantsListSerializer
from api.service import ServiceOutcome
from api.services.users.authentication_service import AuthUserService
from api.services.users.patch_service import PatchUserService
from api.services.users.sympaty_create_service import MatchService
from api.services.users.participants_list_service import ParticipantsListService
from api.services.users.registration_service import RegisterUserService


class RegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(RegisterUserService, {**dict(request.data.items())}, request.FILES.dict())
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(ParticipantSerializer(service_outcome.result).data, status=status.HTTP_201_CREATED)

class PatchUpdateParticipantAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(PatchUserService, {'user':request.user,
                                                               **dict(request.data.items())}, request.FILES.dict())
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(ParticipantSerializer(service_outcome.result).data, status=status.HTTP_200_OK)


class MatchAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(MatchService, {'user':request.user, **request.data})
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(MatchSerializer(service_outcome.result).data, service_outcome.response_status)

class AuthenticationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(AuthUserService, request.data)
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(service_outcome.result, status=status.HTTP_200_OK)

class ParticipantsListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        service_outcome = ServiceOutcome(ParticipantsListService, {'user':request.user, **request.query_params})
        if bool(service_outcome.errors):
            return Response(service_outcome.errors, service_outcome.response_status or status.HTTP_400_BAD_REQUEST)
        return Response(ParticipantsListSerializer(service_outcome.result, many=True).data, service_outcome.response_status)
