from django.urls import path
from . import views


urlpatterns = [
    path('con/<int:id>', views.ConversationView.as_view())
]