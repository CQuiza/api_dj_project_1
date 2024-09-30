from django.urls import path, re_path, include
from .views import ColRrrFuenteViews, ColAgrupacionUnidadesEspacialesViews, ColFuenteAdministrativaViews, ColUnidadEspacialViews, ExtArchivoViews, ExtDireccionViews, ColDrrViews,ExtInteresadoViews, MaFuenteEspacialViews, MaInteresadoViews, MaUabViews
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'ma_uab', MaUabViews, 'ma_uab')
router.register(r'ma_fuente_espacial', MaFuenteEspacialViews, 'ma_fuente_espacial')
router.register(r'col_rrr_fuente', ColRrrFuenteViews, 'col_rrr_fuente')
router.register(r'col_agrupacion_unidades_espaciales', ColAgrupacionUnidadesEspacialesViews, 'col_agrupacion_unidades_espaciales')
router.register(r'col_fuente_administrativa', ColFuenteAdministrativaViews, 'col_fuente_administrativa')
router.register(r'col_unidad_espacial', ColUnidadEspacialViews, 'col_unidad_espacial')
router.register(r'ext_archivo', ExtArchivoViews, 'ext_archivo')
router.register(r'ma_interesado', MaInteresadoViews, 'ma_interesado')
router.register(r'ext_direccion', ExtDireccionViews, 'ext_direccion')
router.register(r'col_drr', ColDrrViews, 'col_drr')
router.register(r'ext_interesado', ExtInteresadoViews, 'ext_interesado')


urlpatterns = [
    path('', include(router.urls)),
    path('docs_ladm/', include_docs_urls(title='LADMCOL API')),
]

