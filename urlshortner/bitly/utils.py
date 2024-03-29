import string
from .models import shorten 

def code_gen():
	import random
	shrtcd = ""
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	for i in range(6):
		shrtcd+=random.choice(chars)
	return shrtcd

def create_shortcode():
	shrtcd = code_gen()
	qs = shorten.objects.filter(shortcode__iexact=shrtcd)
	if qs.exists():
		return create_shortcode()
	else:
		return shrtcd

from datetime import date

def current_date():
	crt_date = date.today()
	return crt_date.strftime("%d-%m-%y")
