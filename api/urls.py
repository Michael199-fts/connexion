from django.urls import path

from api.views import RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='Регистрация'),
]