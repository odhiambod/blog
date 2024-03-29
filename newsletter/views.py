from django.shortcuts import render
from newsletter.forms import SignupForm
app_name = 'newsletter'
# Create your views here.
def signupform(request):
	form_class = SignupForm
	#if form is submitted
	form = form_class(request.POST or None)
	if request.method == 'POST':
		#cheking the form is valid or not
		if form.is_valid():
			#if valid rendering new view with values
			#the form values contains in cleaned_data dictionary
			return render(request, 'result.html', {
				'name':form.cleaned_data['name'],
				'email':form.cleaned_data['email'],
				})
		else:
			#creating a new form
			form = SignupForm()
	#returning form
	return render(request, 'signupform.html', {'form':form});