from django.urls import path
from . import views

urlpatterns = [
    # Empresas
    path('empresas/', views.empresa_list, name='empresa_list'),
    path('empresas/nueva/', views.empresa_create, name='empresa_create'),
    path('empresas/<int:pk>/editar/', views.empresa_update, name='empresa_update'),
    path('empresas/<int:pk>/eliminar/', views.empresa_delete, name='empresa_delete'),
    
    # Tutores
    path('tutores/', views.tutor_list, name='tutor_list'),
    path('tutor/nuevo/', views.crear_tutor, name='crear_tutor'),
    
    # Diario
    path('diario/', views.diario_list, name='diario_list'),
    path('diario/nueva/', views.diario_create, name='diario_create'),
    path('diario/<int:pk>/editar/', views.diario_update, name='diario_update'),
    path('diario/<int:pk>/eliminar/', views.diario_delete, name='diario_delete'),
    path('tutores/<int:pk>/eliminar/', views.tutor_delete, name='tutor_delete'),
]