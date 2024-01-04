from django.shortcuts import render
from urllib import request
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from mainapp.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from mainapp.paginations import *
from .serializers import *
from mainapp.filters import *
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, login, authenticate


class LoginView(APIView):
    # permission_classes = [IsCompanyLead]
    def post(self, request, *args, **kwargs):
        print('1')
        print(request.data)
        print('2')
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"sifre ve ya username yanlisdir"})
        login(request, user)
        
        
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
            
        }
        return Response({"username": username, "tokens": tokens,"userId":user.id}, status=201)

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegistrationView(APIView):     
    def post(self,request,format=None):
 
        data = request.data
        user_serializer = RegistrationSerializer(data=data)
        
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()

        return Response({"Status": "success", "data": user_serializer.data}, status=200)


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    filter_backends = (DjangoFilterBackend,)
    
class ProductSingleView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
class ProductCreateView(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSingleView(generics.RetrieveUpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CheckAuth(APIView):
    def get(self, request):
        print('1')
        data = {}
        print(2)
        user = request.user
        print('3')
        if user.is_authenticated:  
            print('4')
            data['token'] = True
            data['name'] = user.first_name + ' ' + user.last_name
        else:
            print('5')
            data['token'] = False
        return Response(data)
# class BasketView(APIView):
#     serializer_class = BasketSerializer
#     queryset = BasketItem

#     def post(request):
#         data = request.data


    
# #END Homepage 
    
# #Fav
# class AddFavView(generics.CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = FavouritesAddSerializer
#     queryset = Favourites.objects.all()

        
#     def perform_create(self, serializer):
        
#         talent = serializer.validated_data.get('talent')
        
#         if Favourites.objects.filter(user=self.request.user, talent=talent).exists():
  
#             raise serializers.ValidationError("Favourite already exists for this user and talent")
#         return serializer.save(user=self.request.user)
    
# class ListFavView(generics.ListAPIView):
#     serializer_class = FavouritesListSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         queryset = Favourites.objects.filter(user = user)
#         return queryset
    
# class DeleteFromFav(generics.DestroyAPIView):
#     queryset = Favourites.objects.all()
#     serializer_class = FavouritesDeleteSerializer
#     lookup_field = 'id'

#     def perform_destroy(self, instance):
#         instance.delete()

# class DeleteFromFavWithTalentId(APIView):
#     def post(self,request):
#         talent_id = self.request.data.get('talent_id')
#         user = self.request.user
#         print(user)
        
#         try:
#             fav = Favourites.objects.get(user=user,talent=talent_id)
#         except:
#             fav = '1'
#         if fav != '1':
#             fav.delete()
#         else:
#             return Response({"message":"Not exists"},status=200)

#         return Response({"message":"Sucess"},status=204)