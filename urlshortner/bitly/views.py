from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import shorten
from .forms import bitlyForm, editBitly
from .utils import create_shortcode
# Create your views here.
def index(request):
	objects = shorten.objects.all()
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

		return HttpResponseRedirect("http://127.0.0.1:8000/home/")

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
	qs = get_object_or_404(shorten, id=pk)
	form = editBitly(request.POST or None, instance=qs)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("http://127.0.0.1:8000/home/") 

	context = {'urlform': form}
	return render(request, "create.html", context)

def delete(request, pk=None):
	qs = get_object_or_404(shorten, id=pk)
	qs.delete()
	return HttpResponseRedirect("http://127.0.0.1:8000/home/")



