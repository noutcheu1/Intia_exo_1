from django.urls import path, include
from .views import HomeView, ClientView, post_client, update_client

urlpatterns = [
   path('home/', HomeView.as_view(), name='home'),
   path('customer/', ClientView.as_view(), name='customer'),
   path('work/', ClientView.as_view(), name='work'),
   path('addclient/', post_client, name='addclient'),
   path('update_client/pk', update_client, name='update_client')
]
