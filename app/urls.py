from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from app import  views
from app.views import BookViewSet, BookViewSet_detail
app_name = 'app'
books = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})
urlpatterns = [
  path('', books, name = 'books'),
  path('year/<int:publish_year>/', views.BooksByYear.as_view()),
  path('<int:pk>/', book_detail, name = 'book_detail'),
  path('genre/<str:genre>/', views.BooksByGenre.as_view()),
  path('author/<str:author>/', views.BooksByAuthor.as_view()),
  
]
urlpatterns = format_suffix_patterns(urlpatterns)