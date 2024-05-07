from django.contrib import admin
from basic_app.models import Bots, Users
class AdminUsers(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'username','status', 'created_at']
    list_filter = ['status', 'created_at', 'chat_id', 'bot_id']

admin.site.register(Users, AdminUsers)
class BotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'api_key']

admin.site.register(Bots, BotsAdmin)