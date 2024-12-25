from .models import Supplier
from rest_framework import viewsets,permissions
from .serializers import SupplierSerializers
class SupplierViewSet(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=SupplierSerializers