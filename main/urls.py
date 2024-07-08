# from django.urls import path, include
# from .views import ProdutoDetailAPIView, ProdutoListCreateAPIView

# urlpatterns = [
#     path('', ProdutoListCreateAPIView.as_view(), name='produto-listcreate'),
#     path('<int:pk>', ProdutoDetailAPIView.as_view(), name='produto-detail'),
# ]


# - - - - - Rotas usando Router e ViewSets - - - - - 
from .views import ProdutoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
urlpatterns = router.urls