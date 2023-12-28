from rest_framework import serializers
from mainapp.models import *

"""{"username":"admin","password":"123123","email":"n@gmail.com","first_name":"admin","last_name":"admin","is_superuser":true,"is_staff":true}"""

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"})
    
    class Meta:
        model = User
        fields = ("email","password","username", "id",'first_name','last_name','is_superuser',"is_staff")
        
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "slug": {
                "read_only": True
            }
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        username = attrs.get("username")
        username_qs = User.objects.filter(username=username).exists()
        email_qs = User.objects.filter(email=email).exists()
        if email_qs:
            raise serializers.ValidationError("Bu email ile artiq qeydiyyatdan kecilib")
        if username_qs:
            raise serializers.ValidationError("Bu username ile artiq qeydiyyatdan kecilib")
        if password:
            if len(password) < 6:
                raise serializers.ValidationError("Sifre en azi 6 simvoldan ibaret olmalidir")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            **validated_data
        )
        user.set_password(password)
        
        user.is_active = True
        user.save()   
        # send mail
    
        return user
    
    
