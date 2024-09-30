from rest_framework import serializers # para crear las clases
from django.contrib.auth.models import User # para manejar usuarios con django
from .models import ColAgrupacionUnidadesEspaciales, ColDrr, ColFuenteAdministrativa, ColUnidadEspacial, ColRrrFuente, ExtArchivo, ExtDireccion, ExtInteresado, MaFuenteEspacial, MaInteresado, MaUab # importar el modelo de la app1


class MaUabSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaUab
        fields = '__all__'


class MaFuenteEspacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaFuenteEspacial
        fields = '__all__'


class ColDrrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColDrr
        fields = '__all__'


class ColFuenteAdministrativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColFuenteAdministrativa
        fields = '__all__'


class ColUnidadEspacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColUnidadEspacial
        fields = '__all__'


class ColRrrFuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColRrrFuente
        fields = '__all__'


class ExtArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtArchivo
        fields = '__all__'


class ExtDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtDireccion
        fields = '__all__'


class ExtInteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtInteresado
        fields = '__all__'


class MaInteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaInteresado
        fields = '__all__'

class ColAgrupacionUnidadesEspacialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColAgrupacionUnidadesEspaciales
        fields = '__all__'