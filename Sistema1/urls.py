
from django.urls import path
from Sistema1 import views 

urlpatterns = [

    #Log
    path('base/',views.base, name = "base"),
    path('logout/',views.exit, name = "exitt"),   
    path('login/', views.Login_Template, name = "login"),
    path('register/', views.Register_Template, name = "register"),
    path('',views.Home, name = "Home"),    
    path('perfil/',views.perfil, name = "perfil"),    
    path('perfil/update_username/', views.update_username, name='update_username'),
    path('perfil/change_password/', views.change_password, name='change_password'),
    
    #convenios
    path('addConv/',views.Agregar_Convenios, name = "addConv"),
    path('ver_convenio/<str:nombre_archivo>/', views.ver_convenio, name='ver_convenio'),
    path('actualizar_Conv/<int:id>/', views.Actualizar_Convenio, name='actualizar_Conv'),
    path('eliminar_Conv/<int:id>/', views.Eliminar_Convenios, name='eliminar_Conv'),
    path('convenio/<int:id>/historial/', views.Ver_Historial_Convenio, name='ver_historial_convenio'),  
    path('ui1/<int:id>/', views.Ver_Historial_Convenio, name='H_convenio'),
    #campamento
    path('ver_convenio3/<str:nombre_archivo>/', views.ver_convenio3, name='ver_convenio3'),
    path('actualizar_Conv3/<int:id>/', views.Actualizar_Convenio3, name='actualizar_Conv3'),
    path('eliminar_Conv3/<int:id>/', views.Eliminar_Convenios3, name='eliminar_Conv3'),
    path('convenio3/<int:id>/historial/', views.Ver_Historial_Convenio3, name='ver_historial_convenio3'),  
    path('ui13/<int:id>/', views.Ver_Historial_Convenio3, name='H_convenio3'),
    path('addConv3/',views.Agregar_Convenios3, name = "addConv3"),
    path('Mun_List3/',views.Listar_Municipios3, name = "Mun_List3"),
    path('Agregar_Mun3/',views.Agregar_Mun3, name = "Agregar_Mun3"),
    path('actualizar_Mun3/<int:id>/', views.Actualizar_Municipio3, name='actualizar_Mun3'),
    path('deleteMun3/<int:id>/', views.Eliminar_Municipio3, name="delete_mun3"),
    path('detailsMun3/<int:id>/', views.detalles_Municipio3, name="md3"),
    #barrios
    path('ver_convenio2/<str:nombre_archivo>/', views.ver_convenio2, name='ver_convenio2'),
    path('actualizar_Conv2/<int:id>/', views.Actualizar_Convenio2, name='actualizar_Conv2'),
    path('eliminar_Conv2/<int:id>/', views.Eliminar_Convenios2, name='eliminar_Conv2'),
    path('convenio2/<int:id>/historial/', views.Ver_Historial_Convenio2, name='ver_historial_convenio2'),  
    path('ui12/<int:id>/', views.Ver_Historial_Convenio2, name='H_convenio2'),
    path('addConv2/',views.Agregar_Convenios2, name = "addConv2"),
    path('Mun_List2/',views.Listar_Municipios2, name = "Mun_List2"),
    path('Agregar_Mun2/',views.Agregar_Mun2, name = "Agregar_Mun2"),
    path('actualizar_Mun2/<int:id>/', views.Actualizar_Municipio2, name='actualizar_Mun2'),
    path('deleteMun2/<int:id>/', views.Eliminar_Municipio2, name="delete_mun2"),
    path('detailsMun2/<int:id>/', views.detalles_Municipio2, name="md2"),
    #Municipios
    path('Mun_List/',views.Listar_Municipios, name = "Mun_List"),
    path('Agregar_Mun/',views.Agregar_Mun, name = "Agregar_Mun"),
    path('actualizar_Mun/<int:id>/', views.Actualizar_Municipio, name='actualizar_Mun'),
    path('deleteMun/<int:id>/', views.Eliminar_Municipio, name="delete_mun"),
    path('detailsMun/<int:id>/', views.detalles_Municipio, name="md"),
    #Rendiciones
    path('rendiciones/',views.Lista_Rendiciones, name = "rendiciones"),
    path('agregar_rendicion',views.Agregar_Rendiciones, name='agregar_rendicion'),



]
