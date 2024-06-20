from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

#Think of view as where data is taken and represented (sent) to front-end
#Every view should have permission_classes and serializer_class, queryset or some other methods you can generate query_set


#generics.CreateAPIView is a template view in Django, we can use it when we want to create view that handle creation of new objects
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #!list of all User objects, so that same user won't be repeated
    serializer_class = UserSerializer #!define kind a data that our API will accept, in this case datatype User
    permission_classes = [AllowAny] #define who can call this

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] #only access this route when we already pass the JWT tokenization

    def get_queryset(self):
        user = self.request.user #!take the current User object (that is the user requesting this API!! convenient)
        return Note.objects.filter(author = user) #used this to filter stuff, user can only read note of himself
    
    def perform_create(self, serializer):
        #data that we want to create will be passed into the serializer first, then we manually check if all data field is correct by calling is_valid
        if serializer.is_valid():
            serializer.save(author = self.request.user) #call this bc we specify {"author" : {"read-only": True}}
        else:
            raise RuntimeError(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)





