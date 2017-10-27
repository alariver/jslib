from django.http import HttpResponseBadRequest

def ajax_required(f):
	"""docstring for ajax_required"""
	def wrap(request, *args, **kwargs):
		"""docstring for wrap"""
		if not request.is_ajax():
			return HttpResponseBadRequest()
		return f(request, *args, **kwargs)
		
	wrap.__doc__ = f.__doc__
	wrap.__name__=f.__name__
	return wrap