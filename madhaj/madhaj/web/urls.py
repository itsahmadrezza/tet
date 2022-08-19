from django.urls import path

from . import views
# Create your views here.

urlpatterns = [
    path('', views.index, name="index"),
    path('counseling-kafsh/', views.counselingKafsh, name="counseling_kafsh"),
    path('counseling-madhaj/', views.counselingMadhaj, name="counseling_madhaj"),
]
