from django.contrib import admin
from .models import Client, Personnel, Activity, Assurance

# Register your models here.


admin.site.register(Personnel)
admin.site.register(Activity)
admin.site.register(Client)
admin.site.register(Assurance)
