from django.db import models
from django.contrib.auth.models import User
#models for note

#Django will automatically map this to the database (it has an ORM)
class Note(models.Model):
    print(User) #see what User has
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #!django will automatically pass this in
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    #author will be a foreign key because author will be linked to the User table; this will be 1 author - n notes relationship
    # on_delete = models.CASCADE specify that when we delete an author, all notes of that author will be deleted
    #related_notes specify the field in User model which references all of the notes
    def __str__(self) -> str:
        return self.title
