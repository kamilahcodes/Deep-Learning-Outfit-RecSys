from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from .models import Product

import random

from keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16  

from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import os
import sys
from numpy.linalg import norm
import json
import h5py

import tensorflow as tf
import pickle
from tensorflow.python.keras.models import model_from_json
global graph, model


def init():
	# load wights into model
	json_file = open('fyp/model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("fyp/model.h5")
	graph = tf.compat.v1.get_default_graph()

	return loaded_model, graph

vgg_model, graph = init()


loaded_model_al = pickle.load(open('fyp/model1.pickle', 'rb'))

def product_list_view(request):
	query = Product.objects.all().order_by('?')
	context = {
		'allproducts': query
	}
	return render(request, "products/list.html", context)




def product_detail_view(request, pk=None, *args, **kwargs):
	instance = Product.objects.get(pk=pk)#id
	items = Product.objects.exclude(category=instance.category).order_by('?')

	def cal_rec1(instance, items):
		rec1 = None
		for item in items:
			score = check_score(item.image, instance.image)
			re_score = check_score(instance.image, item.image)
			print('btwen seed and rec1:', score )
			if (score > 0.90) or (re_score > 0.90):
				rec1 = item
				return rec1
			
				
	rec1 = cal_rec1(instance, items)
	

	def cal_rec2(instance):
		rec2 = None

		if (rec1 != None):
			
			items2 = Product.objects.exclude(category=rec1.category).exclude(category=instance.category).order_by('?')
			for i in items2:

				seed_score = check_score(instance.image, i.image)

				rec1_score = check_score(rec1.image, i.image)
				if (seed_score > 0.8 or check_score(i.image, instance.image) > 0.8) and (rec1_score>0.8 or check_score(i.image, rec1.image)):
					rec2 = i
					print(rec2)
					return rec2
					# break
					
	rec2 = cal_rec2(instance)




	context = {
		'product': instance,
		'rec1':rec1,
		'rec2': rec2
	
	}



	return render(request, "products/detail.html", context)


def product_cat_view(request, category):
	instance = Product.objects.filter(category=category)
	context = {
	'products': instance
	}

	return render(request, "products/category.html", context)


def check_score(i, j):
	i_feature = extract_features(i, vgg_model)
	j_feature = extract_features(j, vgg_model)

	prediction= loaded_model_al.predict([i_feature.reshape(1, -1), j_feature.reshape(1, -1)])
	
	return prediction



def extract_features(path, model):
	img = image.load_img(path, target_size=(224, 224))
	img_array = image.img_to_array(img)
	expanded_img_array = np.expand_dims(img_array, axis=0)
	preprocessed_img = preprocess_input(expanded_img_array)
	features = model.predict(preprocessed_img)
	flattened_features = features.flatten()
	normalized_features = flattened_features / norm(flattened_features)

	return normalized_features