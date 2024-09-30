from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from.models import ColAgrupacionUnidadesEspaciales, ColDrr, ColFuenteAdministrativa, ColRrrFuente, ColUnidadEspacial, ExtArchivo, ExtDireccion, ExtInteresado, MaFuenteEspacial, MaInteresado, MaUab

from .serializer import ColAgrupacionUnidadesEspacialesSerializer, ColDrrSerializer, ColFuenteAdministrativaSerializer, ColRrrFuenteSerializer, ColUnidadEspacialSerializer, ExtArchivoSerializer, ExtDireccionSerializer, ExtInteresadoSerializer, MaFuenteEspacialSerializer, MaInteresadoSerializer, MaUabSerializer

# Create your views here.

class MaUabViews(viewsets.ModelViewSet):
    serializer_class = MaUabSerializer
    queryset = MaUab.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class MaFuenteEspacialViews(viewsets.ModelViewSet):
    serializer_class = MaFuenteEspacialSerializer
    queryset = MaFuenteEspacial.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ColAgrupacionUnidadesEspacialesViews(viewsets.ModelViewSet):
    serializer_class = ColAgrupacionUnidadesEspacialesSerializer
    queryset = ColAgrupacionUnidadesEspaciales.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ColDrrViews(viewsets.ModelViewSet):
    serializer_class = ColDrrSerializer
    queryset = ColDrr.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ColFuenteAdministrativaViews(viewsets.ModelViewSet):
    serializer_class = ColFuenteAdministrativaSerializer
    queryset = ColFuenteAdministrativa.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ColRrrFuenteViews(viewsets.ModelViewSet):
    serializer_class = ColRrrFuenteSerializer
    queryset = ColRrrFuente.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class ColUnidadEspacialViews(viewsets.ModelViewSet):
    serializer_class = ColUnidadEspacialSerializer
    queryset = ColUnidadEspacial.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ExtArchivoViews(viewsets.ModelViewSet):
    serializer_class = ExtArchivoSerializer
    queryset = ExtArchivo.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class ExtDireccionViews(viewsets.ModelViewSet):
    serializer_class = ExtDireccionSerializer
    queryset = ExtDireccion.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class ExtInteresadoViews(viewsets.ModelViewSet):
    serializer_class = ExtInteresadoSerializer
    queryset = ExtInteresado.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class MaInteresadoViews(viewsets.ModelViewSet):
    serializer_class = MaInteresadoSerializer
    queryset = MaInteresado.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

# Create your views here.

