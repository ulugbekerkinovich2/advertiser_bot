from django.db import models


class Bots(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'bots'
        verbose_name_plural = 'Bots'

class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    bot_id = models.ForeignKey(Bots, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, default='blocked')
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        db_table = 'users'

