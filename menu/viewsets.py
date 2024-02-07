from rest_framework import viewsets
from menu.models import Menu
from menu.serializres import MenuSerializers

class MenuViewset(viewsets.ModelViewSet):
    serializer_class = MenuSerializers


    def get_queryset(self):
        return Menu.objects.all()