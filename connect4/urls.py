from django.urls import path
from .views import Start,Play,AuditView

urlpatterns = [
    path('start/',Start.as_view(),name="start_game"),
    path('move/',Play.as_view(),name="move" ),
    path('history/<int:game>/', AuditView.as_view(), name="history"),
   ]