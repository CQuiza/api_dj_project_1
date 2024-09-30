from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime

# Create your models here.

class Owners(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    # more fields here...

    def __str__(self):
        return self.name
    
# class Deptos(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name_depto = models.CharField(max_length=30, null= False) 
#     id_depto = models.IntegerField(unique=True, null=False)
#     n_mpios = models.IntegerField(null=True)
#     population = models.IntegerField(blank=True)
#     age_creation = models.IntegerField(blank=True)
#     capital_city = models.CharField(max_length=30, null=False)
#     date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
#     update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

#     def __str__(self):
#         return self.name_depto
    
# class Mpios(models.Model):
#     id = models.AutoField(primary_key=True)
#     depto_id = models.ForeignKey(Deptos, on_delete=models.CASCADE, null=False)
#     name_mpio = models.CharField(max_length=30, null= False) 
#     id_mpio = models.IntegerField(unique=True, null=False)
#     n_veredas = models.IntegerField(null=True)
#     cabecera = models.CharField(max_length=30, null=False)
#     date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
#     update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

#     def __str__(self):
#         return self.name_mpio
    

class PropertyLocation(gis_models.Model):
    id = models.AutoField(primary_key=True)
    #owner = models.ForeignKey(Owners, on_delete=models.CASCADE, null=False)
    # department = models.ForeignKey(Deptos, on_delete=models.CASCADE, null=False)
    # municipality = models.ForeignKey(Mpios, on_delete=models.CASCADE, null=False)
    geom = gis_models.PointField(null=False)
    address = models.CharField(max_length=100)
    date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
    update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

    def __str__(self):
        return self.address
    
# class PropertyBounding(gis_models.Model):
#     id = models.AutoField(primary_key=True)
#     location_id = models.ForeignKey(PropertyLocation, on_delete=models.CASCADE, null=False)
#     description = models.CharField(max_length=300, help_text='Breve descripciòn del terreno')
#     name_surveyor = models.CharField(max_length=100, null=False)
#     geom = gis_models.MultiPolygonField(null=False)
#     date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
#     update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

#     def __str__(self):
#         return self.location_id

class Municipality(gis_models.Model):
    id = models.AutoField(primary_key=True)
    name_mpio = models.CharField(max_length=30, null=False)
    geom = gis_models.PointField(null=False, srid=4326)
    date_create = models.DateTimeField(default=datetime.now,null=False, blank=True)
    update_at = models.DateTimeField(default=datetime.now,null=False, blank=True)

    def __str__(self):
        return self.name_mpio
    

class Party(gis_models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    number_id = models.CharField(max_length=15, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=10, null= True)

    def __str__(self):
        return self.name
    
class Parcel(gis_models.Model):
    code = models.IntegerField(primary_key=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=False, related_name='parcels')
    area = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    party_owner = models.ForeignKey(Party, on_delete=models.CASCADE, null=False, related_name='parcels')
    geom = gis_models.PolygonField(null=False, srid=4326)
    land_use = models.CharField(max_length=100, choices=[('residential', 'residential'),('commercial', 'commercial'), ('agricultural', 'agricultural')])
    date_create = models.DateTimeField(default=datetime.now, null=False, blank=True)
    update_at = models.DateTimeField(default=datetime.now, null=False, blank=True)

    def __str__(self):
        return f'parcel {self.code} - {self.municipality.name_mpio}'


    
    
    


