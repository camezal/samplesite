from rest_framework import serializers
from .models import Bb

class BbSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bb
        fields=('title', 'content', 'price', 'published')
