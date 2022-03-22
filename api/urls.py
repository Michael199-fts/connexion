from django.urls import path

from api.views import RegistrationAPIView, MatchAPIView

urlpatterns = [
    path('reg/', RegistrationAPIView.as_view(), name='Регистрация'),
    path('match/', MatchAPIView.as_view(), name='Симпатия')
]