
from django.contrib import admin
from django.urls import path
from .views import ViberUserView, Callback, set_webhook, unset_webhook, \
    send_message_for_user, ViberUserListView, ViberUserCreate


urlpatterns = [
    path('callback/', Callback.as_view()),
    # path('message/', message),
    path('set_webhook/', set_webhook),
    path('unset_webhook/', unset_webhook),
    path('send_message/', send_message_for_user),
    path('hi/', ViberUserView.as_view()),
    path('all/', ViberUserListView.as_view()),
    path('user/add/', ViberUserCreate.as_view()),
    path('all/', ViberUserCreate.as_view(), name='users_all')
]
