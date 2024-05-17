from rest_framework import serializers
from . models import *

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = "__all__"