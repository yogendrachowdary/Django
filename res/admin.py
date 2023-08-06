from django.contrib import admin
from .models import Contact,Login,Register,Feedback
# Register your models here.

admin.site.register(Contact)

admin.site.register(Login)

admin.site.register(Register)
admin.site.register(Feedback)