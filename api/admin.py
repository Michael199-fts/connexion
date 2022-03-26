from django.contrib import admin
from api.models import Participant, Sympaty

# Register your models here.
admin.site.register(Sympaty)

@admin.register(Participant)
class AdminParticipant(admin.ModelAdmin):
    list_display = ('username', 'email', 'id',)

    def save_model(self, request, obj, form, change):
        update_fields = []
        for key, value in form.cleaned_data.items():
            if key != 'user_permissions' and key != 'groups':
            # True if something changed in model
                if value != form.initial[key]:
                    update_fields.append(key)

        obj.save(update_fields=update_fields)
