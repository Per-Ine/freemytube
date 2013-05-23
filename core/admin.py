from django.contrib import admin
from core.models import MainFrame, Video, Measurement
from rest_framework.authtoken.models import Token

admin.site.register(MainFrame)
admin.site.register(Video)
admin.site.register(Measurement)
admin.site.register(Token)
