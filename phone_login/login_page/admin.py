from django.contrib import admin
from .models import User_phone_number,Verify_number

class Verify_numberAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number')


class User_phone_numberAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number')



admin.site.register(Verify_number, Verify_numberAdmin)
admin.site.register(User_phone_number, User_phone_numberAdmin)