from django.urls import path, include
from core.views import HomeView, ClientView

urlpatterns = [
   path('home/', HomeView.as_view(), name='home'),
   path('customer/', ClientView.as_view(), name='customer'),
   path('work/', ClientView.as_view(), name='work')
]
