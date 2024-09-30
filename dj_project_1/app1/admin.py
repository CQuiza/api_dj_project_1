#from django.contrib import admin
from django.contrib.gis import admin
from .models import Owners, PropertyLocation, Municipality, Party, Parcel #, PropertyBounding

# Register your models here.
admin.site.register(Owners)
admin.site.register(Party)
# admin.site.register(Deptos)
# admin.site.register(Mpios)

class CustomGeoadmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs':{
            'default_zoom': 12,
            'map_width': '100%',
            'map_height': '400px',
            'show_form': False,
            'default_lon': -74.0589,
            'default_lat': 4.6097,
            'default_crs': 'EPSG:4326',
            
        }
    }


@admin.register(PropertyLocation)
class PropertyLocationAdmin(CustomGeoadmin):
    pass

@admin.register(Municipality)
class MunicipalityAdmin(CustomGeoadmin):
    list_display = ('id', 'name_mpio', 'date_create', 'update_at')
    search_fields = ('name_mpio',)
    list_filter = ('date_create', 'update_at')

@admin.register(Parcel)
class ParcelAdmin(CustomGeoadmin):
    list_display = ('code', 'municipality' ,'party_owner', 'area', 'land_use', 'date_create', 'update_at')
    search_fields = ('code',)
    list_filter = ('municipality',)

    # list_display = ('id', 'owner', 'department', 'municipality', 'address', 'date_create', 'update_at')
    # search_fields = ('owner__name', 'owner__lastName', 'department__name_depto', 'municipality__name_mpio', 'address')
    # list_filter = ('owner__name', 'owner__lastName', 'department__name_depto')

# @admin.register(PropertyBounding)
# class PropertyBoundingAdmin(CustomGeoadmin):
#     list_display = ('id', 'location_id', 'description', 'name_surveyor', 'date_create', 'update_at')