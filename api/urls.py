from django.urls import path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from api.views import RegistrationAPIView, MatchAPIView, AuthenticationAPIView, ParticipantsListAPIView, \
    PatchUpdateParticipantAPIView
from connexion.settings import BASE_URL

urlpatterns = [
    path('reg/', RegistrationAPIView.as_view(), name='Регистрация'),
    path('match/', MatchAPIView.as_view(), name='Симпатия'),
    path('auth/', AuthenticationAPIView.as_view(), name='Аутентификация'),
    path('list/', ParticipantsListAPIView.as_view(), name='Список участников'),
    path('main_cab/', PatchUpdateParticipantAPIView.as_view(), name='Личный кабинет')
]

schema_view = get_schema_view(
   openapi.Info(
      title="Site API",
      default_version='v1',
      description="Documentation for Site API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   patterns=urlpatterns,
   url=f"{BASE_URL}",
   public=True,
   permission_classes=(permissions.AllowAny,),)

urlpatterns += [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        ]