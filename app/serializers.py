from rest_framework import serializers
# from .models import ModelClassName
from django.conf import settings


class ModelClassNameSerializer(serializers.ModelSerializer):
	model = ModelClassName
	fields = '__all__'
