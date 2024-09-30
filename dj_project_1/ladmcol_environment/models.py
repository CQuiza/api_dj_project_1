from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime
# Create your models here.

class MaUab(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_Uab = models.CharField(null=False, choices=[
        ('MA_UAB_ReservaForetsalProtectoraProductora', 'RFPP'),
        ('MA_UAB_ReservaLey2da', 'Reserva ley 2da'),
        ('MA_UAB_ReservaForestalProtectoraNacional', 'RFPN'),
        ('MA_UAB_SustraccionLey2da', 'Sustraccion ley 2da')
    ])
    nom_ley2 = models.CharField()
    res_zoni = models.CharField()
    acto_admin = models.CharField()
    fecha_acto = models.CharField()
    fecha_ingreso = models.DateTimeField()
    fecha_recoleccion = models.DateTimeField()

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = f"ma_col'.'MaUab"
    
class MaFuenteEspacial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=50, null=False, choices=[
        ('Croquis_Campo', 'Croquis_Campo'),
        ('Datos_Crudos', 'Datos_Crudos'),
        ('Ortofoto', 'Ortofoto'),
        ('Informe_Tecnico', 'Informe_Tecnico'),
        ('Registro_Fotografico', 'Registro_Fotografico')
    ])
    descripcion = models.CharField(null=False)
    metadato = models.CharField()
    estado_disponibilidad = models.CharField(null=False, choices=[
        ('Convertido', 'Convertido'),
        ('Desconocido', 'Desconocido'),
        ('Disponible', 'Disponible')
    ])
    tipo_principal = models.CharField(choices=[
        ('imagen', 'imagen'),
        ('Documento', 'Documento'),
        ('Mapa', 'Mapa')
    ])
    fecha_documento_fuente = models.DateField()

    def __str__(self) -> str:
        return f'{self.nombre, self.id}'
    
    class Meta:
        db_table = f"ma_col'.'MaFuenteEspacial"



class ExtArchivo(models.Model):
    id = models.AutoField(primary_key=True)
    fuente_espacial_id = models.ForeignKey(MaFuenteEspacial,on_delete=models.CASCADE, unique=True, related_name= 'ExtArchivo')
    fecha_aceptacion = models.DateField()
    datos = models.CharField()
    extraccion = models.DateField()
    fecha_grabacion = models.DateField()
    fecha_entrega = models.DateField()
    espacio_nombres = models.CharField(null=False)
    local = models.CharField(null=False)

    def __str__(self) -> str:
        return f'{self.espacio_nombres, self.id}'
    
    class Meta:
        db_table = "ma_col'.'ExtArchivo"
    

class ColDrr(models.Model):
    id = models.AutoField(primary_key=True)
    ma_uab_id = models.ForeignKey(MaUab,on_delete=models.CASCADE, related_name='ColDrr')
    descripcion = models.CharField()

    def __str__(self) -> str:
        return f'{self.ma_uab_id, self.id}'
    
    class Meta:
        db_table = 'ma_col'
    

class MaInteresado(models.Model):
    id = models.AutoField(primary_key=True)
    col_drr_id = models.ForeignKey(ColDrr, on_delete=models.CASCADE, null=True, related_name='MaInteresado')
    tipo = models.CharField(choices=[
        ('Grupo_Civil', 'Grupo_Civil'),
        ('Grupo_Empresarial', 'Grupo_Empresarial'),
        ('Grupo_Etnico', 'Grupo_Etnico'),
        ('Grupo_Mixto', 'Grupo_Mixto')
    ])
    nombre = models.CharField()

    def __str__(self) -> str:
        return f'{self.col_drr_id, self.id}'
    
    class Meta:
        db_table = f"ma_col'.'MaInteresado"

class ExtInteresado(models.Model):
    id = models.AutoField(primary_key=True)
    ma_interesado_id = models.ForeignKey(MaInteresado, on_delete=models.CASCADE, related_name='ExtInteresado')
    nombre = models.CharField()

    def __str__(self) -> str:
        return f'{self.nombre, self.id}'
    
    class Meta:
        db_table = f"ma_col'.'ExtInteresado"

class ExtDireccion(gis_models.Model):
    id = models.AutoField(primary_key=True)
    ext_interesado_id = models.ForeignKey(ExtInteresado, on_delete=models.CASCADE, related_name='ExtDireccion')
    tipo = models.CharField(null=False, choices=[
        ('Domicilio_Particular', 'Domicilio_Particular'),
        ('Domicilio_Comercial', 'Domicilio_Comercial')
    ])
    calle = models.CharField()
    codigo_postal = models.CharField()
    geom = gis_models.PointField(srid=4326)
    sector = models.CharField()

    def __str__(self) -> str:
        return f'{self.tipo, self.id}'
    
    class Meta:
        db_table = f"ma_col'.'ExtDireccion"

class ColFuenteAdministrativa(models.Model):
    id = models.AutoField(primary_key=True)
    estado_disponibilidad = models.CharField(null=False, choices=[
        ('Convertido', 'Convertido'),
        ('Desconocido', 'Desconocido'),
        ('Disponible', 'Disponible')
    ])
    observacion = models.CharField()

    def __str__(self) -> str:
        return f'{self.estado_disponibilidad, self.id}'
    
    class Meta:
        db_table = f"ma_col'.'ColFuenteAdministrativa"


class ColUnidadEspacial(gis_models.Model):
    id = models.AutoField(primary_key=True)
    geom = gis_models.MultiPolygonField(srid=4326)
    tipo_unidad_espacial = models.CharField(null=False, choices=[
        ('MA_UAB_ReservaForetsalProtectoraProductora', 'RFPP'),
        ('MA_UAB_ReservaLey2da', 'Reserva ley 2da'),
        ('MA_UAB_ReservaForestalProtectoraNacional', 'RFPN'),
        ('MA_UAB_SustraccionLey2da', 'Sustraccion ley 2da')
    ])
    
    def __str__(self) -> str:
        return f'{self.id}'
    
    class Meta:
        db_table = f"ma_col'.'ColUnidadEspacial"

class ColAgrupacionUnidadesEspaciales(gis_models.Model):
    id = models.AutoField(primary_key=True)
    nivel_jerarquico = models.IntegerField(null=False)
    nombre = models.CharField()
    geom = gis_models.MultiPolygonField(srid=4326)
    col_unidad_espacial_id = models.ForeignKey(ColUnidadEspacial, on_delete=models.CASCADE, related_name='ColAgrupacionUnidadesEspaciales', null=True)

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = f"ma_col'.'ColAgrupacionUnidadesEspaciales"



# -----> Tablas de relaciones --------------


# Relacion ColDrr - ColFuenteAdministrativa
class ColRrrFuente(models.Model):
    id = models.AutoField(primary_key=True)
    col_drr_id = models.ForeignKey(ColDrr, on_delete=models.CASCADE, related_name='ColRrrFuente')
    col_fuente_administrativa_id = models.ForeignKey(ColFuenteAdministrativa, on_delete=models.CASCADE, related_name='ColRrrFuente', null=True)

    def __str__(self) -> str:
        return f'{self.col_drr_id, self.col_fuente_administrativa_id}'
    
    class Meta:
        db_table = f"ma_col'.'ColRrrFuente"


# Relacion ColDrr - MaInteresado


# Relacion ExtInteresado - ExtDireccion





    


