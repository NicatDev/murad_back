from django.urls import path
from mainapp.views import *
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("products", ProductView.as_view(), name="products"),
    path("productCreate", ProductCreateView.as_view(), name="ProductCreateView"),
    path("product/<pk>", ProductSingleView.as_view(), name="products"),
    
    path("register", RegistrationView.as_view(), name="register"),
    path("RegisterView", RegisterView.as_view(), name="RegisterView"),
]