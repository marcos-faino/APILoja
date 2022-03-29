from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (CategoriaAPIView,
                    CategoriasAPIView,
                    ProdutoAPIView,
                    ProdutosAPIView,
                    AvaliacaoAPIView,
                    AvaliacoesAPIView,
                    ProdutoViewSet,
                    AvaliacaoViewSet)

router = SimpleRouter()
router.register('produtos', ProdutoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('categorias/', CategoriasAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoriaAPIView.as_view(), name='categoria'),
    path('categorias/<int:categoria_pk>/produtos/',
         ProdutosAPIView.as_view(),
         name='categoria_produtos'),
    path('categorias/<int:categoria_pk>/produtos/<int:produto_pk>/',
         ProdutoAPIView.as_view(),
         name='categoria_produto'),

    path('produtos/', ProdutosAPIView.as_view(), name='produtos'),
    path('produtos/<int:produto_pk>/', ProdutoAPIView.as_view(), name='produto'),
    path('produtos/<int:produto_pk>/avaliacoes/',
         AvaliacoesAPIView.as_view(),
         name='produto_avaliacoes'),
    path('produtos/<int:produto_pk>/avaliacoes/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='produto_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
