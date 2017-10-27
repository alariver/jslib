from django.db import models
from django.conf import settings             
#from django.utils.text import slugify 
from uuslug import slugify
from django.core.urlresolvers import reverse

# Create your models here. 
class Image(models.Model):
	"""docstring for Image"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, blank=True)
	
	url = models.URLField()
	image = models.ImageField(upload_to='images/%Y/%m/%d')
	description = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True, db_index=True) 
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
	
	def get_absolute_url(self):
		"""docstring for get_absolute_url"""
		return reverse('images:detail', args=[self.id, self.slug]);
	
	def __str__(self):
		"""docstring for __str__"""
		return self.title  
		
	def save(self, *args, **kwargs):
		"""docstring for save"""
		if not self.slug:
			self.slug = slugify(self.title)
			super(Image, self).save(*args, **kwargs)
