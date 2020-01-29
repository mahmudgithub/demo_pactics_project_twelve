from django.urls import path
from .views import sos

urlpatterns = [
	path('',sos.as_view(),name='hello'),
]
