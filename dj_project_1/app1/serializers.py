from rest_framework import serializers # para crear las clases
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User # para manejar usuarios con django
from .models import Owners, Municipality, Parcel, Party # importar el modelo de la app1


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = '__all__'

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'

class ParcelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Parcel
        
        geo_field = 'geom'
        id_field = False
        auto_bbox = True
        fields = ('code', 'municipality', 'area', 'party_owner', 'land_use', 'date_create', 'update_at')

# class DeptosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deptos
#         fields = '__all__'

# class MpiosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mpios
#         fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'