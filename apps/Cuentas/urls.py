from django.conf.urls import url
from apps.Cuentas.views import *
from . import views

urlpatterns = [
    #-----------------------URL's de Tipos de Documentos---------------------------
    url(r'^nuevoTD/', views.TiposDocumentosCreate.as_view(), name='TiposDocumentos_Create'),
    url(r'^listaTD/', views.TiposDocumentosList.as_view(), name='TiposDocumentos_List'),
    url(r'^borrarTD/(?P<pk>[0-9]+)/$',views.TiposDocumentosDelete.as_view(), name='TiposDocumentos_Borrar'),
    url(r'^editarTD/(?P<pk>[0-9]+)/$', views.TiposDocumentosUpdate.as_view(), name='TiposDocumentos_Editar'),
    url(r'^detallesTD/(?P<pk>[0-9]+)/$', views.TiposDocumentosDetail.as_view(), name='TiposDocumentos_Detail'),
    url(r'^buscarTD/$', Search, name='TiposDocumentos_Serarch'),
    
    #-----------------------URL's de Clientes----------------------------------
    url(r'^nuevoCL/', views.ClientesCreate.as_view(), name='Clientes_Create'),
    url(r'^listaCL/', views.ClientesList.as_view(), name='Clientes_List'),
    url(r'^borrarCL/(?P<pk>[0-9]+)/$',views.ClientesDelete.as_view(), name='Clientes_Borrar'),
    url(r'^editarCL/(?P<pk>[0-9]+)/$', views.ClientesUpdate.as_view(), name='Clientes_Editar'),
    url(r'^detallesCL/(?P<pk>[0-9]+)/$', views.ClientesDetail.as_view(), name='Clientes_Detail'),
    
    
    #-----------------------URL's de Transacciones-----------------------------
    url(r'^nuevoTR/', views.TransaccionesCreate.as_view(), name='Transacciones_Create'),
    url(r'^listaTR/', views.TransaccionesList.as_view(), name='Transacciones_List'),
    url(r'^borrarTR/(?P<pk>[0-9]+)/$',views.TransaccionesDelete.as_view(), name='Transacciones_Borrar'),
    url(r'^editarTR/(?P<pk>[0-9]+)/$', views.TransaccionesUpdate.as_view(), name='Transacciones_Editar'),
    url(r'^detallesTR/(?P<pk>[0-9]+)/$', views.TransaccionesDetail.as_view(), name='Transacciones_Detail'),
  
    
    #-----------------------URL's de Asientos contables---------------------------
    url(r'^nuevoAC/', views.AsientosContablesCreate.as_view(), name='AsientosContables_Create'),
    url(r'^listaAC/', views.AsientosContablesList.as_view(), name='AsientosContables_List'),
    url(r'^borrarAC/(?P<pk>[0-9]+)/$',views.AsientosContablesDelete.as_view(), name='AsientosContables_Borrar'),
    url(r'^editarAC/(?P<pk>[0-9]+)/$', views.AsientosContablesUpdate.as_view(), name='AsientosContables_Editar'),
    url(r'^detallesAC/(?P<pk>[0-9]+)/$', views.AsientosContablesDetail.as_view(), name='AsientosContables_Detail'),
    
    url(r'^AC/', views.AsientosContables.as_view(), name='AsientosContables'),
    url(r'^EnviarAC/(?P<pk>[0-9]+)/$', views.Enviar_AsientosContables.as_view(), name='Enviar_AsientosContables'),
    
]

