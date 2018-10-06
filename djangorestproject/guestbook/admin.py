from django.contrib import admin

from .models import *

admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Programmer)
admin.site.register(Todo)
