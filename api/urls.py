from django.urls import path
from . import views


urlpatterns = [
    path('lstcon', views.list_conversation),
    path('con/<int:id>', views.get_conversation)
]