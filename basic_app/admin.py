from django.contrib import admin
from basic_app.models import Bots, Users
class AdminUsers(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'chat_id', 'username', 'created_at']

admin.site.register(Users, AdminUsers)
class BotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'api_key']

admin.site.register(Bots, BotsAdmin)