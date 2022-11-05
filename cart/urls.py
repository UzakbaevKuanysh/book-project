from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views

from cart.views import CartViewSet
app_name = 'cart'


urlpatterns = [
  path('', views.CartViewSet.as_view(), name = 'cart'),

  
]
urlpatterns = format_suffix_patterns(urlpatterns)