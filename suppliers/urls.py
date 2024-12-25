from rest_framework import routers
from .api import SupplierViewSet
router=routers.DefaultRouter()

router.register("api/suppliers",SupplierViewSet,"suppliers")

urlpatterns=router.urls
