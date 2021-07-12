from django.http import HttpResponse
from django.shortcuts import redirect


def unauthonticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def  wrapper_func(request):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request)
			else:
				return HttpResponse("You are not autherised")
		return wrapper_func
	return decorator


def admin_only(view_func):
	def  wrapper_func(request, *args, **kwargs):

		request.user = request.session.get("email")
		print('====request====',request.user)
		
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		print('========',group)
		if group == 'User':
			return redirect('home')

		if group == 'Admin':
			return view_func(request, *args, **kwargs)
	return wrapper_func
