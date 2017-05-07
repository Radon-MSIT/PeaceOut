from django.conf import settings

from django.shortcuts import render, redirect

from .models import Info

from .forms import InfoForm  

def home(request):
	form = InfoForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)

		instance.save()
		return redirect("http://www.beyondintractability.org/essay/peace-through-tourism")
	
	return render(request, "home.html", context)