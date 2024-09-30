from django.contrib.gis import admin
from .models import MaUab, MaFuenteEspacial,ExtArchivo, ColDrr, ColAgrupacionUnidadesEspaciales,ColRrrFuente,ColFuenteAdministrativa,ColUnidadEspacial,ExtDireccion, ExtInteresado,MaInteresado

# Register your models here.

admin.site.register(MaUab)
admin.site.register(MaFuenteEspacial)
admin.site.register(ExtArchivo)
admin.site.register(ColDrr)
admin.site.register(ColRrrFuente)
admin.site.register(ColFuenteAdministrativa)
admin.site.register(ExtInteresado)
admin.site.register(MaInteresado)


class CustomGeoadmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs':{
            'default_zoom': 5,
            'map_width': '100%',
            'map_height': '400px',
            'show_form': False,
            'default_lon': -74.0589,
            'default_lat': 4.6097,
            'default_crs': 'EPSG:4326'
            
        }
    }

@admin.register(ColUnidadEspacial)
class ColUnidadEspacialAdmin(CustomGeoadmin):
    pass

@admin.register(ColAgrupacionUnidadesEspaciales)
class ColAgrupacionUnidadesEspacialesAdmin(CustomGeoadmin):
    pass

@admin.register(ExtDireccion)
class ColExtDireccionAdmin(CustomGeoadmin):
    pass

