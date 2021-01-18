from django.db import models

# Create your models here.

# class QueryImage(models.Model):
# 	image = models.ImageField(upload_to='images')
# 	uploaded_at = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
	image = models.ImageField(upload_to='images/')

'''
Fields:
	name: name of endpoint
	date created
'''
class Endpoint(models.Model):
	name = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)

'''
name of Algorithm 
code of Algorithm 
parent endpoint
'''
class OutfitRec(models.Model):
	name = models.CharField(max_length=128)
	code = models.CharField(max_length=50000)
	parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

'''
Process request of ML
'''
class Request(models.Model):
	input1 = models.TextField()
	input2 = models.TextField()
	full_response = models.CharField(max_length=10000)
	response = models.CharField(max_length=10000) 
	parent_mlalgorithm = models.ForeignKey(OutfitRec, on_delete=models.CASCADE)