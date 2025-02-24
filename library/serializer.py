from rest_framework import serializers
from .models import Book
from .models import Author


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    author =AuthorListSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class BookDetailSerializer(serializers.ModelSerializer):
    author =AuthorListSerializer()
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date']


