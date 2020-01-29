from django.views.generic import ListView
from .models import post
class sos(ListView):
	model = post
	template_name = 'get.html'
	context_object_name='app1'