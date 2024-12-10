from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProfesionalViewSet, CitaViewSet, custom_api

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('profesionales', ProfesionalViewSet)
router.register('citas', CitaViewSet)

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('custom/', custom_api),
]
