from django.urls import path
from basic_app.views import BotsList, UsersList,UserDetail

urlpatterns = [
    path('bots/post', BotsList.as_view()),
    path('users/post', UsersList.as_view()),
    path('bots/get', BotsList.as_view()),
    path('users/get', UsersList.as_view()),
    path('users/delete/<int:pk>', UserDetail.as_view()),
]