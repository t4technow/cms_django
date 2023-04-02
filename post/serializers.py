from rest_framework import serializers  
from .models import Post, Category, Tag
  
class PostSerializer(serializers.ModelSerializer):  
    title = serializers.CharField(max_length=200)  
    slug = serializers.SlugField()
    
    class Meta:  
        model = Post  
        fields = ('title', 'slug')  