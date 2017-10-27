from django.contrib.auth.models import User

class EmailAuthBackend(object):
	"""docstring for EmailAuthBackend"""
	def authenticate(self, username=None, password=None):
		"""docstring for authenticate"""
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
			
	def get_user(self, user_id):
		"""docstring for get_user"""
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
		