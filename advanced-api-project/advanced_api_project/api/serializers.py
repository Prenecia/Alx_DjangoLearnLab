from datetime import timezone
from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
        