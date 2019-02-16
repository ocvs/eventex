from django.urls import path

from eventex.subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<str:masked_id>/', detail, name='detail'),
]
