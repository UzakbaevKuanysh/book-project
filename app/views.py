from django.shortcuts import render
from rest_framework import viewsets
from app.permissions import IsOwnerOrReadOnly
from app.serializers import BookSerializer,BookDetailSerializer
from app.models import Book
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework import permissions, generics
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookViewSet_detail(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class BooksByAuthor(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author = author)
class BooksByGenre(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        genre = self.kwargs['genre']
        return Book.objects.filter(genre = genre)
class BooksByYear(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        publish_year = self.kwargs['publish_year']
        return Book.objects.filter(publish_year = publish_year)

        