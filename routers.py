from rest_framework import routers
from menu.viewsets import MenuViewset
router = routers.SimpleRouter()
router.register(r'menu', MenuViewset, basename='menu')
