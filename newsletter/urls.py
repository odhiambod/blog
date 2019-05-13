from django.urls import path
from newsletter.views import signupform

app_name = 'newsletter'

urlpatterns = [
	path('signup/', signupform, name='signupview'),
]