from django.contrib import admin

# Register your models here.
from reports.models import River, GidroPost, Pruladu, TelegramUser, PostReport
from reports.models import TelegramUser



admin.site.register(River)
admin.site.register(GidroPost)
admin.site.register(Pruladu)
admin.site.register(PostReport)
admin.site.register(TelegramUser)
