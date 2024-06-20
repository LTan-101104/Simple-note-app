from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#serializers take a Python object and convert into JSON, or vice versa
#Our API will accept JSON format and return JSON format (information about response,...), so we must have serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #User is a built-in model
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #!write_only means Django only accept the field password when receiving request but do not return password when respond back (nothing can read password)
    
    #serializers will look at the model in class Meta first, if it passed everything then it will take those datas and create a user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #**data: split up keywords and pass in dictionary form
        return user

#Serializer for the model Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}} #author will be designated when a user creates a note; we do not let others change this
    
