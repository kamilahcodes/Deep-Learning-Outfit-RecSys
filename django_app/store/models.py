from django.db import models

# Create your models here.
class Product(models.Model):

	category_choices = [('Top', 'Top'), ('Bottom', 'Bottom'), ('Shoe', 'Shoe')]
	name = models.CharField(max_length=128)
	category = models.CharField(max_length=128,
								choices = category_choices,
								default = 'Top')
	price = models.CharField(max_length=10, default = '£20.00')

	image = models.ImageField(upload_to='product_images/')

	def __str__(self):
		return self.name
	# def get_absolute_url(self):
	# 	return '/products/' % self.pk

