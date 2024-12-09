from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProfesionalViewSet, CitaViewSet, historial_atencion

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('profesionales', ProfesionalViewSet)
router.register('citas', CitaViewSet)

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/historial_atencion/<int:cita_id>/', historial_atencion, name='historial_atencion'),
]
