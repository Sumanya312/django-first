from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import shorten
from .forms import bitlyForm, editBitly
from .utils import create_shortcode
#for dynamic url
from django.urls import reverse
#for login feature
from django.contrib.auth.decorators import login_required
#to get the domain name
#fromdjango.contrib.sites.models import Site
# Create your views here.
def index(request):
	objects = shorten.objects.all()[::-1]
	print(objects)

	context = {'objs': objects}
	return render(request, "index.html", context)


def create(request):
	form = bitlyForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.shortcode = create_shortcode()
		instance.datewise = "{}"
		instance.save()

		return HttpResponseRedirect(reverse("index"))

	context = {"urlform": form}
	return render(request, "create.html", context)

def goto(request, xyz=None):
	qs = get_object_or_404(shorten, shortcode__iexact=xyz)
	import json
	from .utils import current_date
	if qs:
		instance = json.loads(qs.datewise)
		if crt_date in instance:
			instance[crt_date] += 1
		else:
			instance[crt_date] = 1
		qs.datewise = json.dumps(instance)
		qs.save()
	return HttpResponseRedirect(qs.long_url)

def update(request, pk=None):
	if request.user.is_authenticated:
		qs = get_object_or_404(shorten, id=pk)
		form = editBitly(request.POST or None, instance=qs)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("index"))

		context = {'urlform': form}
		return render(request, "create.html", context)
	return HttpResponseRedirect(reverse("index"))
def delete(request, pk=None):
	if request.user.is_authenticated:
		qs = get_object_or_404(shorten, id=pk)
		qs.delete()
	return HttpResponseRedirect(reverse("index"))



