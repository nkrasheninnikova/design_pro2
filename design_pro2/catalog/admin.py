from django.contrib import admin

from .models import *

admin.site.register(Request)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Avatar)