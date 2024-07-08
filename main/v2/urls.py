from .views import ProdutoViewSet, LojaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'lojas', LojaViewSet)
urlpatterns = router.urls