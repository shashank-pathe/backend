from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('hello/', views.hello_world),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('user_details/', views.UserDetail.as_view(), name='user_list'),
    path('users/create/', views.CreateUser.as_view(), name='user_create'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
