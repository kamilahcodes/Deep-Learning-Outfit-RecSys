from rest_framework import serializers
from .models import Endpoint
from .models import OutfitRec
from .models import Request


class EndpointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endpoint
		fields = ("name", "created_at")



class OutfitRecSerializer(serializers.ModelSerializer):
	class Meta:
		model = OutfitRec
		fields = ("name", "code", "parent_endpoint")


class RequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields = ("input1", "input2", "full_response", "response", "parent_mlalgorithm")