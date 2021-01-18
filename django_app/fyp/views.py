from django.shortcuts import render
from .forms import QueryImageForm
#  rest api import
from rest_framework import viewsets
from rest_framework import mixins

from .models import Endpoint
from .serializers import EndpointSerializer

from .models import OutfitRec
from .serializers import OutfitRecSerializer

from .models import Request
from .serializers import RequestSerializer
#  keras imports

from keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16  
# tf ^
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import os
import sys
from numpy.linalg import norm
import json
import h5py
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pickle
from tensorflow.python.keras.models import model_from_json
global graph, model



# def init():
# 	json_file = open('fyp/model.json','r')
# 	loaded_model_json = json_file.read()
# 	json_file.close()
# 	loaded_model = model_from_json(loaded_model_json)
# 	# load wights into model
	
# 	loaded_model.load_weights("fyp/model.h5")
# 	graph = tf.compat.v1.get_default_graph()

# 	return loaded_model, graph

# vgg_model, graph = init()

# # Create your views here.

# # model = VGG16(weights='imagenet', include_top=False, input_shape =(224, 224, 3))
# # model1 = load_model('fyp/outfitrecsys1.h5')
# loaded_model_al = pickle.load(open('fyp/model1.pickle', 'rb'))


def queryimage(request):
	if request.method == 'POST':
		form = QueryImageForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.cleaned_data['image']
			print ('cleaned the image')
			
			image_feature = extract_features(image,vgg_model)
			image_feature2 = extract_features('fyp/trousers31.jpg',vgg_model)
			print(image_feature.shape)
			
			# pred = model1.predict([image_feature, image_feature])
			pred = loaded_model_al.predict([image_feature.reshape(1, -1), image_feature2.reshape(1, -1)])
			print(pred)

			
			
	else:
		form = QueryImageForm()
	return render(request,'forms/upload_form.html', {'form':form})


def getimage(image):
	print('i got the image')




def extract_features(path, model):
	img = image.load_img(path, target_size=(224, 224))
	img_array = image.img_to_array(img)
	expanded_img_array = np.expand_dims(img_array, axis=0)
	preprocessed_img = preprocess_input(expanded_img_array)
	features = model.predict(preprocessed_img)
	flattened_features = features.flatten()
	normalized_features = flattened_features / norm(flattened_features)

	return normalized_features


def get_recommendation():
	pass

	# insert the query feature
	#  random image1, get feature 
	# chedk that query and 1 is > 0.85
	# check that  query and random 2 >0.85
	# check that 1 and 2 >0.85
	# if all





class EndpointViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = EndpointSerializer
	queryset = Endpoint.objects.all()

class OutfitRecViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = OutfitRecSerializer
	queryset = OutfitRec.objects.all()

class RequestViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin):
	serializer_class = RequestSerializer
	queryset = Request.objects.all()













