import projects
from rest_framework import serializers
from .models import Author, Project


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'author','published_on','project_image','live_link')

class MerchAuthor(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'sur_name','phone_number','email')