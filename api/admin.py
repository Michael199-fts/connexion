from django.contrib import admin
from api.models import Participant, Sympaty

# Register your models here.
admin.site.register(Sympaty)

@admin.register(Participant)
class AdminParticipant(admin.ModelAdmin):
    list_display = ('username', 'email', 'id',)